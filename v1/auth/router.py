from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from v1.auth.schema import ResponseSuccess
from core.settings.database import get_db


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    path='/register',
    summary="Регистрация нового пользователя",
    response_model=ResponseSuccess,
    responses={} # TODO: wrong fields
)   
async def register(
    # TODO: userSession and bodyScheme here
    db: Session = Depends(get_db)
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/login',
    summary='Вход в аккаунт, получение сессии',
    response_model=ResponseSuccess,
    responses={} # TODO: wrong username or password
)
async def login(
    # TODO: userSession and bodyScheme here
    db: Session = Depends(get_db)
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/logout',
    summary='Выход из аккаунта',
    response_model=ResponseSuccess
)
async def logout(
    # TODO: userSession here
    db: Session = Depends(get_db)
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")