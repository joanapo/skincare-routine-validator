from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database.create_db import SessionLocal, Product, Ingredient, ProductIngredient
from .models.products import AddProductModel, AddProductResponseModel

app = FastAPI(title="Intergration with SQL")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
async def create_product(product: AddProductModel, db: Session = Depends(get_db)):
    if db.query(Product).filter(Product.name == product.name).first():
        raise HTTPException(status_code=400, detail="Product already exists!")

    new_product = Product()
    new_product.name = product.name.strip()
    new_product.category = product.category
    new_product.type = product.type

    db.add(new_product)
    db.flush()  # assigns new_product.id without committing yet

    for ingredient_name in product.ingredients:
        ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient_name).first()

        if not ingredient:
            ingredient = Ingredient(name=ingredient_name)
            db.add(ingredient)
            db.flush()  # assigns ingredient.id

        new_product_ingredient = ProductIngredient()
        new_product_ingredient.product_id = new_product.id
        new_product_ingredient.ingredient_id = ingredient.id
        db.add(new_product_ingredient)

    db.commit()
    db.refresh(new_product)

    return new_product