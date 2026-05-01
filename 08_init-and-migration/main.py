# Chapter A-01: run a quick insert + select to verify the migration worked
# Japanese: migration 適用後にデータ投入と取り出しを確認するスクリプト

import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal
from models import LedgerEntry  # TODO: adjust import to match your model


async def main() -> None:
    async with AsyncSessionLocal() as session:
        # TODO: insert a sample row and query it back
        # Japanese: サンプル行を挿入してクエリで取り出す
        pass


if __name__ == "__main__":
    asyncio.run(main())
