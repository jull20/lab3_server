from fastapi import APIRouter, HTTPException, status

from v1.auth.schema import ResponseSuccess


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    path='/register',
    summary="Регистрация нового пользователя",
    response_model=ResponseSuccess,
    responses={} # TODO: wrong fields
)   
async def register(
    # TODO: db, userSession and bodyScheme here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/login',
    summary='Вход в аккаунт, получение сессии',
    response_model=ResponseSuccess,
    responses={} # TODO: wrong username or password
)
async def login(
    # TODO: db, userSession and bodyScheme here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")