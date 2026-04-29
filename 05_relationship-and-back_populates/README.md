# S-05: `relationship()` and `back_populates`

## What you will learn

<!-- 日本語訳：この単元で学ぶこと -->

| Topic | Description |
|---|---|
| `relationship()` | Declare ORM-level associations between models |
| `back_populates` | Keep both sides of a bidirectional relationship in sync |
| `selectinload()` | Eager-load related objects with a second `SELECT … IN (…)` |
| `joinedload()` | Eager-load with a SQL JOIN (best for many-to-one) |
| `lazy="raise"` | Raise immediately if lazy load attempted — useful in async |
| `uselist=False` | One-to-one relationship |
| `expire_on_commit=False` | Prevent lazy load after commit in async sessions |

## N+1 Problem 🔍

If you query 10 users and access `user.posts` in a loop,
SQLAlchemy fires 1 + 10 = **11 queries**. Use `selectinload()` to collapse it to **2 queries**.

<!-- 日本語訳：10件のユーザーをループで取得し user.posts にアクセスすると 1+10=11クエリ発行される。selectinload() を使えば2クエリに削減できる -->

## Flagship connection (payment-ledger-api)

In `payment-ledger-api`, the `Account ↔ Entry` relationship is the core of
double-entry bookkeeping. Each `Entry` has a `debit_account` and a `credit_account`,
both FK-ing into `Account`. This unit teaches exactly how to model that.

<!-- 日本語訳：payment-ledger-api では Account ↔ Entry の関係が複式簿記の核心。本単元はその実装に直結する -->

## Database connection

```bash
# Start PostgreSQL
docker compose up -d postgres

# Connect with psql
psql postgresql://postgres:postgres@localhost:5432/postgres
```

## Run the exercise

```bash
# From repository root
python -m 05_relationship-and-back_populates.main
```

## Alembic migration (Step 4)

```bash
alembic revision --autogenerate -m "add users and posts tables"
alembic upgrade head
alembic downgrade -1  # rollback test
```

## References

- [SQLAlchemy 2.0 — relationship() API](https://docs.sqlalchemy.org/en/20/orm/relationship_api.html)
- [Relationship Loading Techniques](https://docs.sqlalchemy.org/en/20/orm/loading_relationships.html)
- [Async I/O (asyncio) — SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
