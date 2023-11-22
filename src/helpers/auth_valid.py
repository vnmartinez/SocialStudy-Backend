from fastapi import Depends, HTTPException
from jose import jwt, jwk
from jose.exceptions import JWTClaimsError
from src import config

def authenticate_user(token: str):
    try:
        payload = JWT.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTClaimsError:
        raise HTTPException(status_code=401, detail="O usuário precisa estar logado para realizar a operação")
    except Exception:
        raise HTTPException(status_code=400, detail="Solicitação inválida")