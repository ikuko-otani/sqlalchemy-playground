# Alembic env.py for Chapter A-01
# Alembic の env.py - migration 実行環境の設定ファイル

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# Import Base and models so that autogenerate can detect all tables.
# autogenerate がすべてのテーブルを検出できるよう Base と models を必ず import する。
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Base
import models  # Required: registers all models into Base.metadata

# models を import しないと autogenerate が空の migration を生成する（よくある落とし穴）

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadata tells autogenerate which tables to track.
# autogenerate がどのテーブルを追跡するかを指定する。
target_metadata = Base.metadata


# SQLを実行せずファイルに書き出す（DBAレビュー用）
# 使いどころ: 本番DBに直接アクセスできない環境での事前確認
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    Offline mode: emits SQL to stdout instead of executing against a live DB.
    オフラインモード - 実DBに接続せずSQLをファイル/標準出力に出力する。
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    Online mode: connects to the DB and executes DDL directly.
    オンラインモード - DBに直接接続してDDLを実行する。（通常の開発・CI）
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
