from sqlalchemy import Column, Integer, String, Boolean, JSON, Numeric
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import TimestampMixin

class Partner(Base, TimestampMixin):
    __tablename__ = "partners"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    partner_type = Column(String(20), nullable=False)
    pricing_structure_type = Column(String(20), nullable=False)
    
    api_endpoint = Column(String(500))
    api_credentials = Column(JSON)
    
    is_active = Column(Boolean, default=True)
    priority_score = Column(Integer, default=0)
    coverage_zips = Column(JSON)
    
    default_spread_percent = Column(Numeric(5, 2), default=15.0)
    
    pricing_rules = relationship("PricingRule", back_populates="partner")
    quotes = relationship("Quote", back_populates="partner_ref")