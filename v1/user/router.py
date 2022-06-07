from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/user', tags=['user'])

@router.get(
    path='/isadmin'
)
async def get_user_admin_or_not():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")