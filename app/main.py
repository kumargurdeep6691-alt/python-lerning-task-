from fastapi import FastAPI

from app.database import Base, engine
from app.routes.tasks import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task API",
    description="A small Task Management API",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Task API is running"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }