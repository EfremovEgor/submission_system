from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db
from .models import Submission
from . import service


async def submission_by_id(
    submission_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> Submission:
    submission = await service.get_submission(session, submission_id)
    if submission is not None:
        return submission

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Conference {submission_id} not found!",
    )
