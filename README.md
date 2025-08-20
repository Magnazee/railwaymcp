# MCP Server with HTTP Streaming - Railway Deployment

This project demonstrates deploying a Model Context Protocol (MCP) server with HTTP streaming support to Railway. The server uses the modern **Streamable HTTP transport** which provides efficient bidirectional communication over a single HTTP endpoint.

## Features

- ✅ **Streamable HTTP Transport**: Modern MCP transport with full bidirectional streaming
- ✅ **HTTP Streaming**: Supports real-time communication and server-sent events
- ✅ **Multiple Tools**: Weather API, BMI calculator, and more
- ✅ **Resources & Prompts**: Dynamic greetings and question generation
- ✅ **Railway Optimized**: Configured for seamless Railway deployment

## Tools Available

1. **get_weather(city)** - Get simulated weather data for any city
2. **calculate_bmi(weight_kg, height_m)** - Calculate BMI with category classification
3. **greeting://{{name}}** - Personalized greeting resource
4. **ask_question(topic, style)** - Generate styled questions about topics

## Local Development

### Prerequisites
- Python 3.8+
- pip or uv package manager

### Setup
```bash
# Clone this repository
git clone <your-repo-url>
cd mcp-railway-server

# Install dependencies
pip install -r requirements.txt
# OR with uv
uv pip install -r requirements.txt

# Run locally
python main.py
```

The server will start on `http://localhost:8000/mcp` with Streamable HTTP transport.

### Testing the Server

You can test the server using the MCP Inspector or any MCP client that supports Streamable HTTP:

```bash
# Install MCP CLI tools (if available)
uv tool install mcp

# Test with MCP Inspector
mcp inspect http://localhost:8000/mcp
```

## Railway Deployment

### Method 1: Deploy from GitHub (Recommended)

1. **Fork this repository** to your GitHub account

2. **Create a new Railway project**:
   - Go to [Railway](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your forked repository

3. **Configure deployment**:
   - Railway will automatically detect the `railway.json` configuration
   - The app will build using Nixpacks
   - No additional environment variables needed

4. **Generate domain**:
   - Go to your service settings
   - Navigate to "Networking" tab
   - Click "Generate Domain"
   - Your MCP server will be available at: `https://your-app-name.railway.app/mcp`

### Method 2: Deploy with Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

### Method 3: Deploy with Docker

If you prefer using Docker:

```bash
# Build Docker image
docker build -t mcp-server .

# Run locally (test)
docker run -p 8000:8000 -e PORT=8000 mcp-server

# Deploy to Railway (Railway will handle this automatically if Dockerfile is present)
```

## Configuration

### Environment Variables

Railway automatically sets the `PORT` environment variable. No additional configuration is required for basic deployment.

Optional environment variables you can add:
- `MCP_SERVER_NAME`: Custom server name (default: "Railway MCP Server")
- `DEBUG`: Set to "true" for debug logging

### MCP Client Configuration

To connect an MCP client to your deployed server, use this configuration:

```json
{
  "mcpServers": {
    "railway-mcp": {
      "type": "streamable-http",
      "url": "https://your-app-name.railway.app/mcp"
    }
  }
}
```

## Architecture

This server uses:
- **FastMCP**: High-level MCP server framework
- **Streamable HTTP Transport**: Modern bidirectional communication protocol
- **Railway Platform**: Serverless deployment with automatic scaling

### Key Benefits of Streamable HTTP:
- Single endpoint for all communication (`/mcp`)
- Automatic connection upgrades to SSE when needed
- Better performance than traditional HTTP+SSE approach
- Full bidirectional communication support

## Troubleshooting

### Common Issues

1. **Port binding error locally**:
   ```bash
   # Make sure port 8000 is available
   lsof -i :8000
   ```

2. **Railway deployment fails**:
   - Check that `requirements.txt` includes `mcp>=1.8.0`
   - Ensure `railway.json` has correct start command
   - Verify Railway has access to your GitHub repository

3. **MCP client connection issues**:
   - Ensure client supports Streamable HTTP transport
   - Use correct URL format: `https://your-app.railway.app/mcp`
   - Check that Railway domain is generated and accessible

### Logs and Debugging

View Railway logs:
```bash
railway logs
```

Enable debug mode by setting environment variable:
```bash
railway variables set DEBUG=true
```

## Next Steps

1. **Add Authentication**: Implement OAuth 2.1 for secured endpoints
2. **Add Real APIs**: Replace simulated data with real weather/data APIs
3. **Database Integration**: Add persistent storage with Railway PostgreSQL
4. **Monitoring**: Set up logging and monitoring for production use

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Railway Documentation](https://docs.railway.app/)
- [Streamable HTTP Transport Spec](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)

## License

MIT License - see LICENSE file for details.
