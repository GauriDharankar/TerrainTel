def generate_intelligence(cloud_coverage, brightness, edge_density):

    risk = "Low"
    confidence = "75%"
    observation = "No significant activity detected."
    recommendation = "Routine monitoring."

    if edge_density > 0.20:
        risk = "High"
        confidence = "90%"
        observation = "Highly structured terrain detected."
        recommendation = "Further investigation recommended."

    elif edge_density > 0.15:
        risk = "Medium"
        confidence = "85%"
        observation = "Potential man-made structures detected."
        recommendation = "Review area manually."

    elif edge_density > 0.10:
        risk = "Medium"
        observation = "Dense infrastructure patterns detected."
        recommendation = "Review area manually."
    
    elif cloud_coverage > 20:
        risk = "Medium"
        confidence = "60%"
        observation = "Cloud cover may obscure ground activity."
        recommendation = "Acquire additional imagery."

    elif brightness > 180:
        risk = "Medium"
        observation = "Large bright surface detected."
        recommendation = "Review area manually."

    return {
        "brightness": round(brightness, 2),
        "edge_density": round(edge_density, 4),
        "risk_level": risk,
        "confidence": confidence,
        "observation": observation,
        "recommendation": recommendation
    }