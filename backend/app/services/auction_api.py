import httpx
import logging
from typing import List, Dict, Optional
from decimal import Decimal

logger = logging.getLogger(__name__)

class AuctionAPIService:
    def __init__(self):
        self.base_url = "https://api.auctiondata.com/v1"
        self.api_key = ""  # Set from config
    
    async def get_historical_sales(
        self,
        year: int,
        make: str,
        model: str,
        condition: Optional[str] = None
    ) -> List[Dict]:
        """Get historical auction sales for comparable vehicles."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/sales/historical",
                    params={
                        "year": year,
                        "make": make,
                        "model": model,
                        "condition": condition
                    },
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    return response.json().get('sales', [])
                return []
                
        except Exception as e:
            logger.error(f"Auction API error: {e}")
            return []
    
    async def calculate_market_value(
        self,
        year: int,
        make: str,
        model: str,
        mileage: int
    ) -> Optional[Decimal]:
        """Calculate market value based on auction comps."""
        sales = await self.get_historical_sales(year, make, model)
        
        if not sales:
            return None
        
        prices = [Decimal(str(sale['price'])) for sale in sales if 'price' in sale]
        if not prices:
            return None
        
        return sum(prices) / len(prices)