import uvicorn
from fastapi import FastAPI
from routers import v1

app = FastAPI()

@app.get("/")
def index():
    return { "message" : "Server is running successfully"}

@app.get('/ping')
def ping():
    return {'message': 'pong'}

app.include_router(
    v1.router,
    prefix="/api/v1"
);

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
