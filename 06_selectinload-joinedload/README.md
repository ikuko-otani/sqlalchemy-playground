# Chapter 06 — N+1 Problem & selectinload() / joinedload()

## What you learn

- Why **N+1 queries** happen with default lazy loading in an async context
- How `selectinload()` solves N+1 by issuing a second `IN` query
- How `joinedload()` solves N+1 by issuing a `JOIN` query
- When to choose `selectinload` vs `joinedload`
- How `lazy='raise'` enforces eager-load discipline

## DB Connection

| key | value |
|-----|-------|
| host | localhost |
| port | 5432 |
| user | postgres |
| password | password |
| database | **playground_s06** |

## Run

```bash
# Start PostgreSQL
docker compose up -d postgres

# Create dedicated DB
psql postgresql://postgres:password@localhost:5432/postgres -c "CREATE DATABASE playground_s06;"

# Apply Alembic migrations (tables are created via Alembic only, NOT Base.metadata.create_all)
alembic upgrade head

# Run exercise script
python 06_selectinload-joinedload/main.py
```

## References

- [SQLAlchemy 2.0 — Relationship Loading Techniques](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html)
- [SQLAlchemy 2.0 — selectinload](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html#select-in-loading)
- [SQLAlchemy 2.0 — joinedload](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html#joined-loading)
