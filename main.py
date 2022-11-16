from fastapi import FastAPI

# 创建 api 对象
app = FastAPI() 

# 根路由
@app.get("/") 
async def root():
    return {"fastapi": "fastapi"}

@app.get("/say/{data}")
async def say(data: str,q: int = None):
    return {"data": data, "q": q}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item