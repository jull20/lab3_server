from fastapi import APIRouter

router = APIRouter(prefix='/home', tags=['default'])


@router.get(
    path='/'
)
async def hello():
    return { "message": "Hello pidors" }