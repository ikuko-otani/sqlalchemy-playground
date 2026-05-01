# Chapter A-01: Alembic Init & First Migration

## What you will learn

- How `alembic init` creates the migration environment
- The role of `alembic.ini`, `env.py`, `script.py.mako`, and `versions/`
- `run_migrations_online()` vs `run_migrations_offline()`
- `alembic revision --autogenerate` and when it is **not** enough
- `alembic upgrade head` / `alembic downgrade -1`
- The `alembic_version` table and its role in tracking state

## Reference

<https://alembic.sqlalchemy.org/en/latest/tutorial.html>

## Database connection

| Item        | Value                                                                   |
|-------------|-------------------------------------------------------------------------|
| Driver (async / runtime) | `postgresql+asyncpg://postgres:password@localhost:5432/playground_a01` |
| Driver (sync / alembic)  | `postgresql+psycopg2://postgres:password@localhost:5432/playground_a01` |
| DB name     | `playground_a01`                                                        |

## Quick start

```bash
# 1. Start PostgreSQL
docker compose up -d postgres

# 2. Create the dedicated database
psql -h localhost -U postgres -c "CREATE DATABASE playground_a01;"

# 3. Apply migrations
cd 08_init-and-migration
alembic upgrade head

# 4. Run the verification script
python main.py
```
