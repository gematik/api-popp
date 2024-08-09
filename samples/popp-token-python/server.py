from fastapi import FastAPI, WebSocket, Form
from typing import Annotated
import random
from popp.token import read_signing_key_from_pem, create_jwks, create_mock_token

app = FastAPI()

codes = set()

prk = read_signing_key_from_pem(
    "secrets/popp-signing-key.pem",
    "secrets/popp-signing-cert.pem",
    "secrets/ca-cert.pem",
)

jwks = create_jwks(prk)


def generate_6_digit_code() -> str:
    # random 6 digit code
    return str(random.randint(100000, 999999))


@app.get("/popp/api/v1/public/jwks")
async def public_get_jwks() -> dict:
    return jwks.export(as_dict=True)


@app.post("/popp/api/v1/hcp/token/code")
async def hcp_issue_token_code(code: Annotated[str, Form()]) -> dict:
    return {
        "token": create_mock_token(
            prk, "X123456789", "123456789", "9-24358745985"
        ).serialize()
    }


@app.websocket("/popp/api/v1/hcp/token/ehc")
async def hcp_issue_token_ehv(websocket: WebSocket) -> dict:
    await websocket.accept()
    await websocket.send_text("Type '1' to receive token")
    while True:
        data = await websocket.receive_text()
        if data.rstrip() == "1":
            token = create_mock_token(
                prk, "X123456789", "123456789", "9-24358745985"
            ).serialize()
            await websocket.send_text(token)
            await websocket.close()
            break
        else:
            await websocket.send_text(f"Message text was: {data}")


@app.websocket("/popp/api/v1/patient/proof/ehc")
async def patient_verify_ehc(websocket: WebSocket):
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
