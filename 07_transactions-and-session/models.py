# Chapter 07: Transactions & Session.begin()
# Ref: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`

from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=Decimal("0.00"))

    # Relationship: one account has many log entries
    # 1つのAccountは複数のTransactionLogを持つ
    logs: Mapped[List["TransactionLog"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )


class TransactionLog(Base):
    __tablename__ = "transaction_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    account: Mapped["Account"] = relationship(back_populates="logs")
