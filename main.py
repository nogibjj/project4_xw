from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List
from pydantic import BaseModel

app = FastAPI() 


class Book(BaseModel):
    name: str
    writer: str
    description: str


store_booklist = []

@app.get("/") 
async def root():
    return {"message": "Hello Project 4 This is a book library. Add/Read/Delete/Update the book you like"}

# create
@app.post("/add/")
async def create_book(book: Book):
    store_booklist.append(book)
    return book


# read
@app.get("/getall/", response_model=List[Book])
async def get_all_books():
    return store_booklist


# delete
@app.delete("/delete/{name}")
async def delete_book(name: str):
    for i, x in enumerate(store_booklist):
        if x.name == name:
            obj = store_booklist[i]
            store_booklist.pop(i)
            return obj

    raise HTTPException(status_code=404, detail="ook Not Found")


# update
@app.put("/update/{name}")
async def update_book(name: str, book: Book):
    for i, x in enumerate(store_booklist):
        if x.name == name:
            store_booklist[i] = book
            return store_booklist[i]

    raise HTTPException(status_code=404, detail="Book Not Found")



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")