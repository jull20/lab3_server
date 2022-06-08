from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from core.settings import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    start_amount = Column(Integer, nullable=False)

    orders = relationship('Order', back_populates='product')
    rates = relationship('Rate', back_populates='product')