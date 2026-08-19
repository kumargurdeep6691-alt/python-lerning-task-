from fastapi import FastAPI

from app.database import Base, engine
from app.routes.tasks import router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task API",
    description="A small Task Management API",
    version="1.0.0"
)


# Include task routes
app.include_router(router)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Task API is running"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# API information
@app.get("/info")
def api_info():
    return {
        "name": "Task API",
        "version": "1.0.0",
        "description": "A small Task Management API",
        "status": "running"
    }


# API status
@app.get("/status")
def api_status():
    return {
        "api": "online",
        "database": "connected"
    }


# Welcome endpoint
@app.get("/welcome")
def welcome():
    return {
        "message": "Welcome to the Task Management API!",
        "docs": "/docs"
    }

# Version endpoint
@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "api": "Task API"
    }

@app.get("/database-status")
def database_status():
    return {
        "database": "connected",
        "status": "healthy"
    }