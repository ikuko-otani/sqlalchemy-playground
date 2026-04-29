# Chapter S-04: select() and where() demo script
# S-04 select() と where() のデモスクリプト
#
# Run: python -m 04_select-and-where.main
# 実行方法：python -m 04_select-and-where.main

import asyncio
from sqlalchemy import select, func

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
    async with AsyncSessionLocal() as session:
        # Insert a Transaction linked to Cash account
        # Cashアカウントに紐づくTransactionを挿入
        async with session.begin():
            stmt_cash = select(Account).where(Account.name == "Cash")
            cash = await session.scalar(stmt_cash)
            session.add(
                Transaction(
                    account_id=cash.id,
                    amount=10000,
                    direction="debit",
                    description="Initial deposit",
                )
            )
            # 初期入金トランザクションを追加

        # Fetch Account WITH transactions using selectinload (avoids N+1)
        # selectinloadでTransactionを一括取得（N+1回避）
        stmt = select(Account).options(selectinload(Account.transactions))
        result = await session.scalars(stmt)
        for acc in result.all():
            print(f"{acc.name}: {len(acc.transactions)} transactions")

    # ✍️ TODO Step 4: aggregate — func.count(), func.sum()
    # Step4でfunc.count()等の集計クエリを実装
    async with AsyncSessionLocal() as session:
        # Count total number of accounts
        # 勘定科目の総数を取得
        count_stmt = select(func.count(Account.id))
        total = await session.scalar(count_stmt)
        print(f"  Total accounts: {total}")

        # Sum of all transaction amounts
        # 全トランザクションの合計金額を取得
        sum_stmt = select(func.sum(Transaction.amount))
        total_amount = await session.scalar(sum_stmt)
        print(f"  Total amount: {total_amount}")

        # Count transactions grouped by direction (debit / credit)
        # direction別にトランザクション件数を集計
        group_stmt = select(Transaction.direction, func.count(Transaction.id)).group_by(
            Transaction.direction
        )
        rows = await session.execute(group_stmt)
        for direction, cnt in rows.all():
            print(f"  {direction}: {cnt} transactions")


if __name__ == "__main__":
    asyncio.run(main())
