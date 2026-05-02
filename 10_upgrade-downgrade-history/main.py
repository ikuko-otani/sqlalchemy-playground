# main.py - Demo script: insert and select Account rows
# Japanese: Accountテーブルへのinsert/selectデモスクリプト
import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal
from models import Account

async def main() -> None:
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Insert a sample account
            # Japanese: サンプルアカウントを挿入する
            acct = Account(name="Cash", account_type="asset")
            session.add(acct)

        # Query all accounts
        # Japanese: すべてのアカウントを取得する
        result = await session.execute(select(Account))
        accounts = result.scalars().all()
        for a in accounts:
            print(f"id={a.id}  name={a.name}  type={a.account_type}")

if __name__ == "__main__":
    asyncio.run(main())
