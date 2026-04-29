# Chapter 06 exercise runner — observe SQL logs in the terminal
# 日本語訳：第06章の実行スクリプト。ターミナルのSQLログを観察する

from __future__ import annotations

import asyncio

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from database import AsyncSessionLocal
from models import Base, Author, Book  # type: ignore


async def main() -> None:
    # ✍️ TODO: Insert sample data (Author + Books) and query with selectinload
    # 日本語訳：サンプルデータを投入し、selectinload でクエリする
    pass


if __name__ == "__main__":
    asyncio.run(main())
