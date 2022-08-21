from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from fastapi import Depends

from sqlmodel import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from pydantic import ValidationError

from db.user import UserDb
from endpoints.depends import get_session
from exeptions.exeptions import incorrect_auth
from schemas.security import TokenData


SECRET_KEY = '4b85007d663af5a8e97d2bd65afa8befa815df1c0a5acf44625f7f136d5a8d9c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='users/token',
                                     scopes={"current": "For current user",
                                             "other": "Other users",
                                             "admin": "Hugo BOSS"})

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(planed_password, hashed_password):
    return pwd_context.verify(planed_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def authenticate_user(): 
    pass


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def auth_user(username: str, password: str, db: Session):
    current_user = get_user(username, db)
    if not verify_password(password, current_user.password):
        raise incorrect_auth("Incorrect password")
    return current_user


def get_user(username: str,
             db: Session):
    user = db.query(UserDb).filter(UserDb.name == username).first()
    if user:
        return user
    else:
        raise incorrect_auth("User Not Found")


def get_current_user(security_scopes: SecurityScopes,
                     token: str = Depends(oauth2_scheme),
                     session: Session = Depends(get_session)):
    
    credentials_exeption = incorrect_auth("Could not validate credentials")
    if security_scopes.scopes:
        authenticate_value = f'Bearer scopes={security_scopes.scope_str}'
    else:
        authenticate_value = "Bearer"
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exeption
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(username=username, scopes=token_scopes)
    except (JWTError, ValidationError):
        raise credentials_exeption
    user = get_user(token_data.username, session)
    if user is None:
        return credentials_exeption
    print(security_scopes.scopes)
    for scope in security_scopes.scopes:
        print(f'scope {scope}')
        print(f'security_scope {security_scopes.scopes}')
        print(f'token_data {token_data.scopes}')
        if scope not in token_data.scopes:
            raise incorrect_auth("Not enought permissions")
    return user