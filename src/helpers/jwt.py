from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from src.config import config

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=config.access_token_expire_minutes
        )
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.secret_key, config.algorithm)
    return encoded_jwt