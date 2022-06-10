from datetime import date, datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError

from models.product import Product
from models.rate import Rate
from models.order import Order
from v1.user.schema import UserSession
from v1.products.schema import ResponseProduct, ResponseSuccess


async def get_all_products_service(db: Session):
    products: list[Product] = db.query(Product.id, Product.name, Product.photo, Product.price, Product.start_amount, func.sum(Order.amount).label('ordered'), func.avg(Rate.value).label('avg_rate')).join(Order, Order.product_id == Product.id, isouter=True).join(Rate, Rate.product_id == Product.id, isouter=True).group_by(Product.id).all()
    
    return list(map(
        lambda x: ResponseProduct(
            id=x.id,
            name=x.name, 
            photo=x.photo, 
            price=x.price,
            remaind=x.start_amount - (x.ordered if x.ordered else 0),
            rate=x.avg_rate
        ),
        products
    ))


async def get_product_by_id_service(db: Session, productId: int):
    try:
        product: Product = db.query(Product.id, Product.name, Product.photo, Product.price, Product.start_amount, func.sum(Order.amount).label('ordered'), func.avg(Rate.value).label('avg_rate')).filter(Product.id == productId).join(Order, Order.product_id == Product.id, isouter=True).join(Rate, Rate.product_id == Product.id, isouter=True).group_by(Product.id).one()
        return ResponseProduct(
            id=product.id,
            name=product.name,
            photo=product.photo,
            price=product.price,
            remaind=product.start_amount - (product.ordered if product.ordered else 0),
            rate=product.avg_rate
        )
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with same id not found")


async def post_product_rate_by_id(db: Session, user: UserSession, productId: int, rate_value: float):
    try:
        rate = Rate(user_id=user.id, product_id=productId, value=rate_value)
        db.add(rate)
        db.commit()
    except IntegrityError as e:
        if 'psycopg2.errors.UniqueViolation' in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have been voted yet")
        elif 'psycopg2.errors.ForeignKeyViolation' in str(e):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with same id not found")

    return ResponseSuccess()


async def post_product_buy_bi_id(db: Session, user: UserSession, productId: int, amount: int):
    try:
        product: Product = db.query(Product.id, Product.start_amount, func.sum(Order.amount).label('ordered')).filter(Product.id == productId).join(Order, Order.product_id == Product.id, isouter=True).join(Rate, Rate.product_id == Product.id, isouter=True).group_by(Product.id).one()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with same id not found")

    remaind = product.start_amount - (product.ordered if product.ordered else 0)

    if amount > remaind:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Amount greater than remaind at store')
    
    try:
        order = Order(user_id=user.id, product_id=product.id, amount=amount, date=datetime.now())
        db.add(order)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='Something wrong')

    return ResponseSuccess()