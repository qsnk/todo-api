import uvicorn
from fastapi import FastAPI
from database import engine, session_factory, base
from routers import user as user_router
from routers import token as token_router
from routers import todo as todo_router
from routers import permission as permission_router

base.metadata.create_all(engine)
app = FastAPI()

@app.get("/", response_model=None)
def read_root():
    return {"message": "Welcome to the todos API. Create new user and you are ready to go!"}

app.include_router(user_router.router, prefix='/users')
app.include_router(token_router.router, prefix='/auth')
app.include_router(todo_router.router, prefix='/todos')
app.include_router(permission_router.router, prefix='/permissions')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=2)