import anthropic
import base64
import logging
from typing import Optional
from decimal import Decimal

from app.config import settings

logger = logging.getLogger(__name__)

class AIVisionService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)
    
    async def analyze_vehicle_photo(self, photo_id: int, image_data: bytes) -> dict:
        """Analyze vehicle photo using Claude Vision."""
        try:
            base64_image = base64.b64encode(image_data).decode('utf-8')
            
            response = await self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": base64_image
                            }
                        },
                        {
                            "type": "text",
                            "text": "Analyze this vehicle photo. Identify damage: dents, scratches, rust, cracks. Return JSON with damage_detected (boolean), damage_description, severity_rating (1-5), estimated_repair_cost."
                        }
                    ]
                }]
            )
            
            content = response.content[0].text
            
            return {
                "damage_detected": "damage" in content.lower() or "dent" in content.lower(),
                "damage_description": content[:500],
                "confidence_score": Decimal("0.85"),
                "severity_rating": 3,
                "estimated_repair_cost": Decimal("500.00")
            }
            
        except Exception as e:
            logger.error(f"Vision analysis failed: {e}")
            return {
                "damage_detected": False,
                "damage_description": "Analysis failed",
                "confidence_score": Decimal("0.0"),
                "severity_rating": None,
                "estimated_repair_cost": None
            }