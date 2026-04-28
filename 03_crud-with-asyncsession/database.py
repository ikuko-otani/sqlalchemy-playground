# Async engine and session factory for S-03
# 日本語訳：S-03用の非同期エンジンとセッションファクトリ

from __future__ import annotations

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# 📋 Copy-paste OK: Change user/password/db to match your compose.yaml
# 日本語訳：コピペOK：compose.yamlに合わせてユーザー/パスワード/DB名を変更してください
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/playground"

# Create async engine
# echo=True prints generated SQL — always use this during learning!
# 日本語訳：echo=True で生成SQLを標準出力に表示 — 学習中は必ず使うこと！
# 💡 Interview tip: echo=True reveals N+1 queries. Use it before any selectinload() optimization.
# 日本語訳：面接TIPS: echo=Trueでいつでもどんなクエリが発行されているか確認できる。
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory — do NOT call Session() directly, use async_sessionmaker
# 日本語訳：セッションファクトリ — Session() を直接呼ばず async_sessionmaker を使う
# 💡 Interview tip: expire_on_commit=False prevents lazy-load errors after commit in async contexts
# 日本語訳：面接TIPS: expire_on_commit=False はcommit後の遅延ロードエラーを防ぐ
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncSession:
    """Dependency for FastAPI — yields a session per request.

    日本語訳：FastAPI依存性注入用 — リクエストごとにセッションを生成して返す。
    """
    # ✍️ TODO: implement using `async with AsyncSessionLocal() as session: yield session`
    # 日本語訳：`async with AsyncSessionLocal() as session: yield session` で実装する
    raise NotImplementedError
