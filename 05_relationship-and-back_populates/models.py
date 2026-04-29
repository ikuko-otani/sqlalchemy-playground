# Chapter S-05: relationship() and back_populates
# Ref: https://docs.sqlalchemy.org/en/20/orm/relationship_api.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# 日本語訳：PostgreSQLが `docker compose up -d postgres` で起動していること
#
# Learning goals:
# 日本語訳：学習目標
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
    # 日本語訳：すべてのORMモデルの基底クラス
    pass


# TODO: Define User model here (Step 1)
# 日本語訳：Step 1 で User モデルをここに定義する


# TODO: Define Post model here (Step 1)
# 日本語訳：Step 1 で Post モデルをここに定義する


# TODO: Define Account model here (Step 3 - Flagship connection)
# 日本語訳：Step 3 で payment-ledger-api に対応する Account モデルを定義する


# TODO: Define Entry model here (Step 3 - Flagship connection)
# 日本語訳：Step 3 で Entry モデルをここに定義する（複式簿記の仕訳明細）
