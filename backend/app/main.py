from fastapi import FastAPI  # type: ignore[import-not-found]

from app.routes import email_routes

app = FastAPI()

app.include_router(email_routes.router)


@app.get("/")
def home():

    return {
        "message": "AI Email Reply Generator API is running 🚀"
    }