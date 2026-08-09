from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.root import router as root_router
from app.api.health import router as health_router
from app.api.routes import router as analysis_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title = "TerrainTel API",
    description = "Offline-First Geospatial Intelligence Platform",
    version = "0.1.0"
)

app.mount(
    "/images",
    StaticFiles(directory="../data/images"),
    name = "images"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173"
    ],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(analysis_router)