from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.product import Product
from models.rate import Rate
from models.order import Order
from v1.products.schema import ResponseProduct


async def get_all_products_service(db: Session):
    products: list[Product] = db.query(Product.id, Product.name, Product.photo, Product.price, Product.start_amount, func.sum(Order.amount), func.avg(Rate.value)).join(Order, Order.product_id == Product.id, isouter=True).join(Rate, Rate.product_id == Product.id, isouter=True).group_by(Product.id).all()
    
    return list(map(
        lambda x: ResponseProduct(
            id=x.id,
            name=x.name, 
            photo=x.photo, 
            price=x.price,
            remaind=x.start_amount - (x[5] if x[5] else 0),
            rate=x[6]
        ),
        products
    ))


async def get_product_by_id_service(db: Session, productId: int):
    try:
        product: Product = db.query(Product.id, Product.name, Product.photo, Product.price, Product.start_amount, func.sum(Order.amount), func.avg(Rate.value)).filter(Product.id == productId).join(Order, Order.product_id == Product.id, isouter=True).join(Rate, Rate.product_id == Product.id, isouter=True).group_by(Product.id).one()
        return ResponseProduct(
            id=product.id,
            name=product.name,
            photo=product.photo,
            price=product.price,
            remaind=product.start_amount - (product[5] if product[5] else 0),
            rate=product[6]
        )
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with same id not found")