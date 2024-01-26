from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

from database.config import settings

Base: DeclarativeBase = declarative_base()
async_engine = create_async_engine(settings.URL)
session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
