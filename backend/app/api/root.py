from fastapi import APIRouter

router = APIRouter()

@router.get("/") #decorator
def root():
    return {"message": "TerrainTel API is running."}