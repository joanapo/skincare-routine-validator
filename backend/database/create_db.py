from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
engine = create_engine("sqlite:///skincare.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Products(Base):
    __tablename__="all_products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)


class Ingredients(Base):
    __tablename__="all_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class ProductIngredients(Base):
    __tablename__="product_ingredients"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("all_products.id"))
    ingredient_id = Column(Integer, ForeignKey("all_ingredients.id"))

Base.metadata.create_all(engine)
