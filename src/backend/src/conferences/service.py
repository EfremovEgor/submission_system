from fastapi.background import P
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas.conference import (
    ConferenceCreate,
    ConferenceUpdate,
)
from .schemas.topic import (
    TopicCreate,
)
from .models import Conference, Topic
from users.service import get_user_by_email


async def get_topics(session: AsyncSession) -> list[Topic]:
    stmt = select(Topic).order_by(Topic.id)
    result: Result = await session.execute(stmt)
    topics = result.scalars().all()
    return list(topics)


async def get_topic(session: AsyncSession, topic_id: int) -> Topic:
    return await session.get(Topic, topic_id)


async def create_topic(session: AsyncSession, topic_in: TopicCreate) -> Topic:
    topic = Topic(**topic_in.model_dump())
    session.add(topic)
    await session.commit()
    return topic


async def get_conferences(session: AsyncSession) -> list[Conference]:
    stmt = select(Conference).order_by(Conference.id)
    result: Result = await session.execute(stmt)
    conferences = result.unique().scalars().all()
    return list(conferences)


async def get_conference(session: AsyncSession, conference_id: int) -> Conference:
    return await session.get(Conference, conference_id)


async def get_conference_by_acronym(
    session: AsyncSession, conference_acronym: str
) -> Conference:
    return await session.get(Conference, acronym=conference_acronym)


async def create_conference(
    session: AsyncSession, conference_in: ConferenceCreate
) -> Conference:
    conference = Conference(**conference_in.model_dump(exclude=["reviewers", "topics"]))

    to_add = list()
    to_add.append(conference_in.user_id)

    for reviewer in conference_in.reviewers:
        if (
            user := await get_user_by_email(session, reviewer.email)
        ) is not None and user not in to_add:
            to_add.append(user)
    session.add(conference)
    await session.commit()
    await session.refresh(conference)
    to_add = list()
    for topic in conference_in.topics:
        topic = TopicCreate(**topic.model_dump(), conference_id=conference.id)
        created_topic = await create_topic(session, topic)
        to_add.append(created_topic.id)

    await session.commit()
    return conference


async def update_conference(
    session: AsyncSession,
    conference: Conference,
    conference_update: ConferenceUpdate,
    partial: bool = False,
) -> Conference:

    for name, value in conference_update.model_dump(
        exclude_unset=partial, exclude=["reviewers"]
    ).items():
        setattr(conference, name, value)
    to_add = list()
    to_add.append(conference.user_id)
    for user_email in conference_update.reviewers:
        if (
            user := await get_user_by_email(session, user_email)
        ) is not None and user.id not in to_add:
            to_add.append(user.id)

    if to_add:
        conference.reviewers = to_add
    else:
        conference.reviewers.clear()
    await session.commit()
    return conference


async def delete_conference(session: AsyncSession, conference: Conference) -> None:
    await session.delete(conference)
    await session.commit()


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
