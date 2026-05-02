# Chapter A-02: autogenerate and manual adjustment
# Ref: https://alembic.sqlalchemy.org/en/latest/autogenerate.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# PostgreSQL が docker compose up -d postgres で起動していること

# TODO: Define your SQLAlchemy ORM models below using Mapped[X] and mapped_column()
# 以下に Mapped[X] と mapped_column() を使って ORM モデルを定義してください

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Numeric, DateTime, ForeignKey
from datetime import datetime
import decimal


class Base(DeclarativeBase):
    pass


# Step 1: Define Account model here
# Step 1: Account モデルをここに定義する
