# Chapter A-01: Alembic Init & First Migration
# Ref: https://alembic.sqlalchemy.org/en/latest/tutorial.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`
# Database: playground_a01

from sqlalchemy.orm import Mapped, mapped_column
from database import Base

# TODO: Define your model here (Step 1 in the study guide)
# Example: class LedgerEntry(Base): ...
