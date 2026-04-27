# Chapter S-01: Engine & Connection (async)
# Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
#
# Requires: PostgreSQL running via `docker compose up -d postgres`

# --- Write your model classes below ---
# モデルクラスをここから下に記述

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    def __repr__(self) -> str:
        return f"<Item id={self.id} name={self.name}>"
