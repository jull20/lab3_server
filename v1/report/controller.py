import uuid
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from v1.user.schema import UserSession
from models.order import Order
from models.user import User
from models.product import Product
import csv


async def make_orders_report(db: Session, user: UserSession):
    data: list[Order] = db.query(Order).join(Product).join(User).all()

    file_path = f'public/tmp/{uuid.uuid4()}.csv'
    with open(file_path, 'w', newline='') as csvfile:
        field_names = ['user_id', 'username', 'email', 'name', 'product_id', 'product_name', 'price', 'amount', 'total', 'bought_at']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for order in data:
            writer.writerow({
                "user_id": order.user_id,
                'username': order.user.username,
                'email': order.user.email,
                'product_id': order.product_id,
                'product_name': order.product.name,
                'price': order.product.price,
                'amount': order.amount,
                'total': order.product.price * order.amount,
                'bought_at': order.date
            })

    return FileResponse(file_path, filename='report.csv', media_type='text/csv')