from jwcrypto import jwt
from icecream import ic
import time
from popp.token import generate_signing_key, create_jwks
import json

prk = generate_signing_key()
jwks = create_jwks(prk)
ic(jwks.export(as_dict=True))

popp_claims = {
    "iss": "https://popp.example.com",
    "iat": int(time.time()),
    "urn:telematik:popp:v1": {
        "subject": {
            "auth_method": "pki",
            "auth_time": int(time.time())-2*60*60,
            "identifier": {
                "type": "telematik-id",
                "value": "9-24358745985",
            },
            "profession_oid": "1.2.276.0.76.4.50",
        },
        "patient": {
            "identifier": {
                "type": "kvid-10",
                "value": "X123456789",
            },
            "insurer": {
                "identifier": {
                    "type": "iknr",
                    "value": "123456789",
                },
            },
            "proof_method": "ehc",
            "proof_time": int(time.time())-1,
        },
    },
}

token = jwt.JWT(header={
    "alg": "ES256",
    "jku": "https://popp.example.com/popp/api/v1/public/jwks",
    "kid": prk.kid,
    "typ": "vnd.telematik.popp+jwt",
  },
  claims=popp_claims
)

print(json.dumps(json.loads(token.header), indent=2))
print('.')
print(json.dumps(json.loads(token.claims), indent=2))


token.make_signed_token(prk)

ic(token.serialize())
