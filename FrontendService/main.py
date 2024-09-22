from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import close_database, create_tables, ping_database
from app.routes.user_route import user_router
from app.routes.book_route import book_router
from app.routes.borrow_book_route import borrow_book_router
from app.core.dependencies import rabbitmq_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await ping_database()
    await create_tables()
    await rabbitmq_client.connect()
    await rabbitmq_client.start_consume(["add_book", "delete_book"])
    yield
    # Close DB
    await close_database()
    await rabbitmq_client.close()

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

app.include_router(user_router)
app.include_router(book_router)
app.include_router(borrow_book_router)