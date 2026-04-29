# Chapter S-04: select() and where() demo script
# 日本語訳：S-04 select() と where() のデモスクリプト
#
# Run: python -m 04_select-and-where.main
# 実行方法：python -m 04_select-and-where.main

import asyncio
from sqlalchemy import select
# 日本語訳：2.0スタイルの select() をインポート
from sqlalchemy.orm import selectinload
# 日本語訳：N+1問題を回避するための selectinload をインポート
from database import engine, AsyncSessionLocal, ping_db
from models import Base  # Account, Transaction を定義後にインポート追加


async def create_tables() -> None:
    """Create all tables defined in Base.metadata.
    日本語訳：Base.metadataに定義された全テーブルを作成
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created.")
    # 日本語訳：テーブル作成完了


async def main() -> None:
    await ping_db()
    await create_tables()

    # ✍️ TODO Step 1: Insert seed data (Account rows)
    # 日本語訳：Step1でAccountのシードデータを挿入

    # ✍️ TODO Step 2: select() with where() — basic scalar query
    # 日本語訳：Step2でselect() + where() の基本クエリを実装

    # ✍️ TODO Step 3: select() with relationship (selectinload)
    # 🔍 N+1問題：relationship を fetchする場合は必ず selectinload/joinedload を使うこと
    # 日本語訳：Step3でselectinloadを使ったリレーション取得を実装

    # ✍️ TODO Step 4: aggregate — func.count(), func.sum()
    # 日本語訳：Step4でfunc.count()等の集計クエリを実装


if __name__ == "__main__":
    asyncio.run(main())
