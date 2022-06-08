from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from v1.user.schema import ResponseIsAdmin
from core.settings import get_db


router = APIRouter(prefix='/user', tags=['user'])


@router.get(
    path='/isadmin',
    summary='Получение информации, является ли текущий пользователь админом',
    response_model=ResponseIsAdmin,
)
async def get_user_admin_or_not(
    # TODO: userSession here
    db: Session = Depends(get_db)
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")