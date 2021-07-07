import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return { "message" : "Server is running successfully"}

@app.get('/ping')
def get_name():
    return {'message': 'pong'}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
