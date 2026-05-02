# Chapter A-03: upgrade / downgrade / history

## What you learn

- `alembic upgrade head` / `alembic upgrade +N` / relative identifiers
- `alembic downgrade base` / `alembic downgrade -1`
- `alembic history` / `alembic history --verbose` / range slicing
- `alembic current` — confirm DB revision state
- `alembic heads` / `alembic branches`
- Writing correct `upgrade()` and `downgrade()` functions in a migration file
- Role of `alembic_version` table and `down_revision` chain

## DB connection

| Key | Value |
|-----|-------|
| Host | localhost:5432 |
| User | postgres |
| Password | password |
| Database | **playground_a03** |

## Commands

```bash
# Start PostgreSQL
docker compose up -d postgres

# Create the dedicated DB
psql -h localhost -U postgres -c "CREATE DATABASE playground_a03;"

# Apply migrations
alembic upgrade head

# Check current revision
alembic current

# View history
alembic history --verbose

# Roll back one step
alembic downgrade -1

# Run demo insert/select
python main.py
```
