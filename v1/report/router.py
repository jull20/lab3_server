from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.settings import get_db


router = APIRouter(prefix='/report', tags=['report'])


@router.get(
    path='/',
    summary="Получить отчеты по продажам в виде файла",
    response_model=None,
)
async def get_csv_file_with_orders_report(
    # TODO: userSession here
    db: Session = Depends(get_db)
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")