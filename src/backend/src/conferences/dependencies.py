from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db
from .models import Conference
from . import service


async def conference_by_id(
    conference_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> Conference:
    conference = await service.get_conference(session, conference_id)
    if conference is not None:
        return conference

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Conference {conference_id} not found!",
    )


async def topic_by_id(
    topic_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> Conference:
    topic = await service.get_topic(session, topic_id)
    if topic is not None:
        return topic

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Topic {topic_id} not found!",
    )
