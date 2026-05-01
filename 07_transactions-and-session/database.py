# database.py - Async engine and session factory for Chapter 07
# 非同期エンジンとセッションファクトリの設定
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# Connection URL for the dedicated DB for this unit
# この単元専用のDB接続URL
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground_s07"

# Create async engine with echo=True to observe generated SQL
# echo=True で発行SQLをターミナルで確認できる
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory: expire_on_commit=False is recommended for async
# 非同期では expire_on_commit=False が推奨
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
