# Chapter 06: N+1 and selectinload() / joinedload()
# 日本語訳：第06章：N+1問題と selectinload() / joinedload()
# Ref: https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# 日本語訳：PostgreSQL が `docker compose up -d postgres` で起動していること

from __future__ import annotations

from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# ✍️ TODO: Define Author model here
# 日本語訳：Authorモデルをここに定義する

# ✍️ TODO: Define Book model here
# 日本語訳：Bookモデルをここに定義する
