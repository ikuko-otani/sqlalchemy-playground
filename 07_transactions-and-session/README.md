# Chapter 07: Transactions & Session.begin()

## What you will learn

- How `Session.begin()` works as a context manager
- The difference between `session.flush()` and `session.commit()`
- Nested transactions with `session.begin_nested()` (SAVEPOINT)
- Transaction rollback patterns and error handling
- How `AsyncSession` manages transaction lifecycle
- Why `expire_on_commit=False` matters in async contexts

## Reference

<https://docs.sqlalchemy.org/en/20/orm/session_transaction.html>

## DB Connection

| Item | Value |
|------|-------|
| Host | `localhost` |
| Port | `5432` |
| User | `postgres` |
| Password | `password` |
| Database | `playground_s07` |

## Quick Start

```bash
# 1. Start PostgreSQL
docker compose up -d postgres

# 2. Create the dedicated database
psql postgresql://postgres:password@localhost:5432/postgres -c "CREATE DATABASE playground_s07;"

# 3. Apply migrations
cd 07_transactions-and-session
alembic upgrade head

# 4. Run exercises
python main.py
```
