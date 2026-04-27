# main.py — Entry point: test DB connection, create tables, insert & select
# DB接続・テーブル作成・データ投入・取得を試すスクリプト
#
# Run: python -m 01_engine-and-connection.main
# (or: cd 01_engine-and-connection && python main.py)

import asyncio

from database import AsyncSessionLocal, Base, engine
from models import Item  # TODO: define Item in models.py
from sqlalchemy import select


async def init_db() -> None:
    """Create all tables defined in Base.metadata."""
    # Base.metadata に登録されたテーブルをすべて作成する
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # ↑ engine.begin() は DDL用。セッションではなくコネクションを直接使う


async def insert_sample(name: str) -> None:
    """Insert one Item and commit."""
    # Item を1件挿入してコミットする
    # TODO (Step 3): implement using AsyncSessionLocal
    async with AsyncSessionLocal() as session:
        async with session.begin():
            item = Item(name=name, description="inserted from main.py")
            session.add(item)
        # ↑ session.begin() コンテキストを抜けると自動 commit
        # 🔍 session.begin() の外で add() すると commit されないので注意！


async def fetch_all() -> None:
    """Select all Items and print them."""
    # 全件取得して表示する
    # TODO (Step 3): implement using select(Item)
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Item))
        items = result.scalars().all()
        for item in items:
            print(item)


async def main() -> None:
    await init_db()
    await insert_sample("hello-berlin")
    await fetch_all()


if __name__ == "__main__":
    asyncio.run(main())
