import uvicorn
from fastapi import FastAPI
from database import engine, session_factory, base
from routers import user as user_router

base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the todos API. Create new user and you are ready to go!"}
app.include_router(user_router.router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=2)