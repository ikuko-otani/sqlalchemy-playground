# database.py — Async engine and session factory
# 日本語訳：非同期エンジンとセッションファクトリの設定

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# TODO: Replace with your actual DB URL if needed
# 日本語訳：必要に応じて実際のDB URLに変更してください
DATABASE_URL = "postgresql+asyncpg://ledger:ledger@localhost:5432/ledger_db"

# TODO: Create the async engine with echo=True so you can observe generated SQL
# 日本語訳：echo=True を設定して生成SQLをコンソールで観察できるようにする
# engine = create_async_engine(DATABASE_URL, echo=True)

# TODO: Create the async session factory
# 日本語訳：非同期セッションファクトリを作成する
# AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
