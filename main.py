from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI() 


class Book(BaseModel):
    name: str
    writer: str
    price: float
    description: str

booklist = []

@app.get("/") 
async def root():
    return {"message": "Hello, welcome to the electronic library. You can Search/Read/Add the book here"}


# See booklist
@app.get("/booklist/", response_model=List[Book])
async def get_booklist():
    return booklist

# Add
@app.post("/add/")
async def add_book(book: Book):
    booklist.append(book)
    return book

# Delete
@app.delete("/delete/{name}/{writer}")
async def delete_book(name: str, writer: str):
    for i, x in enumerate(booklist):
        if x.name == name and x.writer == writer:
            obj = booklist[i]
            booklist.pop(i)
            return obj

# Search
@app.get("/search/{keyword}")
async def search_book(keyword: str):
    for i, x in enumerate(booklist):
        if x.name == keyword or x.writer == keyword or x.description == keyword:
            obj = booklist[i]
            return obj


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")