from typing import Annotated

from beanie import Document, init_beanie, Indexed
import motor.motor_asyncio


class Book(Document):
    title: Annotated[str, Indexed(unique=True)]
    author: str
    published_year: int


async def main():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    database = client["pythoneers"]
    await init_beanie(database, document_models=[Book])

    # just deleting so we can start with an empty db
    await Book.delete_all()

    book = Book(title="1984", author="George Orwell", published_year=1949)

    await book.insert()
    book2 = Book(title="Code Red", author="George Orwell", published_year=1949)
    await book2.insert()
    print(book2)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
