from pydantic import BaseModel, Field
from typing import Optional, Dict
from decimal import Decimal

class PhotoUploadRequest(BaseModel):
    quote_id: str
    photo_type: str = Field(..., pattern="^(front|rear|driver_side|passenger_side|interior|engine|video_walkaround)$")
    content_type: str = "image/jpeg"

class PhotoAnalysisResult(BaseModel):
    damage_detected: bool
    damage_description: Optional[str] = None
    confidence_score: Decimal
    severity_rating: Optional[int] = Field(None, ge=1, le=5)
    estimated_repair_cost: Optional[Decimal] = None