# S-02 — Declarative Mapping (`Mapped[X]`)

## What you learn in this chapter

- SQLAlchemy 2.0 Declarative Mapping with `Mapped[X]` and `mapped_column()`
- `DeclarativeBase` and `registry`
- Optional vs required columns (`Mapped[Optional[str]]`)
- Server defaults vs Python-side defaults
- One-to-many `relationship()` with `back_populates`
- Async engine / session lifecycle (`AsyncSession`, `async_sessionmaker`)
- Observing generated SQL with `echo=True`

## DB Connection

| Item | Value |
|------|-------|
| Host | `localhost` |
| Port | `5432` |
| DB | `ledger_db` |
| User | `ledger` |
| Password | `ledger` |

## Start PostgreSQL

```bash
docker compose up -d postgres
```

## Run the exercise script

```bash
# From the repo root:
python -m 02_declarative-mapping.main
```

## Verify tables in psql

```bash
psql postgresql://ledger:ledger@localhost:5432/ledger_db
\dt
\d accounts
```

## Key concepts for Berlin interviews

- `Mapped[X]` is the 2.0 replacement for `Column()` — always use it in new code
- `expire_on_commit=False` is essential for async to avoid lazy-load errors after commit
- Never mix sync and async sessions
- `echo=True` lets you see real SQL — reviewers love candidates who know the actual queries
