# Async engine and session factory for Chapter A-01
# Japanese: 非同期エンジンとセッションファクトリの設定

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# Async driver (asyncpg) for runtime usage
# Japanese: ランタイム用の非同期ドライバー（asyncpg）
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground_a01"

engine = create_async_engine(DATABASE_URL, echo=True)
# Japanese: echo=True により発行されるSQLをコンソールで確認できる

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
    # NOTE: Do NOT call Base.metadata.create_all() here.
    # Japanese: ここでは create_all() を呼ばないこと。テーブル作成は alembic upgrade head のみ。
