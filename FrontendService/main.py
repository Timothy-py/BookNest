from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import close_database, ping_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ping DB
    await ping_database()
    yield
    # Close DB
    await close_database()

app = FastAPI(
    lifespan=lifespan,
    title="BookNest Frontend API",
    version="1.0.0",
    description="BookNest Frontend API",
    debug=True,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"message": "BookNest Frontend API"}