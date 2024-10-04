from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

from .config import env_vars


class Database:
    def __init__(self):
        self.engine = create_async_engine(env_vars.DATABASE_URL, echo=True, future=True)
        self.Base = declarative_base()
        self.async_session_generator = sessionmaker(self.engine, class_=AsyncSession)
        
    # create database if not exist
    async def create_database(self, database_name: str):
        superuser_database_url = env_vars.SUPERUSER_DATABASE_URL
        superuser_engine = create_async_engine(superuser_database_url, echo=True, future=True, isolation_level="AUTOCOMMIT")
        try:
            async with superuser_engine.connect() as conn:
                result = await conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'"))
                db_exists = result.scalar()
                if not db_exists:
                    await conn.execute(text(f"CREATE DATABASE \"{database_name}\""))
                    print(f"Database '{database_name}' created successfully")
                else:
                    print(f"Database '{database_name}' already exists")
        except ProgrammingError as e:
            print(f"Error creating database: {e}")
        finally:
            await superuser_engine.dispose()

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        async_session = self.async_session_generator()
        try:
            async with async_session() as session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    # Ping database to test connection
    async def ping_database(self):
        try:
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            print("Successfully connected to the Database database!")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    async def close_database(self):
        await self.engine.dispose()
        print("Database connection closed!")

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)
        print("Database tables created successfully")


database = Database()

async def setup_database():
    await database.create_database(env_vars.DATABASE_NAME)
    await database.ping_database()
    await database.create_tables()
