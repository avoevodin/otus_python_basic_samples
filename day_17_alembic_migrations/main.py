from __future__ import annotations
from pprint import pprint
from typing import Optional, List

from sqlalchemy.orm import Session as SessionType, joinedload

from models import User  # , Author, Post
from models.base import Session


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)
    print("Create user", user)
    session.add(user)
    session.commit()

    print("Created user", user)
    return user


def create_author_for_user(
    session: SessionType, user: User, author_name: str
) -> Author:
    author = Author(name=author_name, user=user)
    # author = Author(name=author_name, user_id=user.id)
    print(
        "Create author:",
        author,
    )
    session.add(author)
    session.commit()
    print("Created author:", author)


def fetch_author_by_id(session: SessionType, author_id: int) -> Author:
    author = session.get(Author, author_id, options=(joinedload(Author.user),))
    print(author)
    print(author.user)
    return author


def fetch_user_with_author_by_username(session: SessionType, username: str) -> User:
    user: User = (
        session.query(User)
        .filter_by(username=username)
        .options(joinedload(User.author))
        .one()
    )

    print(user)
    print(user.author)


def find_user_by_author_name(session: SessionType, author_name: str) -> Optional[User]:
    user = (
        session.query(User)
        .join(Author)
        # .join(Author, Author.user_id == User.id)
        .filter(Author.name == author_name)
        .options(joinedload(User.author, innerjoin=True))
        .first()
    )
    print("Found user", user)
    if user:
        print("User's author:", user.author)
    return user


def create_posts_for_author(
    session: SessionType, author: Author, titles: List[str]
) -> List[Post]:

    posts = []
    for title in titles:
        post = Post(title=title, author=author)
        posts.append(post)
        session.add(post)

    session.commit()

    print("Created posts:")
    pprint(posts)

    return posts


def find_user_with_author_and_posts(session: SessionType, username: str):
    user = (
        session.query(User)
        # .filter(User.username == username)
        .filter_by(username=username)
        .options(
            # joinedload(User.author),
            # joinedload(User.profile),
            joinedload(User.author).joinedload(Author.posts),
        )
        .one_or_none()
    )
    if not user:
        print("user not found")
        return

    print("user:", user)
    if user.author:
        print("author:", user.author)
        print("posts:")
        pprint(user.author.posts)


def main():
    Base.metadata.create_all()
    return

    session: SessionType = Session()
    # user_john = create_user(session, "john")
    # user_tom = create_user(session, "tom")
    # author_tom = create_author_for_user(session, user_tom, "tom smith")
    # author: Author = fetch_author_by_id(session, 1)
    # user_tom = fetch_user_with_author_by_username(session, "tom")
    # user_john = fetch_user_with_author_by_username(session, "john")
    # author = find_user_by_author_name(session, "tom smith")
    # find_user_by_author_name(session, "tom sm")
    # create_posts_for_author(session, author, ["Django intro", "Flask lesson"])
    # find_user_with_author_and_posts(session, "tom")
    # find_user_with_author_and_posts(session, "to")
    # find_user_with_author_and_posts(session, "john")
    session.close()


if __name__ == "__main__":
    main()
