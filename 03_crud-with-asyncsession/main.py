# S-03 exercise runner: insert and query Account + JournalEntry
# S-03演習ランナー：AccountとJournalEntryの挿入とクエリ
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

from database import AsyncSessionLocal, engine
from models import Base, Account, JournalEntry


async def init_db() -> None:
    """Create tables if they don't exist (dev only — use Alembic in production).
    テーブルが存在しなければ作成（開発専用。本番ではAlembicを使う）。
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_data() -> None:
    """Insert sample Account and JournalEntry rows.
    サンプルのAccountとJournalEntryを挿入する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: Create an Account object and add it to session
            # Accountオブジェクトを作成してセッションに追加する
            account = Account(
                name="Cash",
                account_type="asset",
            )
            session.add(account)

            # flush() to get the PK before inserting JournalEntry
            # flush() でPKを確定してからJournalEntryを作る
            await session.flush()

            entry = JournalEntry(
                account_id=account.id,
                amount=Decimal("100000.00"),
                direction="debit",
                memo="Initial deposit / 初期入金",
            )
            session.add(entry)

        # commit() is called automatically on __aexit__
        # ブロックを抜けると自動でcommit

    print(f"Seeded: account.id={account.id}")


async def query_accounts() -> None:
    """Select all accounts and print them.
    全Accountを検索して表示する。
    """
    async with AsyncSessionLocal() as session:
        # ✍️ TODO: write select(Account) statement and execute with session.execute()
        # select(Account)文を書き、session.execute()で実行する
        # 🔍 N+1 hint: use selectinload(Account.entries) to eagerly load entries
        # N+1対策：selectinload(Account.entries) でentriesを先行ロードする

        # Build SELECT statement — 2.0 style (NOT session.query()!)
        # 2.0スタイルのSELECT文（session.query()ではない！）
        stmt = (
            select(Account)
            .options(selectinload(Account.entries))
            .order_by(Account.id)
        )
        result = await session.execute(stmt)
        accounts = result.scalars().all()

        for acc in accounts:
            print(f"Account: {acc.id} | {acc.name} | {acc.account_type}")
            for entry in acc.entries:
                print(f"  Entry: {entry.direction} {entry.amount} ({entry.memo})")


async def update_account(account_id: int, new_name: str) -> None:
    """Fetch by PK and update name.
    主キーで取得して名前を更新する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: use session.get(Account, account_id) then mutate and commit
            # session.get(Account, account_id) で取得 → 変更 → commit

            # session.get() uses Identity Map — no extra SELECT if already cached
            # session.get()はIdentity Mapを使う — キャッシュ済みなら追加SELECTなし

            account = await session.get(Account, account_id)
            if account is None:
                raise ValueError(f"Account {account_id} not found")
            account.name = new_name  # ORM tracks the change automatically
            # No session.add() needed — dirty object is auto-flushed on commit
            # session.add()不要 — 変更済みオブジェクトはcommit時に自動flush


async def delete_account(account_id: int) -> None:
    """Delete an account by PK.
    主キーでAccountを削除する。
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # ✍️ TODO: session.get() then session.delete(obj)
            # session.get() で取得後 session.delete(obj) で削除
            account = await session.get(Account, account_id)
            if account:
                await session.delete(account)


async def main() -> None:
    await init_db()
    await seed_data()
    await query_accounts()
    await update_account(1, "Cash (Updated)")
    await query_accounts()  # 変更確認
    await delete_account(1)
    await query_accounts()  # 削除確認（空になるはず）


if __name__ == "__main__":
    asyncio.run(main())
