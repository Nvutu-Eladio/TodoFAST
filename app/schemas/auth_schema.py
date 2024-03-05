from pydantic import BaseModel
from uuid import UUID

# Usado quando for autenticar
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

# Para utilizar access token
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None