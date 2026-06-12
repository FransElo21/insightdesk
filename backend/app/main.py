from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.api.complaint_router import (
    router as complaint_router
)

from app.api.dashboard_router import (
    router as dashboard_router
)

from app.api.insight_router import (
    router as insight_router
)

app = FastAPI(
    title="InsightDesk API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    complaint_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    insight_router
)


@app.get("/")
def root():

    return {
        "message": "InsightDesk API Running"
    }