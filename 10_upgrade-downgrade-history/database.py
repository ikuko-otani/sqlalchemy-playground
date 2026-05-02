# database.py - Async engine and session factory
# Japanese: 非同期エンジンとセッションファクトリの設定
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Async driver (asyncpg) for runtime use
# Japanese: ランタイム用非同期ドライバー
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground_a03"

# DeclarativeBase is the base class for all ORM models
# Japanese: すべてのORMモデルの基底クラス
class Base(DeclarativeBase):
    pass

# Create async engine with echo=True to log all SQL statements
# Japanese: echo=Trueですべての発行SQLをログ出力する
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory bound to the async engine
# Japanese: 非同期エンジンに紐付いたセッションファクトリ
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
