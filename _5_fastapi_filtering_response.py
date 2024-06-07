from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel
from _2_beanie_model import Book, main as init_db


class BookResponseModel(BaseModel):
    title: str
    author: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/books", response_model=list[BookResponseModel])
async def get_books_by_author(author: str):
    books = await Book.find(Book.author == author).to_list()
    return books


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
