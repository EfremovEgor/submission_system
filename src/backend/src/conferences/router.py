from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from auth.dependencies import super_user_dependency
from users.schemas import UserBase

from .models import Conference, Topic
from .schemas.conference import (
    ConferenceBase,
    ConferenceInDBBase,
    ConferenceUpdate,
    ConferenceCreate,
    ConferenceCreateIn,
)
from .schemas.topic import (
    TopicBase,
    TopicCreate,
    TopicInDBBase,
)
from .dependencies import conference_by_acronym, conference_by_id, topic_by_id
from core.database import db
from . import service


from auth.dependencies import super_user_dependency


router = APIRouter(
    prefix="/conferences",
    tags=["Conferences"],
)


@router.get("/topics", response_model=list[TopicInDBBase])
async def get_topics(
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return await service.get_topics(session)


@router.get("/topics/{topic_id}", response_model=TopicInDBBase)
async def get_topic(
    topic: Topic = Depends(topic_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return topic


@router.post("/topics", response_model=TopicInDBBase)
async def create_topic(
    topic_in: TopicCreate,
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    try:
        return await service.create_topic(session, topic_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Conference already exists"
        )


@router.get("/", response_model=list[ConferenceInDBBase])
async def get_conferences(
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return await service.get_conferences(session)


@router.get("/{conference_id}", response_model=ConferenceInDBBase)
async def get_conference(
    conference=Depends(conference_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return conference


@router.get("/by_acronym/{acronym}", response_model=ConferenceInDBBase)
async def get_conference_by_acronym(
    conference=Depends(conference_by_acronym),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return conference


@router.post("/", response_model=ConferenceInDBBase)
async def create_conference(
    conference_in: ConferenceCreateIn,
    session: AsyncSession = Depends(db.scoped_session_dependency),
    current_super_user: UserBase = Depends(super_user_dependency),
):

    conference_in = ConferenceCreate(
        **conference_in.model_dump(), user_id=current_super_user.id
    )
    try:
        return await service.create_conference(session, conference_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Conference already exists"
        )


@router.put("/{conference_id}/", response_model=ConferenceBase)
async def update_conference(
    conference_update: ConferenceUpdate,
    conference=Depends(conference_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return await service.update_conference(
        session=session,
        conference=conference,
        conference_update=conference_update,
    )


@router.patch("/{conference_id}/", response_model=ConferenceInDBBase)
async def update_conference_partial(
    conference_update: ConferenceUpdate,
    conference=Depends(conference_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await service.update_conference(
        session=session,
        conference=conference,
        conference_update=conference_update,
        partial=True,
    )


@router.delete("/{conference_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conference(
    conference=Depends(conference_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> None:
    await service.delete_conference(session=session, conference=conference)
