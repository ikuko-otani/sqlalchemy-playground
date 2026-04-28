# Chapter S-02: Declarative Mapping (Mapped[X])
# Ref: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
#
# TODO: Implement ORM models below using SQLAlchemy 2.0 style.
# - Use Mapped[X] for all column annotations
# - Use mapped_column() for column options
# - Define at least two models with a relationship()


# imports
from __future__ import annotations
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional, List
from sqlalchemy import ForeignKey, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# base class（2.0スタイル：クラス継承方式）
# DeclarativeBase is the 2.0 replacement for declarative_base()
# DeclarativeBase は旧 declarative_base() の2.0置き換え
class Base(DeclarativeBase):
    pass

# Account model
class Account(Base):
    __tablename__ = "accounts"

    # Primary key — Mapped[int] means NOT NULL, PK auto-increments
    # Mapped[int] は NOT NULL を意味し、PKは自動採番
    id: Mapped[int] = mapped_column(primary_key=True)

    # Mapped[str] = NOT NULL varchar; Optional[str] = nullable
    # Mapped[str] は NOT NULL / Mapped[Optional[str]] は nullable
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Server-side default: DB sets created_at automatically
    # サーバーデフォルト — DBがcreated_atを自動設定する
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # One-to-many: Account has many Transactions
    # back_populates links the two sides of the relationship
    # 1対多 — back_populates で双方向リレーションを結ぶ
    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="account",
        lazy="selectin"
    )


# Transaction model
class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))

    # Decimal for monetary values — avoid float for money!
    # 金額はDecimalで — floatは金額に使わない（精度問題）
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Many-to-one back reference
    # 多対1の逆参照
    account: Mapped["Account"] = relationship(back_populates="transactions")
