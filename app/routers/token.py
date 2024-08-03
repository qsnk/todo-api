from sqlalchemy.orm import Session
from database import connect_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services import token as token_service
from dto.token import Token


router = APIRouter()


@router.post("/token", tags=['Token'], response_model=Token)
async def login_for_access_token(
        data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(connect_db)
        ):
    return token_service.get_token(data=data, db=db)