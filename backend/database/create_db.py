from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "skincare.db"
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Product(Base):
    __tablename__="all_products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)


class Ingredient(Base):
    __tablename__="all_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class ProductIngredient(Base):
    __tablename__="product_ingredients"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("all_products.id"))
    ingredient_id = Column(Integer, ForeignKey("all_ingredients.id"))

Base.metadata.create_all(engine)
