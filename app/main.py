from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Medical AI Agent")
app.include_router(router, prefix="/api")