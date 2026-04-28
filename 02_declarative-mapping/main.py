# main.py — Script to run insert / select exercises
# insert / select 演習を実行するスクリプト
#
# Run with: python -m 02_declarative-mapping.main
# 実行方法: python -m 02_declarative-mapping.main

# TODO: Import engine, AsyncSessionLocal, and models
# engine, AsyncSessionLocal, モデルをimportする

import asyncio
from sqlalchemy import select
from database import engine, AsyncSessionLocal
from models import Base, Account, Transaction

# TODO: Implement async main() that:
#   1. Creates all tables (Base.metadata.create_all)
#   2. Inserts sample rows
#   3. Queries them back and prints results
# 以下を実行する async main() を実装する
#   1. テーブルを全作成
#   2. サンプル行を挿入
#   3. 取り出して print

# create tables
async def create_tables():
    # Run DDL: CREATE TABLE IF NOT EXISTS for all models
    # 全モデルのCREATE TABLE IF NOT EXISTSを実行
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# insert sample data
async def insert_samples():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # session.begin() manages the transaction boundary
            # session.begin() がトランザクション境界を管理する
            acc = Account(
                name="Cash",
                description="Main cash account"
            )
            session.add(acc)
            await session.flush()  # assigns acc.id without committing

            # flush: DBに送信するがトランザクションはまだ開いている
            tx = Transaction(
                account_id=acc.id,
                amount="1000.00",
                description="Opening balance"
            )
            session.add(tx)
        # session.begin() context exit auto-commits
        # with ブロック終了時に自動コミット

# select and print
async def query_accounts():
    async with AsyncSessionLocal() as session:
        # 2.0-style: session.execute(select(Model))
        # 2.0スタイル — session.execute(select(Model))
        result = await session.execute(select(Account))
        account = result.scalars().all()
        for acc in account:
            print(f"Account: {acc.id} | {acc.name} | txns: {len(acc.transactions)}")

async def main():
    await create_tables()
    await insert_samples()
    await query_accounts()

if __name__ == "__main__":
    asyncio.run(main())
