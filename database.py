from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite+aiosqlite:///./test.posts"

Base = declarative_base()


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    class_=AsyncSession
)


async def get_db() -> AsyncSession:
    async with SessionLocal(bind=engine) as session:
        yield session
