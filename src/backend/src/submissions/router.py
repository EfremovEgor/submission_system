from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from auth.dependencies import super_user_dependency
from auth.dependencies import active_user_dependency
from users.models import User
from mailing.tasks import send_create_submission_email, send_update_submission_email
from users.schemas import UserBase
from mailing.schemas import SubmissionEmailData
from .models import Submission
from .schemas import (
    SubmissionCreate,
    SubmissionCreateIn,
    SubmissionInDBBase,
    SubmissionUpdate,
    Author,
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
        submission = await service.create_submission(session, submission_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Submission already exists"
        )
    await session.refresh(submission, ["authors", "topic"])
    authors = [Author(**author.to_dict()) for author in submission.authors]
    for author in authors:
        if author.is_corresponding:
            send_create_submission_email.delay(
                email=author.email,
                data=SubmissionEmailData(
                    submission_id=submission.id,
                    conference_email=submission.conference.email,
                    conference_name=submission.conference.name,
                    conference_short_name=submission.conference.short_name,
                    first_name=author.first_name,
                    last_name=author.last_name,
                    corresponding_title=author.title,
                    title=submission.title,
                    presentation_format=submission.presentation_format,
                    topic=submission.topic.name,
                    authors=authors,
                ).model_dump(),
            )

    return submission


@router.delete("/{submission_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_submission(
    submission=Depends(submission_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester: User = Depends(active_user_dependency),
) -> None:
    if (
        (submission.user.id == requester.id)
        or (requester.is_super_user)
        or (
            submission.conference.id
            in [conference.id for conference in requester.reviewer_in]
        )
    ):
        await service.delete_submission(session=session, submission=submission)
        return
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@router.patch("/{submission_id}", response_model=SubmissionInDBBase)
async def update_submission_partial(
    submission_update: SubmissionUpdate,
    submission=Depends(submission_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester: User = Depends(active_user_dependency),
):
    access_granted = False
    if requester.is_super_user:
        access_granted = True
    if requester.id == submission.user.id:
        access_granted == True
    if not access_granted:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    submission = await service.update_submission(
        session=session,
        submission=submission,
        submission_update=submission_update,
        partial=True,
    )

    await session.refresh(submission, ["authors", "topic"])

    authors = [Author(**author.to_dict()) for author in submission.authors]
    for author in submission.authors:
        if author.is_corresponding:
            send_update_submission_email.delay(
                email=author.email,
                data=SubmissionEmailData(
                    submission_id=submission.id,
                    conference_email=submission.conference.email,
                    conference_name=submission.conference.name,
                    conference_short_name=submission.conference.short_name,
                    first_name=author.first_name,
                    last_name=author.last_name,
                    corresponding_title=author.title,
                    title=submission.title,
                    presentation_format=submission.presentation_format,
                    topic=submission.topic.name,
                    authors=authors,
                ).model_dump(),
            )
    return submission
