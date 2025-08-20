"""
MCP Server with Streamable HTTP transport for Railway deployment
Based on the MCP Python SDK examples with HTTP streaming support
"""

import os
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

# Create FastMCP server with streamable HTTP support
mcp = FastMCP(
    name="Railway MCP Server",
    instructions="A demo MCP server with HTTP streaming deployed on Railway"
)

@mcp.tool()
def get_weather(city: str = "San Francisco") -> Dict[str, Any]:
    """Get current weather for a city (simulated data)."""
    # In a real implementation, you'd call a weather API
    weather_data = {
        "city": city,
        "temperature": "22°C",
        "condition": "Partly cloudy",
        "humidity": "65%",
        "wind_speed": "15 km/h",
        "timestamp": "2024-01-15T10:30:00Z"
    }
    return weather_data

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> Dict[str, Any]:
    """Calculate BMI given weight in kg and height in meters."""
    if height_m <= 0 or weight_kg <= 0:
        return {"error": "Weight and height must be positive numbers"}
    
    bmi = weight_kg / (height_m ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return {
        "bmi": round(bmi, 2),
        "category": category,
        "weight_kg": weight_kg,
        "height_m": height_m
    }

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting."""
    return f"Hello, {name}! Welcome to our Railway-deployed MCP server with HTTP streaming!"

@mcp.prompt()
def ask_question(topic: str, style: str = "friendly") -> str:
    """Generate a question prompt about a topic."""
    styles = {
        "friendly": "Could you please tell me more about",
        "formal": "I would like to inquire about",
        "casual": "What's up with",
        "academic": "Could you provide detailed information regarding"
    }
    
    prompt_start = styles.get(style, styles["friendly"])
    return f"{prompt_start} {topic}? I'm really interested to learn more!"

def main():
    """Entry point for the MCP server."""
    # Get port from environment variable (Railway sets this automatically)
    port = int(os.environ.get("PORT", 8000))
    
    print(f"Starting MCP server with Streamable HTTP transport on port {port}")
    
    # Configure server settings for Railway deployment
    mcp.settings.host = "0.0.0.0"  # Railway requires binding to 0.0.0.0
    mcp.settings.port = port
    
    # Run with streamable HTTP transport (modern approach)
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
