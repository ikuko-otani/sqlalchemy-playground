# main.py - Demo script: insert and select Account rows
# Accountテーブルへのinsert/selectデモスクリプト
import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal
from models import Account


async def main() -> None:
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Insert a sample account
            # サンプルアカウントを挿入する
            session.add(Account(name="Cash", account_type="asset"))
            session.add(Account(name="Revenue", account_type="income"))
            session.add(Account(name="Rent Expense", account_type="expense"))

        # Query all accounts
        # すべてのアカウントを取得する
        result = await session.execute(select(Account).order_by(Account.id))
        accounts = result.scalars().all()
        for a in accounts:
            print(f"  id={a.id}  name={a.name}  type={a.account_type}")


if __name__ == "__main__":
    asyncio.run(main())
