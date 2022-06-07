from fastapi import APIRouter, HTTPException, status

from v1.user.schema import ResponseIsAdmin


router = APIRouter(prefix='/user', tags=['user'])


@router.get(
    path='/isadmin',
    summary='Получение информации, является ли текущий пользователь админом',
    response_model=ResponseIsAdmin,
)
async def get_user_admin_or_not(
    # TODO: db and userSession here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")