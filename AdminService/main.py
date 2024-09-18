import asyncio
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import close_mongo_db_connection, connect_to_mongo_db
from app.routes.user_route import user_router
from app.routes.book_route import book_router

# logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # PInd DB
    await connect_to_mongo_db()
    yield
    # Close DB
    await close_mongo_db_connection()

app = FastAPI(
    lifespan=lifespan,
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

# Index health check
@app.get('/')
def index():
    return {"message": "BookNest Admin API"}


app.include_router(user_router)
app.include_router(book_router)