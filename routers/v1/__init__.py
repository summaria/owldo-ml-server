from fastapi import APIRouter
from .qg_router import router as qg_router
from .ts_router import router as ts_router

router = APIRouter()

# router.include_router(
#     qg_router,
#     prefix='/qg',
#     tags=['question-generation'],
# );

router.include_router(
    ts_router,
    prefix='/ts',
    tags=['text-summarization'],
)
