from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, Session
from app.config.settings import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with Session(engine) as session:
        yield session


