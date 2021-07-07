from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def qg_info():
  return {"message": "This route deals with the api to generate questions and answers from a context"}