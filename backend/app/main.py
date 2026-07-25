"""FastAPI Application Entry Point"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.api.v1 import auth, vehicles, users, admin
from app.middleware.error_handler import error_handler_middleware
from app.middleware.logging import setup_logging
from app.database.connection import engine, Base

# Setup logging
logger = setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle manager"""
    # Startup
    logger.info("Application starting...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")
    
    yield
    
    # Shutdown
    logger.info("Application shutting down...")


# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# Add Trusted Host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# Add error handler middleware
app.middleware("http")(error_handler_middleware)


# Include routers
app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Authentication"],
)

app.include_router(
    vehicles.router,
    prefix="/api/v1/vehicles",
    tags=["Vehicles"],
)

app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["Users"],
)

app.include_router(
    admin.router,
    prefix="/api/v1/admin",
    tags=["Admin"],
)


# Health check endpoints
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/health/db", tags=["Health"])
async def health_check_db():
    """Database health check"""
    try:
        from app.database.connection import SessionLocal
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        return {"status": "healthy", "component": "database"}
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "component": "database", "error": str(e)}
        )


@app.get("/health/cache", tags=["Health"])
async def health_check_cache():
    """Cache health check"""
    try:
        from app.services.cache_service import cache_service
        await cache_service.ping()
        return {"status": "healthy", "component": "cache"}
    except Exception as e:
        logger.error(f"Cache health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "component": "cache", "error": str(e)}
        )


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "name": settings.API_TITLE,
        "description": settings.API_DESCRIPTION,
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT,
        reload=settings.FASTAPI_DEBUG,
        log_level="info",
    )
