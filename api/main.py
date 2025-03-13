from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, crud

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/")
def create_book(title: str, author: str, description: str, db: Session = Depends(get_db)):
    return crud.create_book(db, title, author, description)

@app.put("/books/{book_id}")
def update_book(book_id: int, title: str, author: str, description: str, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, title, author, description)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
