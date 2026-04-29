# Chapter S-04: select() and where() (2.0 style)
# Ref: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# DeclarativeBase=ベースクラス, Mapped=型付きカラム, mapped_column=カラム定義, relationship=リレーション
from sqlalchemy import String, Integer, ForeignKey, DateTime, func

# 各型とForeignKey、func（SQL関数）をインポート
from typing import Optional, List
import datetime


class Base(DeclarativeBase):
    # Declarative base for all ORM models
    # 全ORMモデルの基底クラス
    pass


# ✍️ TODO: Define Account model here
# ここにAccountモデルを定義
class Account(Base):
    __tablename__ = "accounts"

    # 主キー（整数）
    id: Mapped[int] = mapped_column(primary_key=True)
    # 勘定科目名（最大100文字、NULL不可
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    # 勘定タイプ（"asset" / "liability" / "equity" など）
    account_type: Mapped[str] = mapped_column(String(20), nullable=False)
    # 作成日時（DBサーバー側でデフォルト値を設定）
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Transactionとの1対多リレーション
    # lazy="raise" → async環境では明示的にeager loadしないとエラーになる設定
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", back_populates="account", lazy="raise"
    )


# ✍️ TODO: Define Transaction model here (with ForeignKey to Account)
# ここにTransactionモデルを定義（AccountへのForeignKey付き）
class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    # 外部キー（accountsテーブルのid）、親削除時カスケード
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    # 金額（最小単位：円、pence など整数管理が複式簿記の定石
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    # "debit" または "credit"
    direction: Mapped[str] = mapped_column(String(6), nullable=False)
    # 摘要（省略可能）
    description: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Accountへの多対1リレーション
    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
