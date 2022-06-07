from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/products', tags=['products'])

@router.get(
    path='/'
)
async def get_all_products():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/'
)
async def create_new_product():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.get(
    path='/{productId}'
)
async def get_product_by_id():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/{productId}/rate'
)
async def set_rate_to_product_by_id():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/{productId}/buy'
)
async def buy_product_by_id():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")