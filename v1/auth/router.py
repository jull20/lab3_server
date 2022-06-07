from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post(
    path='/register'
)   
async def register():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")

@router.post(
    path='/login'
)
async def login():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")