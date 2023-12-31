from uuid import uuid4

from storage.redis_db import RedisDataBase
from storage.db import get_database_interface
from entity import SecretsRequest, GenerateRequest, SecretResponse
from utils import encrypt_string, generate_key, decrypt_string

from uvicorn import run
from cryptography.fernet import InvalidToken
from fastapi import FastAPI, HTTPException


app = FastAPI()
storage = get_database_interface(RedisDataBase, "redis://localhost")


@app.post("/generate", response_model=dict)
async def generate_key_secret(request: GenerateRequest):
    """
    Generates a new secret.
    :param request: json
    :return: secret_key
    """
    key_id = str(uuid4())
    await storage.set_data_by_key(
        key_id,
        encrypt_string(request.data, generate_key(request.password)),
    )

    return {"secret_key": key_id}


@app.post("/secrets", response_model=SecretResponse)
async def get_secret(request: SecretsRequest):
    """
    Gets a secret.
    :param request: json
    :return: data
    """
    if data := await storage.get_data_by_key(key_id=request.secret_key) is None:
        raise HTTPException(status_code=404, detail="NOT FOUND")

    encryption_key = generate_key(request.password)
    try:
        decrypted_string = decrypt_string(data, encryption_key)
        print(f"Расшифрованная строка: {decrypted_string}")
    except InvalidToken:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"data": data}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
