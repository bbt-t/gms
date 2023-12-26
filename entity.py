from pydantic import BaseModel


class GenerateRequest(BaseModel):
    data: str
    password: str
    ttl: int = None


class SecretsRequest(BaseModel):
    secret_key: str
    password: str


class SecretResponse(BaseModel):
    data: str
