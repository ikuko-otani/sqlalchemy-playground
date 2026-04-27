# main.py — Entry point: test DB connection, create tables, insert & select
# 日本語訳：DB接続・テーブル作成・データ投入・取得を試すスクリプト
#
# Run: python -m 01_engine-and-connection.main
# (or: cd 01_engine-and-connection && python main.py)

import asyncio

from database import AsyncSessionLocal, Base, engine
from models import Item  # TODO: define Item in models.py
from sqlalchemy import select


async def init_db() -> None:
    """Create all tables defined in Base.metadata."""
    # 日本語訳：Base.metadata に登録されたテーブルをすべて作成する
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def insert_sample(name: str) -> None:
    """Insert one Item and commit."""
    # 日本語訳：Item を1件挿入してコミットする
    # TODO (✍️ Step 3): implement using AsyncSessionLocal
    pass


async def fetch_all() -> None:
    """Select all Items and print them."""
    # 日本語訳：全件取得して表示する
    # TODO (✍️ Step 3): implement using select(Item)
    pass


async def main() -> None:
    await init_db()
    await insert_sample("hello-berlin")
    await fetch_all()


if __name__ == "__main__":
    asyncio.run(main())
