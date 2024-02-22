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


# async def update_conference(
#     session: AsyncSession,
#     conference: Conference,
#     conference_update: ConferenceUpdate,
#     partial: bool = False,
# ) -> Conference:

#     for name, value in conference_update.model_dump(exclude_unset=partial).items():
#         setattr(conference, name, value)
#     await session.commit()
#     return conference


# async def delete_conference(session: AsyncSession, conference: Conference) -> None:
#     await session.delete(conference)
#     await session.commit()
