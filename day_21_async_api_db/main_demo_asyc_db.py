import asyncio
import logging
from pprint import pprint
from typing import List

from sqlalchemy import select, desc
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, noload

import config
from models import User, Author, Post, Tag
from models.base import Base

log = logging.getLogger(__name__)

async_engine = create_async_engine(config.SQLALCHEMY_ASYNC_DB_URI, echo=True)
async_session = sessionmanker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    print("create user:", user)
    session.add(user)

    await session.commit()
    print("saved user:", user)

    await session.refresh(user)
    print("refreshed user:", user)

    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    # get uses cache!!!
    user = await session.get(User, user_id)
    # user = await session.get(User, user_id)
    # user = await session.get(User, 2)
    print("user", user)
    return user


async def create_author_for_user(
    session: AsyncSession, username: str, author_name: str
) -> Author:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User = result.scalar_one()
    author = Author(name=author_name, user=user)
    session.add(author)
    print(f"create author {author} for user {user}.")
    await session.commit()
    print(f"create author {author} for user {user}.")
    return author


async def create_posts_for_user(
    session: AsyncSession, username: str, *posts_titles: str
) -> List[Post]:
    posts = []

    stmt = select(Author).join(Author.user).where(User.username == username)
    result: Result = await session.execute(stmt)
    author: Author = result.scalar_one()
    print(f"fetched author for user {username!r}: {author!r}")
    for title in posts_titles:
        post = Post(title=title, author=author)
        posts.append(post)
        # session.add(post)
    session.add_all(posts)

    await session.commit()

    print("created posts:")
    pprint(posts)
    return posts


async def create_tags(session: AsyncSession, *tags_names: str) -> List[Tag]:
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    await session.commit()
    print("created tags", tags)
    return tags


async def create_posts_tags_associations(session: AsyncSession):
    stmt_tags = select(Tag)
    result: Result = await session.execute(stmt_tags)
    tags: List[Tag] = list(result.scalars())

    # stmt_posts = select(Post).filter().options(noload(Post.tags))
    stmt_posts = select(Post).filter().options(selectinload(Post.tags))
    result: Result = await session.execute(stmt_posts)
    posts: List[Post] = list(result.scalars())

    print("tags:", tags)
    print("posts:")
    pprint(posts)

    for post in posts:
        print("* process post", post, "with tags:", post.tags)
        for tag in tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)
                print("added tag", tag)

    await session.commit()


async def fetch_posts_with_tags_and_authors(session: AsyncSession):
    stmt_posts = (
        select(Post)
        .filter()
        .options(
            joinedload(Post.author).joinedload(Author.user), selectinload(Post.tags)
        )
        .order_by(desc(Post.id))
    )
    result: Result = await session.execute(stmt_posts)
    posts: List[Post] = list(result.scalars())

    for post in posts:
        print("-- post:", post)
        print("   by author", post.author)
        print("   and user", post.author.user)
        print("   tags", post.tags)


async def main_async():
    # await create_tables()
    async with async_session() as session:  # type: AsyncSession
        # user = await create_user(session, "tom")
        # user = await get_user_by_id(session, 2)
        # author = await create_author_for_user(session, user.username, "tom ford")
        # posts = await create_posts_for_user(
        #     session, user.username, "Django news", "SQLAlchemy async", "Flask news"
        # )
        # tags = await create_tags(
        #     session, "news", "async", "django", "flask", "sqlalchemy"
        # )
        # await create_posts_tags_associations(session)
        await fetch_posts_with_tags_and_authors(session)


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
