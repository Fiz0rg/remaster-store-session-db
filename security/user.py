import datetime

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt


SECRET_KEY = '4b85007d663af5a8e97d2bd65afa8befa815df1c0a5acf44625f7f136d5a8d9c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(planed_password, hashed_password):
    return pwd_context.verify(planed_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def authenticate_user(): 
    pass


def create_access_token(data: dict, expires_delta: datetime.timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

