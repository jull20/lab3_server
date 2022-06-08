from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from core.settings import Base


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), index=True)
    value = Column(Float, nullable=False)

    user = relationship('User', back_populates='rates')
    product = relationship('Product', back_populates='rates')