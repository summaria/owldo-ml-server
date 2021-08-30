from fastapi import APIRouter
# from question_generation import MODEL, MODEL_MCQ

from typing import Optional
from pydantic import BaseModel

router = APIRouter()


@router.get('/')
async def qg_info():
    return {"message": "This route deals with the api to generate questions and answers from a context"}


class Text(BaseModel):
    text: str


# @router.post('/generate/')
# def generate_questions(text: Text):
#     return {
#         "data": MODEL.generate_questions(text.text)
#     }

# @router.post('/generate-mcq/')
# def generate_mcq_questions(text: Text):
#   return {
#     "data": MODEL_MCQ.generate(text.text)
#   }
