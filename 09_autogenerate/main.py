# main.py - Script to verify migration and insert/query data
# migration 適用後にデータ投入・取り出しを確認するスクリプト

import asyncio
from sqlalchemy import select, text
from database import AsyncSessionLocal, engine
from models import Base  # noqa: F401 - ensures models are registered

# Base を import することで全モデルが Base.metadata に登録される


async def check_connection() -> None:
    """Verify database connectivity."""
    # DB接続確認
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("DB connection OK:", result.scalar())


async def insert_and_query() -> None:
    """Insert sample data and query it back."""
    # サンプルデータを投入して取り出す
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # TODO: create Account instances and add to session
            # Account インスタンスを作成してセッションに追加する
            pass

        # TODO: query and print results
        # 結果を取り出して表示する
        pass


async def main() -> None:
    await check_connection()
    await insert_and_query()


if __name__ == "__main__":
    asyncio.run(main())
