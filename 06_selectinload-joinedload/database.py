# Async engine and session factory for Chapter 06
# 日本語訳：第06章用の非同期エンジンとセッションファクトリ

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# 📋 Copy-paste OK
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground_s06"

# Create async engine with SQL echo enabled so you can observe generated SQL
# 日本語訳：生成SQLを観察できるよう echo=True でエンジンを作成する
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory — expire_on_commit=False is important for async usage
# 日本語訳：expire_on_commit=False は非同期利用時に重要（遅延ロードを防ぐ）
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
