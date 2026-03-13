from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM


def create_token():

    payload = {
        "exp": datetime.utcnow() + timedelta(hours=2)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token