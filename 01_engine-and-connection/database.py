# database.py — Async engine and session factory
# 日本語訳：非同期エンジンとセッションファクトリの設定ファイル
#
# Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# TODO: Replace with your actual DATABASE_URL
# 日本語訳：実際の接続URLに置き換えてください
# 📋 Copy-paste OK
DATABASE_URL = "postgresql+asyncpg://ledger:ledger@localhost:5432/ledger"

# TODO (✍️ Step 1): Create the async engine with echo=True
# 日本語訳：echo=True でクエリログを出力する非同期エンジンを作成してください
# Hint: create_async_engine(DATABASE_URL, echo=True)
engine = None  # replace me

# TODO (✍️ Step 1): Create the async session factory
# 日本語訳：非同期セッションファクトリを作成してください
# Hint: async_sessionmaker(engine, expire_on_commit=False)
AsyncSessionLocal = None  # replace me


# TODO (✍️ Step 1): Define the DeclarativeBase subclass
# 日本語訳：DeclarativeBase を継承した Base クラスを定義してください
class Base(DeclarativeBase):
    pass
