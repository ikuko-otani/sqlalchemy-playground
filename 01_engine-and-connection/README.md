# S-01: Engine & Connection (async)

## What you learn

- How to create an `AsyncEngine` with `create_async_engine()`
- How to build a session factory with `async_sessionmaker`
- The lifecycle of an `AsyncSession` (begin → execute → commit/rollback → close)
- SQLAlchemy 2.0 style: `Mapped[X]` + `mapped_column()`
- Observing generated SQL with `echo=True`
- Difference between `session.flush()` and `session.commit()`

## DB Connection Info

| Key      | Value                                        |
|----------|----------------------------------------------|
| Host     | `localhost`                                  |
| Port     | `5432`                                       |
| DB       | `ledger`                                     |
| User     | `ledger`                                     |
| Password | `ledger`                                     |
| URL      | `postgresql+asyncpg://ledger:ledger@localhost:5432/ledger` |

## Start PostgreSQL

```bash
# From repo root
docker compose up -d postgres
```

## Run the exercise

```bash
pip install sqlalchemy asyncpg
python 01_engine-and-connection/main.py
```

## Verify tables (psql)

```bash
psql postgresql://ledger:ledger@localhost:5432/ledger -c "\dt"
```

## Ref

- https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
