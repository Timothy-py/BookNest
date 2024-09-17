import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.user_route import user_router

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


# Index health check
@app.get('/')
def index():
    return {"message": "BookNest Admin API"}


app.include_router(user_router)