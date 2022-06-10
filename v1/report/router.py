from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.settings.database import get_db
from core.utils.permissions import get_admin_user_from_session

from v1.user.schema import UserSession
from v1.report.controller import *


router = APIRouter(prefix='/report', tags=['report'])


@router.get(
    path='/',
    summary="Получить отчеты по продажам в виде файла",
    response_model=None,
)
async def get_csv_file_with_orders_report(
    user: UserSession = Depends(get_admin_user_from_session),
    db: Session = Depends(get_db)
):
    return await make_orders_report(db, user)