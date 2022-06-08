from fastapi import HTTPException, status
from sqlalchemy.orm import Session


async def get_all_products_service(db: Session):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")


async def get_product_by_id_service(db: Session, productId: int):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")