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
            # lazy="raise" のため、ここで InvalidRequestError が発生する
            print(author.books)  # ← intentional error to observe


# ✍️ Query WITH selectinload — issues 2 SQL statements total (1 for authors, 1 IN query for books)
# selectinload を使うと2本のSQLで完結（著者1本＋IN句で本1本）
async def query_with_selectinload() -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Author).options(selectinload(Author.books))
        )
        authors = result.scalars().all()
        for author in authors:
            print(f"{author.name}: {[b.title for b in author.books]}")


# ✍️ Query WITH joinedload — issues 1 SQL with LEFT OUTER JOIN
# joinedload を使うと1本のSQLでJOINして取得する
async def query_with_joinedload() -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Author).options(joinedload(Author.books)))
        authors = result.unique().scalars().all()
        # unique() is needed when joinedload is used with collections
        # コレクションに joinedload を使う場合は unique() が必要
        for author in authors:
            print(f"{author.name}: {[b.title for b in author.books]}")


async def main() -> None:
    # ✍️ TODO: Insert sample data (Author + Books) and query with selectinload
    # サンプルデータを投入し、selectinload でクエリする
    await seed_data()

    print("\n--- selectinload ---")
    await query_with_selectinload()

    print("\n--- joinedload ---")
    await query_with_joinedload()


if __name__ == "__main__":
    asyncio.run(main())
