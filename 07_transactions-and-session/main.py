# main.py - Entry point for Chapter 07 exercises
# Japanese: 第7章演習のエントリーポイント
import asyncio

from database import AsyncSessionLocal


async def main() -> None:
    # TODO: replace with your actual exercise logic
    # Japanese: 演習ロジックをここに記述する
    async with AsyncSessionLocal() as session:
        async with session.begin():
            print("Transaction started via session.begin()")
            # Japanese: session.begin() でトランザクション開始


if __name__ == "__main__":
    asyncio.run(main())
