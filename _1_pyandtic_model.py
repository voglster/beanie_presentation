from pprint import pprint

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    published_year: int


if __name__ == "__main__":
    book = Book(title="1984", author="George Orwell", published_year=1949)
    print(book)
    print(id(book))
    pprint(book.model_dump())

    data = {"author": "George Orwell", "published_year": "1949.5", "title": "1984"}
    book2 = Book.model_validate(data)
    print(book2)
    print(id(book2))
