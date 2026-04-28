# S-03 exercise runner: insert and query Account + JournalEntry
# 日本語訳：S-03演習ランナー：AccountとJournalEntryの挿入とクエリ
"""
Run with:
    python -m 03_crud-with-asyncsession.main
or from inside the directory:
    python main.py

Make sure PostgreSQL is up:
    docker compose up -d postgres
"""
from __future__ import annotations

import asyncio
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .database import AsyncSessionLocal, engine
from .models import Base, Account, JournalEntry


async def init_db() -> None:
    """Create tables if they don't exist (dev only — use Alembic in production).
    日本語訳：テーブルが存在しなければ作成（開発専用。本番ではAlembicを使う）。
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_data() -> None:
    """Insert sample Account and JournalEntry rows.
    日本語訳：サンプルのAccountとJournalEntryを挿入する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: Create an Account object and add it to session
            # 日本語訳：Accountオブジェクトを作成してセッションに追加する
            pass


async def query_accounts() -> None:
    """Select all accounts and print them.
    日本語訳：全Accountを検索して表示する。
    """
    async with AsyncSessionLocal() as session:
        # ✍️ TODO: write select(Account) statement and execute with session.execute()
        # 日本語訳：select(Account)文を書き、session.execute()で実行する
        # 🔍 N+1 hint: use selectinload(Account.entries) to eagerly load entries
        # 日本語訳：N+1対策：selectinload(Account.entries) でentriesを先行ロードする
        pass


async def update_account(account_id: int, new_name: str) -> None:
    """Fetch by PK and update name.
    日本語訳：主キーで取得して名前を更新する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: use session.get(Account, account_id) then mutate and commit
            # 日本語訳：session.get(Account, account_id) で取得 → 変更 → commit
            pass


async def delete_account(account_id: int) -> None:
    """Delete an account by PK.
    日本語訳：主キーでAccountを削除する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: session.get() then session.delete(obj)
            # 日本語訳：session.get() で取得後 session.delete(obj) で削除
            pass


async def main() -> None:
    await init_db()
    await seed_data()
    await query_accounts()


if __name__ == "__main__":
    asyncio.run(main())
