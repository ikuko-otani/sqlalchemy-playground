# Async engine and session factory for Chapter S-04
# 日本語訳：S-04用 非同期エンジンとセッションファクトリ

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
# 日本語訳：非同期エンジン・非同期セッション・セッションファクトリをインポート
from sqlalchemy import text

# ---------------------------------------------------------------------------
# 📋 Copy-paste: adjust user/password/db as needed
# 📋 コピペOK：必要に応じてuser/password/dbを変更
# ---------------------------------------------------------------------------
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/playground"

# echo=True → SQLAlchemy will print every SQL statement to stdout
# 日本語訳：echo=True にすると生成されたSQLがすべてstdoutに出力される
# 💡 面接ポイント：echo=True は開発中に必ず使い、生成SQLを目視確認する習慣をつけること
engine = create_async_engine(DATABASE_URL, echo=True)

# async_sessionmaker is the 2.0-style replacement for sessionmaker
# 日本語訳：async_sessionmaker は 2.0スタイルの sessionmaker 代替
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_expire=False,  # avoid lazy-load errors after commit
    # 日本語訳：commit後のlazy-loadエラーを防ぐ
)


async def get_db() -> AsyncSession:
    """Dependency-injectable async session generator.
    日本語訳：DI可能な非同期セッションジェネレーター（FastAPI Depends用）
    """
    async with AsyncSessionLocal() as session:
        yield session


async def ping_db() -> None:
    """Quick connectivity check — run once at startup.
    日本語訳：起動時に1回だけDB接続確認を行うユーティリティ
    """
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(f"DB ping OK: {result.scalar()}")
        # 日本語訳：DB接続確認OK
