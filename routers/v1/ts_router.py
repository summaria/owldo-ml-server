from fastapi import APIRouter
from summarization import MODEL

from typing import Optional
from pydantic import BaseModel


router = APIRouter()


@router.get('/')
async def ts_info():
    return {"message": "This route deals with the api to summarize text from a context"}


class Text(BaseModel):
    text: str
    extent:int


@router.post('/generate/')
def generate_summary(textObj: Text):
    return {
        "data": [ MODEL.generate_summary(textObj.text, textObj.extent) ]
    }
