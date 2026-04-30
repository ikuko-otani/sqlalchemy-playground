# Chapter 06 exercise runner — observe SQL logs in the terminal
# 第06章の実行スクリプト。ターミナルのSQLログを観察する

from __future__ import annotations

import asyncio

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from database import AsyncSessionLocal
from models import Base, Author, Book  # type: ignore


# ✍️ Insert sample data: 2 authors, 3 books each
# サンプルデータ投入：著者2名、それぞれ本3冊
async def seed_data() -> None:
    async with AsyncSessionLocal() as session:
        async with session.begin():
            a1 = Author(name="Dostoevsky")
            a2 = Author(name="Kafka")
            session.add_all([a1, a2])
            await session.flush()  # get IDs without committing

            session.add_all(
                [
                    Book(title="Crime and Punishment", author_id=a1.id),
                    Book(title="The Idiot", author_id=a1.id),
                    Book(title="The Brothers Karamazov", author_id=a1.id),
                    Book(title="The Trial", author_id=a2.id),
                    Book(title="The Castle", author_id=a2.id),
                    Book(title="Amerika", author_id=a2.id),
                ]
            )


# ✍️ Query WITHOUT selectinload — triggers MissingGreenlet or lazy load error
# selectinload なしでクエリ → lazy=raise により例外が発生することを確認
async def query_without_eager_load() -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Author))
        authors = result.scalars().all()
        for author in authors:
            # This will raise because lazy="raise" is set
            # 日本語訳：lazy="raise" のため、ここで InvalidRequestError が発生する
            print(author.books)  # ← intentional error to observe


async def main() -> None:
    # ✍️ TODO: Insert sample data (Author + Books) and query with selectinload
    # サンプルデータを投入し、selectinload でクエリする
    await seed_data()
    await query_without_eager_load()


if __name__ == "__main__":
    asyncio.run(main())
