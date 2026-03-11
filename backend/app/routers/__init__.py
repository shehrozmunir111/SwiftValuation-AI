from app.routers.quotes import router as quotes_router
from app.routers.vehicles import router as vehicles_router
from app.routers.partners import router as partners_router
from app.routers.photos import router as photos_router

__all__ = ["quotes_router", "vehicles_router", "partners_router", "photos_router"]