# TerrainTel

## Offline-First Geospatial Intelligence Platform

TerrainTel is an Offline-First Geospatial Intelligence Platform designed to acquire satellite imagery, perform automated terrain analysis, and generate intelligence summaries for strategic monitoring applications.

This project was developed as part of the Def-Space Summer Internship and serves as a proof-of-concept for future defence, disaster management, and geospatial intelligence systems.

---

## Project Overview

TerrainTel enables users to:

- Select any location on an interactive map
- Retrieve Sentinel-2 satellite imagery
- Perform automated image analysis
- Generate intelligence reports
- Assess potential areas of interest through terrain features

The platform demonstrates an end-to-end geospatial intelligence workflow from location selection to intelligence generation.

---

## Key Features

### Location Selection
- Interactive map interface
- Coordinate capture
- Reverse geocoding to obtain human-readable addresses

### Satellite Imagery Acquisition
- Integration with Sentinel-2 satellite imagery
- Automated image retrieval
- Latest available satellite image processing

### Image Analysis
- Brightness analysis
- Edge density calculation
- Terrain feature extraction
- Basic infrastructure pattern detection

### Intelligence Generation
- Risk assessment
- Confidence scoring
- Observation generation
- Recommendation generation

### Modular Architecture
- React Frontend
- FastAPI Backend
- Satellite Service Layer
- Intelligence Engine
- Image Processing Module

---

## System Architecture

```text
User
  │
  ▼
React Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Satellite Service
  │
  ▼
Sentinel-2 Imagery
  │
  ▼
Image Analysis Engine
  │
  ▼
Intelligence Generator
  │
  ▼
Terrain Intelligence Report
```

---

## Technology Stack

### Frontend
- React
- Vite
- CSS

### Backend
- FastAPI
- Python

### Geospatial Services
- Sentinel Hub API
- OpenStreetMap Reverse Geocoding

### Image Processing
- OpenCV
- NumPy

### Development Tools
- VS Code
- Git
- GitHub

---

## Project Structure

```text
TerrainTel/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── data/
│   ├── images/
│   ├── raw/
│   └── processed/
│
├── README.md
└── LICENSE
```

---

## Sample Workflow

1. User selects a location on the map.
2. Coordinates are sent to the backend.
3. Sentinel-2 imagery is retrieved.
4. Image processing extracts terrain metrics.
5. Intelligence engine evaluates observations.
6. A terrain intelligence report is generated.

---

## Example Intelligence Report

**Location:** Nashik, Maharashtra, India

**Satellite Source:** Sentinel-2

**Cloud Coverage:** 12%

**Risk Level:** Medium

**Confidence:** 75%

**Observation:** Large bright surface detected.

**Recommendation:** Review area manually.

---

## Screenshots

### Location Selection

Insert screenshot here.

---

### Satellite Imagery Retrieval

Insert screenshot here.

---

### Generated Intelligence Report

Insert screenshot here.

---

## Current Limitations

- Rule-based intelligence engine
- Limited terrain analysis metrics
- No SAR imagery integration
- No object detection models
- Requires internet connectivity for imagery acquisition

---

## Future Scope

- Offline map support
- SAR (Synthetic Aperture Radar) integration
- Multi-sensor data fusion
- Object detection using AI models
- Explainable geospatial reasoning
- Border monitoring applications
- Disaster response intelligence
- Defence-grade situational awareness platform

---

## Expected Impact

TerrainTel demonstrates how satellite imagery can be automatically processed and transformed into actionable intelligence. The platform provides a foundation for future geospatial intelligence systems that can support defence, disaster management, infrastructure monitoring, and strategic decision-making.

---

## Author

**Gauri Dharankar**

Final Year Information Technology Engineering Student

Def-Space Summer Internship Project

---
## Copyright

© 2026 Gauri Dharankar. All rights reserved.

This repository is provided for academic and demonstration purposes.
