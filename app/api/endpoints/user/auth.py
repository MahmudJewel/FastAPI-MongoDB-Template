# # fastapi 
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from datetime import timedelta

# # import
from app.schemas.user import User, UserLogin, Token
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.endpoints.user import functions as user_functions


auth_module = APIRouter()

# ============> login/logout < ======================
# getting access token for login 
@auth_module.post("/login", response_model= Token)
async def login_for_access_token(
    user: UserLogin
) -> Token:
    member = await user_functions.authenticate_user(user=user)
    # print('member =================> ', member)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await user_functions.create_access_token(
        data={"id": member.id, "email": member.email, "role": member.role}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


# get curren user 
@auth_module.get('/users/me/', response_model= User)
async def read_current_user( current_user: Annotated[User, Depends(user_functions.get_current_user)]):
    return current_user
