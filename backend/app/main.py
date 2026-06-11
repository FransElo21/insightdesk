from fastapi import FastAPI

from app.api.complaint_router import (
    router as complaint_router
)

app = FastAPI(
    title="InsightDesk API"
)

app.include_router(
    complaint_router
)


@app.get("/")
def root():

    return {
        "message": "InsightDesk API Running"
    }