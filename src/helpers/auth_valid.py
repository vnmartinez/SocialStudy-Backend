from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from src.config import config
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
        user_email = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        
        user = db.query(User).filter(User.email == user_email).first()
        
        if user is None:
            raise credentials_exception
        
        return {"id": user.id, "user_info": payload}
    except JWTError:
        raise credentials_exception