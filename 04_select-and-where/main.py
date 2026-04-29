# Chapter S-04: select() and where() demo script
# S-04 select() と where() のデモスクリプト
#
# Run: python -m 04_select-and-where.main
# 実行方法：python -m 04_select-and-where.main

import asyncio
from sqlalchemy import select

# 2.0スタイルの select() をインポート
from sqlalchemy.orm import selectinload

# N+1問題を回避するための selectinload をインポート
from database import engine, AsyncSessionLocal, ping_db
from models import Base, Account, Transaction


async def create_tables() -> None:
    """Create all tables defined in Base.metadata.
    Base.metadataに定義された全テーブルを作成
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created.")
    # テーブル作成完了


async def main() -> None:
    await ping_db()
    await create_tables()

    # ✍️ TODO Step 1: Insert seed data (Account rows)
    # Step1でAccountのシードデータを挿入
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # session.begin() でトランザクション開始→自動commit
            session.add_all(
                [
                    Account(name="Cash", account_type="asset"),
                    Account(name="Revenue", account_type="equity"),
                ]
            )
    # 2つのAccountをまとめてinsert

    # ✍️ TODO Step 2: select() with where() — basic scalar query
    # Step2でselect() + where() の基本クエリを実装
    async with AsyncSessionLocal() as session:
        # account_type が "asset" のAccountを取得
        stmt = select(Account).where(Account.account_type == "asset")
        result = await session.scalars(stmt)
        accounts = result.all()
        for acc in accounts:
            # 取得したAccountを出力
            print(f"  id={acc.id}  name={acc.name}")

    # ✍️ TODO Step 3: select() with relationship (selectinload)
    # 🔍 N+1問題：relationship を fetchする場合は必ず selectinload/joinedload を使うこと
    # Step3でselectinloadを使ったリレーション取得を実装

    # ✍️ TODO Step 4: aggregate — func.count(), func.sum()
    # Step4でfunc.count()等の集計クエリを実装


if __name__ == "__main__":
    asyncio.run(main())
