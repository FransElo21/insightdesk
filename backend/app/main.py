from fastapi import FastAPI

app = FastAPI(
    title="InsightDesk API"
)

@app.get("/")
def root():
    return {
        "message": "InsightDesk API Running"
    }