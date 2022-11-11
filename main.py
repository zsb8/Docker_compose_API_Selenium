import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from match import get_price
app = FastAPI()


class Item(BaseModel):
    expiry_date: str
    birthday: str
    effective_date: str


@app.post("/get_price")
async def update_item(item: Item):
    expiry_date = item.expiry_date
    birthday = item.birthday
    effective_date = item.effective_date
    response = get_price.main(expiry_date, birthday, effective_date)
    result = {
        "Expiry_date_input": expiry_date,
        "Birthday_input": birthday,
        "Effective_date_input": effective_date,
        "Package_input": "all_inclusive",
        "Res": response
    }
    if response:
        results = {
            "Results": result
        }
    else:
        results = {
            "Results": "Failed."
        }
    return results


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

