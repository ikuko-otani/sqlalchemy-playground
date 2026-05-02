# A-02: autogenerate and Manual Adjustment

## What you learn in this chapter

- How `alembic revision --autogenerate` compares ORM metadata with the live DB
- What autogenerate **can** and **cannot** detect (e.g., CHECK constraints, partial indexes)
- How to manually review and adjust generated migration files
- The role of `target_metadata` in `env.py`
- How `alembic upgrade head` / `alembic downgrade -1` work
- The `alembic_version` table and its role in tracking state

## Prerequisites

- Alembic A-01 (init and basic migration) completed
- Docker Compose with PostgreSQL 16 running

## Database

| Item | Value |
|------|-------|
| DB name | `playground_a02` |
| Host | `localhost:5432` |
| User | `postgres` |
| Password | `password` |
| Async URL | `postgresql+asyncpg://postgres:password@localhost:5432/playground_a02` |
| Alembic URL | `postgresql+psycopg2://postgres:password@localhost:5432/playground_a02` |

## Quick Start

```bash
# 1. Start PostgreSQL
docker compose up -d postgres

# 2. Create the dedicated DB
psql -h localhost -U postgres -c "CREATE DATABASE playground_a02;"

# 3. Apply migrations
cd 09_autogenerate
alembic upgrade head

# 4. Run main script
python main.py
```

## Reference

- [Alembic autogenerate docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
