from _2_beanie_model import Book, main as init_db
import asyncio


async def insert_book():
    await init_db()
    book = Book(title="1984", author="George Orwell", published_year=1949)
    await book.insert()
    print(f"Inserted book: {book}")


if __name__ == "__main__":
    asyncio.run(insert_book())
