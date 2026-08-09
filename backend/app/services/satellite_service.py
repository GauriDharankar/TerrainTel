import requests

from app.services.intelligence import generate_intelligence
from datetime import date
from app.services.copernicus_service import get_satellite_image_url
from app.models.imagery import analyze_image

def get_location_name(lat, lon):
    url = (f"https://nominatim.openstreetmap.org/reverse"
           f"?lat={lat}"
           f"&lon={lon}"
           f"&format=json"
           )
    headers = {"User-Agent": "TerrainTel"}
    response = requests.get(
        url,
        headers = headers
    )
    data = response.json()
    return data.get(
        "display_name",
        "Unknown Location"
    )

def analyze_location(lat, lon):
    location_name = get_location_name(lat, lon)
    cloud_coverage = 12
    satellite_source = "Sentinel-2"
    image_metrics = analyze_image("../data/images/latest.png")
    intelligence = generate_intelligence(cloud_coverage, image_metrics["brightness"], image_metrics["edge_density"])
    satellite_data = get_satellite_image_url(lat, lon)
    result = {
        "location_name": location_name,
        "satellite_source": satellite_source,
        "date": str(date.today()),
        "cloud_coverage": f"{cloud_coverage}%",
        "satellite_data": satellite_data,
        **intelligence
    }

    print(result)

    return result

    return {
        "location_name": location_name,  
        "satellite_source": satellite_source,
        "date": str(date.today()),
        "cloud_coverage": f"{cloud_coverage}%",
        "satellite_data": satellite_data,  
        **intelligence
    }

