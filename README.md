# ToDo API application
## API information:
### API Docs:
```
GET 0.0.0.0:8000/docs
```
or
```
GET 127.0.0.1:8000/docs
```
or
```
GET localhost:8000/docs
```
## Running app 
### 1. Clone repository:
```
git clone https://github.com/qsnk/todo-api.git
```
### 2. Change directory:
```
cd todo-api
```
### 3. Add .env file:
by command:
```
echo JWT_SECRET_KEY=key \
POSTGRES_HOST=host \
POSTGRES_DB=db \
POSTGRES_USER=user \
POSTGRES_PASSWORD=password \
> .env
```
or manually by this structure:
```
JWT_SECRET_KEY=key
POSTGRES_HOST=host
POSTGRES_DB=db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
```
## Via docker
### Run container:
```
docker-compose up
```
## Locally (Via Terminal)
### Install dependencies:
```
pip install -r requirements.txt
```
### Change directory:
```
cd app
```
### Run app:
```
python main.py
```
## Run tests:
```
pytest test.py
```