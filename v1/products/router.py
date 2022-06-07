from fastapi import APIRouter, HTTPException, status, Path

from v1.products.schema import ResponseProduct, ResponseSuccess


router = APIRouter(prefix='/products', tags=['products'])


@router.get(
    path='/',
    summary='Получение списка все товаров',
    response_model=list[ResponseProduct],
)
async def get_all_products(
    # TODO: db and userSession here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/',
    summary='Создание нового объекта товара',
    response_model=ResponseSuccess,
    responses={} # TODO: something wrong
)
async def create_new_product(
    #TODO: db, userSession and bodyScheme here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.get(
    path='/{productId}',
    summary='Получение одного товара, по его id',
    response_model=ResponseProduct,
    responses={} # TODO: if wrong id 4xx response
)
async def get_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    # TODO: db and userSession here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/{productId}/rate',
    summary='Оставление рейтинга для товара от активного пользоваля',
    response_model=ResponseSuccess,
    responses={} # TODO: you have been voted yet
)
async def set_rate_to_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    # TODO: db and userSession and bodyScheme here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


@router.post(
    path='/{productId}/buy',
    summary='Оформление заказа выбранного товара',
    response_model=ResponseSuccess,
    responses={} # TODO: amount > remaind
)
async def buy_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    # TODO: db and userSession and bodyScheme here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")