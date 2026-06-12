from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.database.base import Base
from app.database.connection import SessionLocal, engine
from app.models.complaint_model import Complaint
from app.models.insight_model import Insight

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


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        complaint_count = db.query(Complaint).count()
        if complaint_count == 0:
            db.add_all([
                Complaint(
                    title="Wi-Fi di gedung A sering mati",
                    description="Sinyal Wi-Fi sering hilang saat jam sibuk.",
                    location="Gedung A",
                    category="Jaringan",
                    sentiment="Negatif",
                ),
                Complaint(
                    title="Nilai mata kuliah belum keluar",
                    description="Mahasiswa belum menerima nilai untuk tugas akhir.",
                    location="Akademik",
                    category="Akademik",
                    sentiment="Netral",
                ),
                Complaint(
                    title="Kantin tutup terlalu cepat",
                    description="Kantin sering tutup sebelum jam makan siang selesai.",
                    location="Kantin",
                    category="Fasilitas",
                    sentiment="Negatif",
                ),
            ])

        insight_count = db.query(Insight).count()
        if insight_count == 0:
            db.add(
                Insight(
                    content="Demo insight: mayoritas pengaduan berkaitan dengan jaringan dan fasilitas kampus. Perlu evaluasi layanan Wi-Fi dan jam operasional kantin."
                )
            )

        db.commit()
    finally:
        db.close()

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