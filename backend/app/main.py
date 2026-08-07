from fastapi import FastAPI

app = FastAPI(
    title = "TerrainTel API",
    description = "Offline-First Geospatial Intelligence Platform",
    version = "0.1.0"
)

@app.get("/") #decorator
def root():
    return {"message": "TerrainTel API is running."}

@app.get("/health")
def health():
    return {"status": "healthy"}