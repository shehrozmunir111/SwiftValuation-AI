from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.database import get_db
from app.schemas.quote import QuoteRequest, QuoteResponse
from app.services.pricing_engine import PricingEngine
from app.services.ai_classifier import AIClassifier
from app.models.quote import Quote

router = APIRouter()

@router.post("/calculate", response_model=QuoteResponse)
async def calculate_quote(
    request: QuoteRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    # 1. AI Classification
    classifier = AIClassifier()
    classification = await classifier.classify_vehicle(request)
    
    # 2. Pricing Engine
    engine = PricingEngine(db)
    pricing = engine.find_best_price(request)
    
    # 3. Create quote
    quote = Quote(
        vin=request.vin,
        year=request.year,
        make=request.make,
        model=request.model,
        mileage=request.mileage,
        zip_code=request.zip_code,
        classification=classification['classification'],
        classification_confidence=classification['confidence'],
        partner_id=pricing['partner_id'],
        partner_price=pricing['partner_price'],
        spread_amount=pricing['spread_amount'],
        final_offer=pricing['final_offer'],
        offer_valid_until=datetime.now() + timedelta(hours=24),
        ai_classified=True,
        needs_human_review=classification['confidence'] < 0.7
    )
    
    db.add(quote)
    db.commit()
    db.refresh(quote)
    
    return QuoteResponse(
        quote_id=quote.quote_id,
        classification=classification['classification'],
        confidence=classification['confidence'],
        offer_amount=pricing['final_offer'],
        offer_valid_until=quote.offer_valid_until,
        partner_id=pricing['partner_id'],
        calculation_method=pricing['calculation_method'],
        query_time_ms=pricing['query_time_ms'],
        needs_human_review=quote.needs_human_review
    )