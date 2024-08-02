from jwcrypto import jwt
from icecream import ic
import time
from popp.token import generate_signing_key, create_jwks

prk = generate_signing_key()
jwks = create_jwks(prk)
ic(jwks.export(as_dict=True))

popp_claims = {
    "iss": "https://popp.example.com",
    "iat": time.time(),
    "urn:telematik:popp:v1": {
        "subject": {
            "auth_method": "pki",
            "auth_time": int(time.time()),
            "id": "9-24358745985",
            "profession_oid": "1.2.276.",
        },
        "patient": {
            "id": "X123456789",
            "insurance_id": "134567890",
            "proof_method": "ehc",
            "proof_time": int(time.time()),
        },
    },
}

ic(popp_claims)
token = jwt.JWT(header={"alg": "ES256", "kid": prk.kid}, claims=popp_claims)

token.make_signed_token(prk)

ic(token.serialize())
