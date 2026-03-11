from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.database import get_db

security = HTTPBearer(auto_error=False)

async def get_current_user(credentials=Depends(security), db: Session = Depends(get_db)):
    # Simplified auth
    return {"user_id": "anonymous"}