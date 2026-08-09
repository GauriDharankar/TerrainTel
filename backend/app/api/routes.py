from fastapi import APIRouter

from app.services.satellite_service import analyze_location

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    lat = data.get("lat")
    lon = data.get("lon")
    return analyze_location(lat, lon)