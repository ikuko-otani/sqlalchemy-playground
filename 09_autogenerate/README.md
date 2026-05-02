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

## Alembic Commands Used in This Unit

```bash
# Check current revision state in the DB
# DBの現在のrevision状態を確認
alembic current

# Auto-generate a migration from model changes
# モデルの変更差分からmigrationを自動生成
alembic revision --autogenerate -m "<message>"
alembic revision --autogenerate -m "add accounts table"
alembic revision --autogenerate -m "add entries table with FK to accounts"

# Apply all pending migrations
# 未適用のmigrationをすべて適用
alembic upgrade head

# Roll back one migration
# 1つ前のmigrationに戻す
alembic downgrade -1

# Show migration history
# migrationの履歴を表示
alembic history --verbose

# Check if there are unapplied changes (useful in CI)
# 未反映の変更がないか確認（CI/CDで使う）
alembic check
```

### Notes

- Always review generated migration files before applying (`alembic upgrade head`)
- `downgrade()` must be implemented for production rollback
- `alembic check` exits with code 1 if pending changes exist — use in GitHub Actions

## Reference

- [Alembic autogenerate docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
