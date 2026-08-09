import os
import requests

from app.core.config import (
    COPERNICUS_CLIENT_ID,
    COPERNICUS_CLIENT_SECRET
)
def get_access_token():
    url = (
        "https://identity.dataspace.copernicus.eu"
        "/auth/realms/CDSE/protocol/openid-connect/token"
    )
    payload = {
        "grant_type": "client_credentials",
        "client_id": COPERNICUS_CLIENT_ID,
        "client_secret": COPERNICUS_CLIENT_SECRET
    }
    response = requests.post(
        url, 
        data = payload
    )
    token_data = response.json()
    return token_data.get("access_token")

def get_satellite_image_url(lat, lon):

    token = get_access_token()

    print("Token received:", token[:20])

    bbox = [
        lon - 0.01,
        lat - 0.01,
        lon + 0.01,
        lat + 0.01
    ]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "input": {
            "bounds": {
                "bbox": bbox
            },
            "data": [
                {
                "type": "sentinel-2-l2a"
                }
            ]
        },
        "output": {
            "width": 512,
            "height": 512
        },
        "evalscript": """
            //VERSION=3
            function setup() {
                return {
                    input: ["B04", "B03", "B02"],
                    output: { bands: 3 }
                };
            }
            function evaluatePixel(sample) {
                return [
                    sample.B04,
                    sample.B03,
                    sample.B02
                ];
            }
        """
    }

    print(payload["evalscript"])

    print("Payload:")
    print(payload)

    print("Headers:")
    print(headers)

    print("BBox:", bbox)

    response = requests.post(
        "https://sh.dataspace.copernicus.eu/api/v1/process",
        headers = headers,
        json = payload
    )

    with open("../data/images/latest.png", "wb") as f:
        f.write(response.content)

    print("Status:", response.status_code)
    try:
        print(response.json())
    except:
        print("Status:", response.status_code)
        print("Content Type:", response.headers.get("Content-Type"))

    return {
        "bbox": bbox,
        "image_url": "../data/images/latest.png"
    }