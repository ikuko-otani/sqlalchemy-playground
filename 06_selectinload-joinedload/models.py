# Chapter 06: N+1 and selectinload() / joinedload()
# 第06章：N+1問題と selectinload() / joinedload()
# Ref: https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# PostgreSQL が `docker compose up -d postgres` で起動していること

from __future__ import annotations

from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# ✍️ TODO: Define Author model here
# Authorモデルをここに定義する
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # relationship to Book — lazy="raise" enforces eager load discipline
    # lazy="raise" で Lazy load を禁止し、明示的ローディングを強制する
    books: Mapped[List["Book"]] = relationship(
        "Book", back_populates="author", lazy="raise"
    )


# ✍️ TODO: Define Book model here
# Bookモデルをここに定義する
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey="authors.id")

    author: Mapped["Author"] = relationship(
        "Author", back_populates="books", lazy="raise"
    )
