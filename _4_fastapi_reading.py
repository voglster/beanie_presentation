from contextlib import asynccontextmanager

from fastapi import FastAPI
from _2_beanie_model import Book, main as init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/books")
async def get_books():
    books = await Book.find_all().to_list()
    return books


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
