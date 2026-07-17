from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, func, select
from datetime import datetime
from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True)
    username = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    language = Column(String(10), default=None, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_blocked = Column(Boolean, default=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_or_create_user(user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if not user:
            user = User(id=user_id, username=username, first_name=first_name, last_name=last_name)
            session.add(user)
            await session.commit()
        return user

async def set_user_language(user_id: int, lang: str):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.language = lang
            await session.commit()

async def get_user_language(user_id: int) -> str | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        return user.language if user else None

async def get_all_users() -> list[User]:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.is_blocked == False))
        return list(result.scalars().all())


async def get_users_by_audience(audience: str) -> list[User]:
    async with async_session() as session:
        query = select(User).where(User.is_blocked == False)
        if audience != 'all':
            query = query.where(User.language == audience)
        result = await session.execute(query)
        return list(result.scalars().all())


async def count_users_by_audience(audience: str) -> int:
    async with async_session() as session:
        query = select(func.count(User.id)).where(User.is_blocked == False)
        if audience != 'all':
            query = query.where(User.language == audience)
        result = await session.execute(query)
        return result.scalar() or 0


async def get_language_stats() -> dict:
    async with async_session() as session:
        stats = {}
        for lang in ('ru', 'en', 'ka'):
            result = await session.execute(
                select(func.count(User.id)).where(
                    User.is_blocked == False,
                    User.language == lang,
                )
            )
            stats[lang] = result.scalar() or 0

        result = await session.execute(
            select(func.count(User.id)).where(
                User.is_blocked == False,
                User.language.is_(None),
            )
        )
        stats['none'] = result.scalar() or 0
        return stats

async def get_stats() -> dict:
    async with async_session() as session:
        total = await session.execute(select(func.count(User.id)))
        today = await session.execute(
            select(func.count(User.id)).where(func.date(User.created_at) == func.date(func.now()))
        )
        return {
            'total': total.scalar() or 0,
            'today': today.scalar() or 0
        }

async def mark_user_blocked(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.is_blocked = True
            await session.commit()
