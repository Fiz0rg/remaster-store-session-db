from fastapi import status, HTTPException


def incorrect_auth(detail: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={'WWW-Authenticate': "Bearer"}
        )