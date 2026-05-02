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

### Setup

```bash
# Start PostgreSQL
docker compose up -d postgres

# Create the dedicated DB for this unit
psql -h localhost -U postgres -c "CREATE DATABASE playground_a03;"

# Move into the exercise directory
cd 10_upgrade-downgrade-history
```

### Alembic — Core Workflow

```bash
# Check current DB revision (empty = no migrations applied yet)
alembic current

# Generate a migration file from model diff (autogenerate)
alembic revision --autogenerate -m "create accounts table"

# Apply all pending migrations to head
alembic upgrade head

# Roll back one step
alembic downgrade -1

# Roll back to absolute base (undo all migrations)
alembic downgrade base

# Re-apply up to head
alembic upgrade head
```

### Alembic — History & Inspection

```bash
# View full migration history
alembic history

# View with details (revision ID, date, message)
alembic history --verbose

# View a range: from base to head
alembic history -r base:head

# Check current applied revision in DB
alembic current

# List all head revisions (useful when branches exist)
alembic heads

# List branch points
alembic branches
```

### Alembic — Relative Identifiers

```bash
# Advance N steps forward from current
alembic upgrade +2

# Go back N steps from current
alembic downgrade -2

# Upgrade to a specific revision ID
alembic upgrade <revision_id>

# Downgrade to a specific revision ID
alembic downgrade <revision_id>
```

### DB Verification (psql)

```bash
# List all tables
psql -h localhost -U postgres -d playground_a03 -c "\dt"

# Check table schema (columns, types)
psql -h localhost -U postgres -d playground_a03 -c "\d accounts"

# Check alembic_version table (current revision stored here)
psql -h localhost -U postgres -d playground_a03 -c "SELECT * FROM alembic_version;"
```

### Run Demo Script

```bash
# Insert and select Account rows (SQL logged via echo=True)
python main.py
```

### Cleanup

```bash
# Stop PostgreSQL and remove volume (next unit starts clean)
docker compose down -v

# Stop without removing volume (keep learning data)
docker compose down
```
