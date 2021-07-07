from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def ts_info():
  return {"message": "This route deals with the api to summarize text from a context"}