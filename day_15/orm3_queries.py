from datetime import datetime
from pprint import pprint

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

DB_URL = "postgresql+pg8000://pgadmin:passwd!@localhost:5432/blog"
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=engine, cls=Base)


class User(Base):
    __tablename__ = "users"

    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def promote(self):
        self.is_staff = True

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f"username={self.username!r},"
            f"is_staff={self.is_staff},"
            f"created_at={self.created_at}"
            f")"
        )

    def __repr__(self):
        return str(self)


def query_all_users(session: SessionType) -> list[User]:
    users = session.query(User).all()
    print("Received users:", users)
    return users


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)
    session.add(user)
    session.commit()
    print("Saved user:", user)
    return user


def find_user_by_username(session: SessionType, username: str) -> User:
    # user = session.query(User).filter_by(username=username).one()
    # user  = session.query(User).filter_by(username=username).one_or_none()
    user = session.query(User).filter_by(username=username).first()
    print("Found user:", user)
    return user


def find_user_by_id(session: SessionType, id: int) -> User:
    user = session.get(User, id)
    print("Got user:", user)
    return user


def find_users_by_username(session: SessionType, name_part: str) -> list[User]:
    q_users = session.query(User)
    q_users_match_username = q_users.filter(User.username.like(f"%{name_part}%"))
    users = q_users_match_username.all()
    print(f"Found users for {name_part!r}:")
    pprint(users)
    return users


def promote_user(session: SessionType, user: User) -> User:
    print("Before:", user)
    user.promote()
    print("After:", user)

    session.commit()
    print("After commit:", user)
    return user


def main():
    # Base.metadata.create_all()

    session: SessionType = Session()
    # create_user(session, "tom")
    # query_all_users(session)
    user_max = find_user_by_username(session, "max")
    # find_user_by_id(session, 10)
    # find_users_by_username(session, "m")
    promote_user(session, user_max)
    session.close()


if __name__ == "__main__":
    main()
