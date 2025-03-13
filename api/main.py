from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Book
from .crud import create_book, get_books, get_book, update_book, delete_book
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    description: str

class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    description: str

@app.post("/books/")
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}")
def update_existing_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    updated_book = update_book(db, book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}")
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = delete_book(db, book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
