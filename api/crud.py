from sqlalchemy.orm import Session
from . import models

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, title: str, author: str, description: str):
    book = models.Book(title=title, author=author, description=description)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, title: str, author: str, description: str):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.title = title
        book.author = author
        book.description = description
        db.commit()
        db.refresh(book)
        return book
    return None

def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return None
