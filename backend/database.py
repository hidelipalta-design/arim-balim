from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os
from dotenv import load_dotenv

load_dotenv()

# Veritabanı URL'si
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./test.db"  # Varsayılan: SQLite
)

# Engine oluştur
if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı bağlantısı için dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
