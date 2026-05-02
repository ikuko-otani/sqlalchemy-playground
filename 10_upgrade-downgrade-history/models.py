# Chapter A-03: upgrade / downgrade / history
# Ref: https://alembic.sqlalchemy.org/en/latest/tutorial.html#downgrade
#
# Requires: PostgreSQL running via `docker compose up -d postgres`

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    account_type: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"<Account  id={self.id} name={self.name} type={self.account_type}>"
