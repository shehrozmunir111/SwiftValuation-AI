from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean, Date, Index
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import TimestampMixin

class PricingRule(Base, TimestampMixin):
    __tablename__ = "pricing_rules"
    
    id = Column(Integer, primary_key=True, index=True)
    partner_id = Column(Integer, ForeignKey("partners.id"), nullable=False)
    rule_type = Column(String(20), nullable=False)
    
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicle_category = Column(String(50))
    
    zip_code = Column(String(10))
    zip_prefix = Column(String(5))
    
    base_price = Column(Numeric(10, 2))
    category_price = Column(Numeric(10, 2))
    specific_price = Column(Numeric(10, 2))
    price_per_ton = Column(Numeric(10, 2))
    
    condition_min = Column(String(20))
    condition_max = Column(String(20))
    adjustment_percent = Column(Numeric(5, 2))
    
    buyer_spread_percent = Column(Numeric(5, 2))
    min_margin = Column(Numeric(10, 2))
    max_margin = Column(Numeric(10, 2))
    
    valid_from = Column(Date)
    valid_until = Column(Date)
    is_active = Column(Boolean, default=True)
    
    partner = relationship("Partner", back_populates="pricing_rules")
    vehicle = relationship("Vehicle", back_populates="pricing_rules")
    
    __table_args__ = (
        Index('idx_pricing_partner', 'partner_id'),
        Index('idx_pricing_lookup', 'partner_id', 'vehicle_id', 'is_active'),
    )