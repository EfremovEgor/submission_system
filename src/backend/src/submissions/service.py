from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import SubmissionUpdate, SubmissionCreate
from .models import Submission, Author


async def get_submissions(
    session: AsyncSession, from_conference: int = None
) -> list[Submission]:
    stmt = select(Submission).order_by(Submission.id)
    if from_conference is not None:
        stmt = (
            select(Submission)
            .order_by(Submission.id)
            .where(Submission.conference_id == from_conference)
        )
    result: Result = await session.execute(stmt)
    submissions = result.scalars().all()
    return list(submissions)


async def get_submission(session: AsyncSession, submission_id: int) -> Submission:
    return await session.get(Submission, submission_id)


async def create_submission(
    session: AsyncSession, submission_in: SubmissionCreate
) -> Submission:
    submission = Submission(**submission_in.model_dump(exclude=("authors", "topic")))
    session.add(submission)
    await session.commit()
    to_add = list()
    await session.refresh(submission, ["authors", "topic"])
    for author in submission_in.authors:
        to_add.append(Author(submission_id=submission.id, **author.model_dump()))
    session.add_all(to_add)
    await session.commit()
    return submission


async def delete_submission(session: AsyncSession, submission: Submission) -> None:
    await session.delete(submission)
    await session.commit()


async def update_submission(
    session: AsyncSession,
    submission: Submission,
    submission_update: SubmissionUpdate,
    partial: bool = False,
) -> Submission:

    for name, value in submission_update.model_dump(
        exclude_unset=partial, exclude=("authors", "topic")
    ).items():
        setattr(submission, name, value)
    to_add = list()
    for author in submission.authors:
        await session.delete(author)
    if not submission_update.authors:
        return submission
    for author in submission_update.authors:
        to_add.append(Author(submission_id=submission.id, **author.model_dump()))
    submission.authors = to_add
    await session.commit()
    return submission
