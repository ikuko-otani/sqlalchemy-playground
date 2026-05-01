# Chapter A-01: Alembic Init & First Migration
# Ref: https://alembic.sqlalchemy.org/en/latest/tutorial.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# Database: playground_a01

from sqlalchemy import Numeric, String, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

# TODO: Define your model here (Step 1 in the study guide)
class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
