import logging
from pprint import pprint
from typing import Optional, List

from sqlalchemy.orm import Session as SessionType, joinedload, selectinload
from sqlalchemy.orm.exc import NoResultFound

from models import User, Author, Post, Tag
from models.base import Session

log = logging.getLogger(__name__)


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
    return author


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
    return user


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


def find_matching_usernames(session: SessionType, username_part: str) -> List[User]:
    users: List[User] = (
        session.query(User).filter(User.username.ilike(f"%{username_part}%")).all()
    )
    print("found users:")
    pprint(users)
    return users


def create_tags(session: SessionType, *tags_names: str):
    tags = []

    for tag_name in tags_names:
        tag = Tag(name=tag_name)
        session.add(tag)
        tags.append(tag)

    session.commit()
    print("created tags:")
    pprint(tags)


def fetch_all_tags(session: SessionType) -> List[Tag]:
    tags = session.query(Tag).all()
    print("Tags:")
    pprint(tags)
    return tags


def assign_tags_to_posts(session: SessionType):
    tags = fetch_all_tags(session)
    posts: list[Post] = session.query(Post).all()

    tag_python = next(filter(lambda t: t.name == "python", tags), None)
    for post in posts:
        for tag in tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)
        if tag_python and tag_python not in post.tags:
            post.tags.append(tag_python)

    session.commit()


def fetch_posts_with_tags(session: SessionType) -> List[Post]:
    posts = session.query(Post).options(joinedload(Post.tags)).all()
    for post in posts:
        print("post", post)
        print("--tags:", post.tags)
    return posts


def fetch_posts_with_tags_selectinload(session: SessionType) -> List[Post]:
    """
    selectinload is able for async.
    :param session:
    :return:
    """
    posts = session.query(Post).options(selectinload(Post.tags)).all()
    for post in posts:
        print("post", post)
        print("--tags:", post.tags)
    return posts


def fetch_tags_with_posts(session: SessionType) -> List[Tag]:
    tags: list[Tag] = session.query(Tag).options(joinedload(Tag.posts)).all()
    for tag in tags:
        print("tag", tag)
        print("--posts:")
        pprint(tag.posts)
    return tags


def assign_and_delete_tag(session: SessionType, tag_name: str):
    post: Post = session.query(Post).options(joinedload(Post.tags)).first()
    if not post:
        raise ValueError("post not found")

    print(">>>> post to update:")
    print("--post", post.id, post.title)
    print("...post tags:", post.tags)

    tag: Tag = session.query(Tag).filter_by(name=tag_name).one_or_none()
    if not tag:
        tag = Tag(name=tag_name)
        # session.add(tag)
        # session.commit()

    post.tags.append(tag)
    session.commit()

    print(">>>> added tag to post:")
    print("--post", post.id, post.title)
    print("...post tags:", post.tags)

    print(">>>> remove tag:")
    post.tags.remove(tag)
    session.commit()

    print("--post", post.id, post.title)
    print("...post tags:", post.tags)


def find_user_by_author_post_tag(session: SessionType, tag_name: str) -> List[User]:
    users: List[User] = (
        session.query(User)
        .join(User.author)
        .join(Author.posts)
        .join(Post.tags)
        .filter(Tag.name == tag_name)
        .options(joinedload(User.author).joinedload(Author.posts).joinedload(Post.tags))
        .all()
    )

    print("found users:")
    for user in users:
        print(">>> user:", user)
        print("   - author:", user.author)
        print("posts:")
        for post in user.author.posts:
            print("  > post:", post.id, post.title)
            print("  .. tags:", post.tags)

    return users


def main():
    session: SessionType = Session()
    # user_tom = create_user(session, "tom")
    # user_john = create_user(session, "john")
    # author_tom = create_author_for_user(session, user_tom, "tom smith")
    # author: Author = fetch_author_by_id(session, 1)
    # us er_tom = fetch_user_with_author_by_username(session, "tom")
    # try:
    #     fetch_user_with_author_by_username(session, "todm")
    # except NoResultFound:
    #     log.info("No user todm")
    # user_john = fetch_user_with_author_by_username(session, "john")
    # author = create_author_for_user(session, user_john, "john dorian")
    # find_user_by_author_name(session, "tom smith")
    # find_user_by_author_name(session, "tom sm")
    # create_posts_for_author(session, author, ["Django intro", "Flask lesson"])
    # find_user_with_author_and_posts(session, "tom")
    # find_user_with_author_and_posts(session, "to")
    # find_user_with_author_and_posts(session, "john")
    # find_matching_usernames(session, "o")
    # create_posts_for_author(
    #     session,
    #     user_john.author,
    #     ["Django lesson", "SQLAlchemy lesson", "Python News"],
    # )
    # create_tags(session, "python", "news", "django", "flask", "sqlalchemy")
    # fetch_all_tags(session)
    # assign_tags_to_posts(session)
    # fetch_posts_with_tags(session)
    # fetch_posts_with_tags_selectinload(session)
    assign_and_delete_tag(session, "hello")
    # find_user_by_author_post_tag(session, "python")
    session.close()


if __name__ == "__main__":
    main()
