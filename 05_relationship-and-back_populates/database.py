# database.py — Async engine and session factory
# 日本語訳：非同期エンジンとセッションファクトリの設定
#
# Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Connection URL for local Docker PostgreSQL
# 日本語訳：Docker上のPostgreSQL接続URL
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground"

# Create async engine with echo=True to observe generated SQL
# 日本語訳：echo=True で発行されるSQLをコンソールに出力する（面接でSQLを説明できるようにするため）
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # IMPORTANT: always observe generated SQL during learning
    # 日本語訳：重要：学習中は必ずSQLを観察すること
)

# Session factory — expire_on_commit=False prevents lazy loading after commit
# 日本語訳：expire_on_commit=False でコミット後のレイジーロードを防ぐ（async必須設定）
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
