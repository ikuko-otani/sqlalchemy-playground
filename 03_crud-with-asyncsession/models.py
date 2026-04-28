# Chapter S-03: CRUD with AsyncSession
# 日本語訳：第3章：AsyncSessionを使ったCRUD操作
# Ref: https://docs.sqlalchemy.org/en/20/orm/session_basics.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# 日本語訳：前提条件：`docker compose up -d postgres` でPostgreSQLが起動済みであること

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import String, Numeric, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# --- Base class ---
# All ORM models inherit from this single Base.
# 日本語訳：すべてのORMモデルはこの単一のBaseを継承する。
class Base(DeclarativeBase):
    pass


# ✍️ TODO: Define Account model here
# 日本語訳：ここにAccountモデルを定義する（自分で入力）
# Fields: id (int PK), name (str), account_type (str), created_at (datetime server_default)
# Relationship: entries -> list["JournalEntry"]


# ✍️ TODO: Define JournalEntry model here
# 日本語訳：ここにJournalEntryモデルを定義する（自分で入力）
# Fields: id (int PK), account_id (FK -> accounts.id), amount (Decimal),
#         direction (str: 'debit'/'credit'), memo (Optional[str]), created_at (datetime)
# Relationship: account -> Account (back_populates="entries")
