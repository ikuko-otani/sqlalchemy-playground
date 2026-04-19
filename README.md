![Status](https://img.shields.io/badge/status-active-success?style=flat-square) ![Mode](https://img.shields.io/badge/mode-minimum_viable-blue?style=flat-square) ![Focus](https://img.shields.io/badge/current_focus-backend_flagship-success?style=flat-square)

# sqlalchemy-playground

My SQLAlchemy 2.0 (async ORM) + Alembic learning playground — the persistence layer for my flagship project [`payment-ledger-api`](https://github.com/ikuko-otani).

## 🎯 Why this repo exists

Async ORM usage with PostgreSQL is a core skill for modern Python backends at my target employers (HelloFresh, Revolut, Prima). SQLAlchemy 2.0's unified API + `AsyncSession` is the stack I will use in the flagship, so this repo is where I build confidence with the declarative style, relationships, and Alembic migrations in isolation.

## 📅 Learning window

**2026-05-03 → 2026-05-09** (Week 3 of the 73-day sprint). See `learning_plan_minimum_viable.md` v3 dated 2026-04-19.

## 🗂 Planned units

### SQLAlchemy 2.0 ORM
- [ ] 01 Declarative `Base` + first model
- [ ] 02 `AsyncEngine`, `async_sessionmaker`, `AsyncSession` lifecycle
- [ ] 03 `select()` + `scalars()` for CRUD
- [ ] 04 Relationships: `Mapped`, `relationship()`, eager vs lazy loading
- [ ] 05 Transactions and `begin_nested()` savepoints

### Alembic (migrations)
- [ ] 06 Alembic init + environment config for async
- [ ] 07 `alembic revision --autogenerate` and reviewing generated ops
- [ ] 08 Upgrade / downgrade cycle
- [ ] 09 Data migration (not just schema)

## 🔗 Related repositories

- [`payment-ledger-api`](https://github.com/ikuko-otani) — flagship project (target: ship by 2026-06)
- [`python-playground`](https://github.com/ikuko-otani/python-playground) — Python foundation
- [`docker-playground`](https://github.com/ikuko-otani/docker-playground) — containerization
- [`fastapi-playground`](https://github.com/ikuko-otani/fastapi-playground) — API framework
- [`pytest-playground`](https://github.com/ikuko-otani/pytest-playground) — testing discipline

## 📚 References

- [SQLAlchemy 2.0 Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [SQLAlchemy Async ORM Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
