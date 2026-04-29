# main.py — Exercise runner: insert and query with relationships
# 日本語訳：演習実行スクリプト：リレーションシップを使った挿入・検索
#
# Run: python -m 05_relationship-and-back_populates.main
# 日本語訳：実行方法：リポジトリルートから上記コマンドを実行する

import asyncio

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .database import AsyncSessionLocal, engine
from .models import Base

# TODO: import User, Post from models after defining them (Step 1)
# 日本語訳：Step 1 で User, Post を定義したらここでインポートする


async def create_tables() -> None:
    # Create all tables defined in Base.metadata
    # 日本語訳：Base.metadata に登録されたテーブルを全て作成する
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created.")
    # 日本語訳：テーブルを作成しました


async def seed_data() -> None:
    # TODO: Insert sample User and Post records (Step 2)
    # 日本語訳：Step 2 でサンプルデータを挿入する
    pass


async def query_with_selectinload() -> None:
    # TODO: Query users with posts using selectinload (Step 2)
    # 日本語訳：Step 2 で selectinload を使って users と posts を取得する
    pass


async def main() -> None:
    await create_tables()
    await seed_data()
    await query_with_selectinload()


if __name__ == "__main__":
    asyncio.run(main())
