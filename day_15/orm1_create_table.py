from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Boolean

DB_URL = "sqlite:///example-01.db"
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True),
    Column("is_staff", Boolean, default=False, nullable=False),
)

if __name__ == "__main__":
    # print(engine, [engine])
    # print(users_table, [users_table])
    metadata.create_all(bind=engine)
