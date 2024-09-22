from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import text

from .config import env_vars


engine = create_async_engine(env_vars.DATABASE_URL, echo=True, future=True)

Base = declarative_base()

def async_session_generator():
    return sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_session() -> AsyncSession:
    async_session = async_session_generator()
    try: 
        async with async_session() as session:
            yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally: 
        await session.close()
        

# Ping database to test connection
async def ping_database():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("Successfully connected to the Database database!")
    except Exception as e:
        print(f"Error connecting to database: {e}")

async def close_database():
    await engine.dispose()
    print("Database connection closed!")
    

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully")