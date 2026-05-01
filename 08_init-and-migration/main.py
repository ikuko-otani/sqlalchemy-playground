# Chapter A-01: run a quick insert + select to verify the migration worked
# migration 適用後にデータ投入と取り出しを確認するスクリプト

import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal
from models import LedgerEntry  # TODO: adjust import to match your model


async def main() -> None:
    async with AsyncSessionLocal() as session:
        # TODO: insert a sample row and query it back
        # サンプル行を挿入してクエリで取り出す
        async with session.begin():
            entry = LedgerEntry(
                description="Initial deposit",
                amount=10000.00,
            )
            session.add(entry)
        # Flush automatically happens at commit; verify with echo=True in database.py

        result = await session.execute(
            select(LedgerEntry).where(LedgerEntry.amount > 0)
        )
        entries = result.scalars().all()
        for e in entries:
            print(f"id={e.id}, desc={e.description}, amount={e.amount}")


if __name__ == "__main__":
    asyncio.run(main())
