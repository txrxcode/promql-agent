from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.sre import router as sre_router

app = FastAPI(
    title="promql-agent API",
    description="CLI-first agent for Prometheus, Loki, and Grafana",
    version="1.0.0"
)

# Add CORS middleware - Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    """Root endpoint for API health check"""
    return {
        "message": (
            "promql-agent API is running"
        ),
        "status": "healthy",
        "version": "1.0.0",
        "documentation": "/docs",
        "services": [
            "SRE Agent"
        ]
    }

app.include_router(sre_router)
