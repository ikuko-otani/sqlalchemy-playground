# database.py — Async engine and session factory
# 非同期エンジンとセッションファクトリの設定ファイル
#
# Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# TODO: Replace with your actual DATABASE_URL
# 実際の接続URLに置き換える
DATABASE_URL = "postgresql+asyncpg://ledger:ledger@localhost:5432/ledger"

# TODO (Step 1): Create the async engine with echo=True
# echo=True でクエリログを出力する非同期エンジンを作成
engine = create_async_engine(DATABASE_URL, echo=True)

# TODO (Step 1): Create the async session factory
# 非同期セッションファクトリを作成
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# TODO (Step 1): Define the DeclarativeBase subclass
# DeclarativeBase を継承した Base クラスを定義
class Base(DeclarativeBase):
    pass
