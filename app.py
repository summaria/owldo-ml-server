import uvicorn
from fastapi import FastAPI, Request
from routers import v1
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse('test.html', context={'request': request})

@app.get('/ping')
def ping():
    return {'message': 'pong'}


app.include_router(
    v1.router,
    prefix="/api/v1"
)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
