import asyncio
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import close_mongo_db_connection, connect_to_mongo_db
from app.routes.user_route import user_router
from app.routes.book_route import book_router

# logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title="BookNest Admin API",
    version="1.0.0",
    description="BookNest Admin API",
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

# Start event handlers
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo_db()


# Shutdown event handlers
@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_db_connection()

# Index health check
@app.get('/')
def index():
    return {"message": "BookNest Admin API"}


app.include_router(user_router)
app.include_router(book_router)