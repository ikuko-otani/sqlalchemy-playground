# Chapter S-04: select() and where() (2.0 style)
# Ref: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`

# ---------------------------------------------------------------------------
# 日本語訳：S-04 select() と where() (2.0スタイル)
# 参照：上記ドキュメントURL
# 前提：`docker compose up -d postgres` でPostgreSQL起動済み
# ---------------------------------------------------------------------------

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# 日本語訳：DeclarativeBase=ベースクラス, Mapped=型付きカラム, mapped_column=カラム定義, relationship=リレーション
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
# 日本語訳：各型とForeignKey、func（SQL関数）をインポート
from typing import Optional, List
import datetime


class Base(DeclarativeBase):
    # Declarative base for all ORM models
    # 日本語訳：全ORMモデルの基底クラス
    pass


# ✍️ TODO: Define Account model here
# 日本語訳：ここにAccountモデルを定義してください
# class Account(Base):
#     __tablename__ = ...


# ✍️ TODO: Define Transaction model here (with ForeignKey to Account)
# 日本語訳：ここにTransactionモデルを定義してください（AccountへのForeignKey付き）
# class Transaction(Base):
#     __tablename__ = ...
