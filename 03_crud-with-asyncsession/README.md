# S-03: CRUD with AsyncSession

## 何を学ぶか / What you'll learn

| Topic | SQLAlchemy API |
|---|---|
| モデル定義 | `DeclarativeBase`, `Mapped[X]`, `mapped_column()` |
| リレーション | `relationship()`, `back_populates`, `ForeignKey` |
| セッション操作 | `AsyncSession`, `session.add()`, `session.get()`, `session.delete()` |
| クエリ構文 | `select()`, `session.execute()`, `.scalars()`, `.all()` |
| トランザクション | `session.begin()`, `session.commit()`, `session.flush()` |
| N+1対策 | `selectinload()`, `joinedload()` |
| テーブル作成 | `Base.metadata.create_all` (開発用) / Alembic (本番用) |

## DB接続情報 / DB Connection Info

```
Host:     localhost
Port:     5432
Database: playground
User:     postgres
Password: postgres
```

> `compose.yaml` は `sqlalchemy-playground/` ルートにあります。

## 実行コマンド / Run Commands

```bash
# 1. Start PostgreSQL
docker compose up -d postgres

# 2. Install dependencies (first time)
pip install sqlalchemy[asyncio] asyncpg alembic psycopg2-binary

# 3. Run the exercise
cd sqlalchemy-playground
python -m 03_crud-with-asyncsession.main

# 4. Inspect in psql
psql -h localhost -U postgres -d playground
\dt
SELECT * FROM accounts;
SELECT * FROM journal_entries;

# 5. Stop (keep data)
docker compose stop
# or remove volumes
docker compose down -v
```

## 💡 面接で聞かれやすいポイント / Interview Hot Spots

- `flush()` vs `commit()` の違い
- `expire_on_commit=False` を async で使う理由
- N+1 問題と `selectinload()` による解決
- Identity Map とは何か
- `Query` API (1.x) が非推奨になった理由と `select()` (2.0) への移行
- `session.begin()` のコンテキストマネージャとトランザクション境界

## ファイル構成 / File Structure

```
03_crud-with-asyncsession/
├── models.py      # ORM model definitions (Account, JournalEntry)
├── database.py    # Async engine + session factory
├── main.py        # Exercise runner (insert / query / update / delete)
└── README.md      # This file
```
