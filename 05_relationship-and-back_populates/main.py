# main.py — Exercise runner: insert and query with relationships
# 演習実行スクリプト：リレーションシップを使った挿入・検索
#
# Run: python -m 05_relationship-and-back_populates.main
# 実行方法：リポジトリルートから上記コマンドを実行する

import asyncio

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import AsyncSessionLocal, engine

# TODO: import User, Post from models after defining them (Step 1)
# Step 1 で User, Post を定義したらここでインポートする
from models import Base, User, Post


async def create_tables() -> None:
    # Create all tables defined in Base.metadata
    # Base.metadata に登録されたテーブルを全て作成する
    async with engine.begin() as conn:
        # Drop all tables first, then recreate
        # 既存テーブルを全削除してから再作成（開発専用）
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created.")
    # テーブルを作成しました


async def seed_data() -> None:
    # TODO: Insert sample User and Post records (Step 2)
    # Step 2 でサンプルデータを挿入する
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Create users with posts in one transaction
            # 1トランザクション内でユーザーと投稿を作成する
            alice = User(name="Alice", email="alice@example.com")
            bob = User(name="Bob", email="bob@example.com")

            alice.posts = [
                Post(title="Alice Post 1"),
                Post(title="Alice Post 2"),
            ]
            bob.posts = [
                Post(title="Bob Post 1"),
            ]
            session.add_all([alice, bob])
        # session.begin() auto-commits here
        # session.begin() のコンテキストマネージャ終了時に自動コミット
    print("Seed data inserted.")


async def query_with_selectinload() -> None:
    # TODO: Query users with posts using selectinload (Step 2)
    # Step 2 で selectinload を使って users と posts を取得する
    async with AsyncSessionLocal() as session:
        # selectinload fires: SELECT * FROM users + SELECT * FROM posts WHERE user_id IN (...)
        # selectinload は2クエリで全ユーザーと投稿を取得する（N+1にならない
        stmt = select(User).options(selectinload(User.posts)).order_by(User.id)
        result = await session.execute(stmt)
        users = result.scalars().all()

    for user in users:
        print(f"{user.name}: {[p.title for p in user.posts]}")
        # 各ユーザーの投稿タイトル一覧を表示


async def main() -> None:
    await create_tables()
    await seed_data()
    await query_with_selectinload()


if __name__ == "__main__":
    asyncio.run(main())
