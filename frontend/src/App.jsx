import { useState } from 'react'
import { MapContainer, TileLayer, useMapEvents, Marker } from 'react-leaflet'
//import axios from "axios"

function LocationMarker({ position, setPosition, analyzeLocation })
{
  useMapEvents ({
    click(e){
      setPosition(e.latlng)

      analyzeLocation(
        e.latlng.lat,
        e.latlng.lng
      )
    },
  })

  return position ? <Marker position = {position} /> : null
}

function App()
{
  const [position, setPosition] = useState(null)
  const [report, setReport] = useState(null)
  const [analysis, setAnalysis] = useState(null)

  async function analyzeLocation(lat, lon)
  {
    try
    {
      const response = await fetch (
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: 
          {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            lat: lat,
            lon: lon
          })
        }
      )

      const data = await response.json()
      console.log(data)
      setReport(data)
    }
    catch(error)
    {
      console.error(error)
    }
  }
  return (
    <div style = {{ padding: '20px' }}>
      <h1>TerrainTel</h1>
      <p>Offline-First Geospatial Intelligence Platform</p>

      <MapContainer
        center = {[20.5937, 78.96929]}
        zoom = {5}
        style = {{ height: '500px', width: '100%' }}
        >
          <TileLayer
            attribution = "&copy; OpenStreetMap contributors"
            url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            <LocationMarker 
              position = {position} 
              setPosition = {setPosition} 
              analyzeLocation = {analyzeLocation}
              />
        </MapContainer>

        {position && (
          <div style = {{ marginTop: '20px' }}>
            <h3>Selected Location</h3>
            <p>Latitude: {position.lat.toFixed(6)}</p>
            <p>Longitude: {position.lng.toFixed(6)}</p>
          </div>)}

          <div
            style = {{
              border: "1px solid gray",
              padding: "10px",
              marginBottom: "20px"
            }}
          >
              <h3>Satellite Preview</h3>
              <img
                src = {`http://127.0.0.1:8000/images/latest.png`}
                alt = "Satellite Preview"
                style = {{
                  width: "100%"
                }}
              />
            </div>

          {report && (
            <div>
              <h3> TerrainTel Analysis</h3>
              <p>Location: {report.location_name}</p>
              <h4>Satellite Metadata</h4>
              <p>Source: {report.satellite_source}</p>
              <p>Date: {report.date}</p>
              <p>Cloud Coverage: {report.cloud_coverage}</p>
              <h4>Image Metrics</h4>
              <p>Brightness: {report.brightness}</p>
              <p>Edge Density: {report.edge_density}</p>
              <p>Risk: {report.risk_level}</p>
              <p>Confidence: {report.confidence}</p>
              <p>Observation: {report.observation}</p>
              <p>Recommendation: {report.recommendation}</p>
            </div>
          )}
    </div>
  )
}

export default App