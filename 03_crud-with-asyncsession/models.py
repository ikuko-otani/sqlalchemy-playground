# Chapter S-03: CRUD with AsyncSession
# 第3章：AsyncSessionを使ったCRUD操作
# Ref: https://docs.sqlalchemy.org/en/20/orm/session_basics.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# 前提条件：`docker compose up -d postgres` でPostgreSQLが起動済みであること

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import String, Numeric, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# --- Base class ---
# All ORM models inherit from this single Base.
# すべてのORMモデルはこの単一のBaseを継承する。
class Base(DeclarativeBase):
    pass


# TODO: Define Account model here
# ここにAccountモデルを定義する
# Fields: id (int PK), name (str), account_type (str), created_at (datetime server_default)
# Relationship: entries -> list["JournalEntry"]

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    account_type: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    # Relationship: one Account has many JournalEntry
    entries: Mapped[list["JournalEntry"]] = relationship(
        "JournalEntry",
        back_populates="account",
        lazy="select",
        cascade="all, delete-orphan",  # ORM側カスケード
    )


# TODO: Define JournalEntry model here
# ここにJournalEntryモデルを定義する
# Fields: id (int PK), account_id (FK -> accounts.id), amount (Decimal),
#         direction (str: 'debit'/'credit'), memo (Optional[str]), created_at (datetime)
# Relationship: account -> Account (back_populates="entries")

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    direction: Mapped[str] = mapped_column(
        String(6),
        nullable=False
    )  # 'debit'/'credit'
    memo: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    # Relationship: many JournalEntry belongs to one Account
    account: Mapped["Account"] = relationship(
        "Account",
        back_populates="entries"
    )
