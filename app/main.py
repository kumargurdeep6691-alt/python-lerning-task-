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

