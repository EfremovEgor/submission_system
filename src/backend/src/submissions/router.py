from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from auth.dependencies import super_user_dependency
from auth.dependencies import active_user_dependency
from users.models import User
from mailing.tasks import send_submission_email
from users.schemas import UserBase

from .models import Submission
from .schemas import (
    SubmissionBase,
    SubmissionCreate,
    SubmissionCreateIn,
    SubmissionInDBBase,
    SubmissionUpdate,
)
from .dependencies import submission_by_id
from core.database import db
from . import service
from conferences.service import get_conference

from auth.dependencies import super_user_dependency


router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"],
)


@router.get("/", response_model=list[SubmissionInDBBase])
async def get_submissions(
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester=Depends(super_user_dependency),
):

    return await service.get_submissions(session)


@router.get("/from_conference/{conference_id}", response_model=list[SubmissionInDBBase])
async def get_submissions_from_conference(
    conference_id: int,
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester=Depends(active_user_dependency),
):
    access_granted = False

    if requester.is_super_user:

        access_granted = True
    if not access_granted:

        conference = await get_conference(session, conference_id)

        for reviewer in conference.reviewers:

            if reviewer.id == requester.id:
                access_granted = True

                break
    if not access_granted:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return await service.get_submissions(session, from_conference=conference_id)


@router.get("/{submission_id}", response_model=SubmissionInDBBase)
async def get_submission(
    submission: Submission = Depends(submission_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester: User = Depends(active_user_dependency),
):
    if (
        (submission.user.id == requester.id)
        or (requester.is_super_user)
        or (
            submission.conference.id
            in [conference.id for conference in requester.reviewer_in]
        )
    ):
        return submission

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@router.post("/", response_model=SubmissionInDBBase)
async def create_submission(
    submission_in: SubmissionCreateIn,
    session: AsyncSession = Depends(db.scoped_session_dependency),
    user: UserBase = Depends(active_user_dependency),
):
    submission_in = SubmissionCreate(user_id=user.id, **submission_in.model_dump())
    try:
        result = await service.create_submission(session, submission_in)
        to_send = result.to_dict()
        to_send["topic"] = result.topic.to_dict()
        send_submission_email.delay(
            email=user.email,
            submission_data=to_send,
            user=user.to_dict(),
        )

        return result
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Submission already exists"
        )


# @router.put("/{conference_id}/", response_model=SubmissionBase)
# async def update_conference(
#     conference_update: SubmissionUpdate,
#     conference=Depends(conference_by_id),
#     session: AsyncSession = Depends(db.scoped_session_dependency),
# ):

#     return await service.update_conference(
#         session=session,
#         conference=conference,
#         conference_update=conference_update,
#     )


# @router.patch("/{conference_id}/", response_model=SubmissionInDBBase)
# async def update_conference_partial(
#     conference_update: SubmissionUpdate,
#     conference=Depends(conference_by_id),
#     session: AsyncSession = Depends(db.scoped_session_dependency),
# ):
#     return await service.update_conference(
#         session=session,
#         conference=conference,
#         conference_update=conference_update,
#         partial=True,
#     )


# @router.delete("/{conference_id}/", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_conference(
#     conference=Depends(conference_by_id),
#     session: AsyncSession = Depends(db.scoped_session_dependency),
# ) -> None:
#     await service.delete_conference(session=session, conference=conference)
