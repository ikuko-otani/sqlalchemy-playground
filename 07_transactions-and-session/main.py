# main.py - Entry point for Chapter 07 exercises
# 第7章演習のエントリーポイント
import asyncio
from decimal import Decimal

from database import AsyncSessionLocal
from models import Account, TransactionLog


async def insert_with_begin() -> None:
    # TODO: replace with your actual exercise logic
    # 演習ロジックをここに記述する
    async with AsyncSessionLocal() as session:
        # session.begin() auto-commits on success, rolls back on exception
        # 成功時は自動commit、例外時は自動rollback
        async with session.begin():
            print("Transaction started via session.begin()")
            # session.begin() でトランザクション開始

            account = Account(name="Checking", balance=Decimal("1000.00"))
            session.add(account)

            # flush() sends SQL to DB but does NOT commit yet
            # flush()はSQLをDBに送るがまだcommitしない
            await session.flush()
            print(f"After flush — account.id = {account.id}")

            log = TransactionLog(account_id=account.id, amount=Decimal("1000.00"))
            session.add(log)

        # commit happens automatically here when `async with session.begin()` exits
        # ブロック終了時に自動でcommitされる
        print("Transaction committed.")


async def flush_vs_commit_demo() -> None:
    async with AsyncSessionLocal() as session:
        async with session.begin():
            acc = Account(name="Savings", balance=Decimal("500.00"))
            session.add(acc)

            # Before flush: id is None because no SQL sent yet
            # flush前はSQLが送られていないのでidはNone
             print(f"Before flush: acc.id = {acc.id}")

            


if __name__ == "__main__":
    asyncio.run(flush_vs_commit_demo())
