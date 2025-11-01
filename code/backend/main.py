"""Application entry point"""

import os
import uvicorn
from app.main import app

if __name__ == "__main__":
    reload = os.getenv("RELOAD", "false").lower() == "true"
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=reload
    )
