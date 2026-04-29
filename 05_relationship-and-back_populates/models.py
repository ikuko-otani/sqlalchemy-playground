# Chapter S-05: relationship() and back_populates
# Ref: https://docs.sqlalchemy.org/en/20/orm/relationship_api.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# PostgreSQLが `docker compose up -d postgres` で起動していること
#
# Learning goals:
# 学習目標
#   1. Define bidirectional relationships with relationship() and back_populates
#      双方向リレーションシップを relationship() と back_populates で定義する
#   2. Understand lazy vs eager loading (selectinload / joinedload)
#      遅延ロードと積極的ロードの違いを理解する
#   3. Avoid N+1 query problems in async context
#      非同期コンテキストでのN+1クエリ問題を回避する

from __future__ import annotations

from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    # Base class for all ORM models
    # すべてのORMモデルの基底クラス
    pass


# TODO: Define User model here (Step 1)
# Step 1 で User モデルをここに定義する
class User(Base):
    __tablename__ = "users"

    # Primary key — automatically NOT NULL
    # 主キー（自動的に NOT NULL）
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)

    # One-to-many: one user has many posts
    # 1対多：1ユーザーが複数の投稿を持つ
    posts: Mapped[List["Post"]] = relationship(
        back_populates="author",
        lazy="raise",  # raise error if lazy load attempted in async
        cascade="all, delete-orphan",
    )


# TODO: Define Post model here (Step 1)
# Step 1 で Post モデルをここに定義する
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Many-to-one: many posts belong to one user
    # 多対1：複数の投稿が1ユーザーに属する
    author: Mapped["User"] = relationship(
        back_populates="posts",
        lazy="raise",
    )


# TODO: Define Account model here (Step 3 - Flagship connection)
# Step 3 で payment-ledger-api に対応する Account モデルを定義する
class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(10), unique=True)

    # Entries where this account is debited
    # この勘定が借方になる仕訳明細
    debit_entries: Mapped[List["Entry"]] = relationship(
        back_populates="debit_account",
        foreign_keys="Entry.debit_account_id",
        lazy="raise",
    )

    # Entries where this account is credited
    # この勘定が貸方になる仕訳明細
    credit_entries: Mapped[List["Entry"]] = relationship(
        back_populates="credit_account",
        foreign_keys="Entry.credit_account_id",
        lazy="raise",
    )


# TODO: Define Entry model here (Step 3 - Flagship connection)
# Step 3 で Entry モデルをここに定義する（複式簿記の仕訳明細）
class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]  # in cents / 金額（最小通貨単位）
    debit_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    credit_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))

    debit_account: Mapped["Account"] = relationship(
        back_populates="debit_entries",
        foreign_keys=[debit_account_id],
        lazy="raise",
    )
    credit_account: Mapped["Account"] = relationship(
        back_populates="credit_entries",
        foreign_keys=[credit_account_id],
        lazy="raise",
    )
