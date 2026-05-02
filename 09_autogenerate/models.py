# Chapter A-02: autogenerate and manual adjustment
# Ref: https://alembic.sqlalchemy.org/en/latest/autogenerate.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# PostgreSQL が docker compose up -d postgres で起動していること

# TODO: Define your SQLAlchemy ORM models below using Mapped[X] and mapped_column()
# 以下に Mapped[X] と mapped_column() を使って ORM モデルを定義する

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, DateTime, ForeignKey
from datetime import datetime, timezone  # timezone added for aware datetime

# timezone を追加 - aware datetime（タイムゾーン付き）のデフォルト値に使用
import decimal


class Base(DeclarativeBase):
    pass


# Step 1: Define Account model here
# Step 1: Account モデルをここに定義する
class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    account_type: Mapped[str] = mapped_column(String(20), nullable=False)
    balance: Mapped[decimal.Decimal] = mapped_column(
        Numeric(18, 4), nullable=False, default=decimal.Decimal("0.0")
    )
    # aware datetime
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        # lambda でラップしないと呼び出し時ではなくクラス定義時に評価される
    )

    entries: Mapped[list["Entry"]] = relationship("Entry", back_populates="account")


class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    account: Mapped["Account"] = relationship("Account", back_populates="entries")
