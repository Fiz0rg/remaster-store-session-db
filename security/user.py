from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(planed_password, hashed_password):
    return pwd_context.verify(planed_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def authenticate_user(): 
    pass
