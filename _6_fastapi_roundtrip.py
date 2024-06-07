# insert_update.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from _2_beanie_model import Book, main as init_db
import asyncio
from contextlib import asynccontextmanager


class BookCreateModel(BaseModel):
    title: str
    author: str
    published_year: int


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/books", response_model=Book)
async def create_book(book: BookCreateModel):
    book_obj = Book(**book.dict())
    await book_obj.insert()
    return book_obj


@app.get("/books", response_model=list[Book])
async def get_books():
    books = await Book.find_all().to_list()
    return books


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: BookCreateModel):
    book_obj = await Book.get(book_id)
    if not book_obj:
        raise HTTPException(status_code=404, detail="Book not found")
    book_obj.title = book.title
    book_obj.author = book.author
    book_obj.published_year = book.published_year
    await book_obj.save()
    return book_obj


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
