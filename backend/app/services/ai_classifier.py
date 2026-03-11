import anthropic
import json
import logging
from typing import Dict
from decimal import Decimal

from app.config import settings
from app.schemas.quote import QuoteRequest

logger = logging.getLogger(__name__)

class AIClassifier:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)
    
    async def classify_vehicle(self, request: QuoteRequest) -> Dict:
        # 1. Rules first (free)
        if request.mileage > 200000 and not request.drivable:
            return {
                'classification': 'junk',
                'confidence': Decimal('0.95'),
                'reasoning': 'High mileage + non-drivable'
            }
        
        # 2. AI for edge cases
        prompt = f"""
        Vehicle: {request.year} {request.make} {request.model}
        Miles: {request.mileage}, Condition: {request.condition_rating}
        Drivable: {request.drivable}, Title: {request.title_status}
        
        Classify as 'junk' or 'auction'. Return JSON with classification, confidence (0-1), reasoning.
        """
        
        try:
            response = await self.client.messages.create(
                model=settings.CLAUDE_MODEL,
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = json.loads(response.content[0].text)
            return {
                'classification': result['classification'],
                'confidence': Decimal(str(result['confidence'])),
                'reasoning': result['reasoning']
            }
            
        except Exception as e:
            logger.error(f"AI classification failed: {e}")
            return self._rules_fallback(request)
    
    def _rules_fallback(self, request: QuoteRequest) -> Dict:
        score = 0
        age = 2024 - request.year
        
        if age > 15: score -= 2
        if request.mileage > 200000: score -= 2
        if request.title_status in ['salvage', 'junk']: score -= 3
        if not request.drivable: score -= 3
        
        classification = 'auction' if score >= 0 else 'junk'
        
        return {
            'classification': classification,
            'confidence': Decimal('0.70'),
            'reasoning': f'Rules-based fallback, score: {score}'
        }