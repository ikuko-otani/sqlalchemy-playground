# database.py - Async engine and session factory
# Japanese: 非同期エンジンとセッションファクトリの定義

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# Async driver: asyncpg
# Japanese: 非同期ドライバとして asyncpg を使用
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground_a02"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Log all SQL statements - useful for learning
    # Japanese: 全SQLをログ出力 - 学習時に生成SQLを確認するため
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    # Japanese: expire_on_commit=False: commit後もオブジェクト属性を維持する
)
