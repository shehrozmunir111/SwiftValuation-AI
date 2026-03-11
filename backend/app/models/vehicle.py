from sqlalchemy import Column, Integer, String, Numeric, Index
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import TimestampMixin

class Vehicle(Base, TimestampMixin):
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    make = Column(String(100), nullable=False, index=True)
    model = Column(String(100), nullable=False, index=True)
    trim = Column(String(100))
    body_type = Column(String(50))
    weight_kg = Column(Numeric(8, 2))
    
    pricing_rules = relationship("PricingRule", back_populates="vehicle")
    quotes = relationship("Quote", back_populates="vehicle_ref")
    
    __table_args__ = (
        Index('idx_vehicles_ymm', 'year', 'make', 'model'),
    )