from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


class Product(Base):
    """Model representing products sold in a store"""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    quantity_sold = Column(Integer, nullable=False, default=0)
    revenue = Column(Float, nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, qty={self.quantity_sold})>"


def get_engine():
    """Create and return a database engine"""
    user = os.getenv('METABASE_USER')
    password = os.getenv('METABASE_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db = os.getenv('METABASE_DB')

    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(connection_string, echo=True)


def get_session():
    """Create and return a database session"""
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
