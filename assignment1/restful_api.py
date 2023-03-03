from fastapi import FastAPI
from ner import SpacyDocument
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str


@app.get("/api")
def get_api_info():
    return {"info": "This is a RESTful API for processing text with spaCy NER"}


@app.post("/api")
def process_text(item: Item):
    doc = SpacyDocument(item.text)
    markup = doc.get_entities_with_markup()
    return {"markup": markup}