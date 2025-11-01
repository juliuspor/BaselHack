"""FastAPI application initialization"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app import __version__

app = FastAPI(
    title="Opinion Clustering API",
    version=__version__,
    description="API for storing and clustering political opinions using semantic similarity"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Opinion Clustering API",
        "version": __version__,
        "status": "running"
    }

