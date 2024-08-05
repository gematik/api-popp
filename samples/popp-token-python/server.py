from fastapi import FastAPI, WebSocket, Form
from typing import Annotated
import random
from popp.token import generate_signing_key, create_jwks

app = FastAPI()

codes = set()

prk = generate_signing_key()
jwks = create_jwks(prk)


def generate_6_digit_code() -> str:
    # random 6 digit code
    return str(random.randint(100000, 999999))


@app.get("/popp/api/v1/public/jwks")
async def getJWKS():
    return jwks.export(as_dict=True)


@app.post("/popp/api/v1/healthcare-provider/token/code")
async def issueTokenCode(code: Annotated[str, Form()]):
    return {"token": "token"}


@app.websocket("/popp/api/v1/healthcare-provider/token/ehc")
async def issueTokenEHC(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Type '1' to receive token")
    while True:
        data = await websocket.receive_text()
        if data.rstrip() == "1":
            await websocket.send_text("Token")
            await websocket.close()
            break
        else:
            await websocket.send_text(f"Message text was: {data}")


@app.websocket("/popp/api/v1/patient/proof/ehc")
async def patientVerifyEHC(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Type '1' to receive code")
    while True:
        data = await websocket.receive_text()
        if data.rstrip() == "1":
            code = generate_6_digit_code()
            codes.add(code)
            await websocket.send_text(code)
            await websocket.close()
            break
        else:
            await websocket.send_text(f"Message text was: {data}")
