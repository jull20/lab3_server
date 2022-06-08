from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

import datetime

from core.settings import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), index=True)
    amount = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')

