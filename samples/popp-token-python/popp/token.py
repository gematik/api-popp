from jwcrypto import jwk, jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.serialization import Encoding
import base64
import time


def read_signing_key_from_pem(path: str, cert_path: str, ca_cert_path: str) -> jwk.JWK:
    with open(path, "r") as key_file:
        key = jwk.JWK.from_pem(key_file.read().encode())

    with open(cert_path, "r") as cert_file:
        cert = load_pem_x509_certificate(cert_file.read().encode())
    # encode cert as der
    cert_der = cert.public_bytes(encoding=Encoding.DER)

    with open(ca_cert_path, "r") as ca_cert_file:
        ca_cert = load_pem_x509_certificate(ca_cert_file.read().encode())
    # encode ca_cert as der
    ca_cert_der = ca_cert.public_bytes(encoding=Encoding.DER)

    # add x5c to key
    key.x5c = [
        base64.b64encode(cert_der).decode(),
        base64.b64encode(ca_cert_der).decode(),
    ]

    return key


def generate_signing_key() -> jwk.JWK:
    key = jwk.JWK.generate(kty="EC", use="sig", crv="P-256")
    key.kid = key.thumbprint()
    return key


def create_jwks(*keys: jwk.JWK) -> jwk.JWKSet:
    jwks = jwk.JWKSet()
    for key in keys:
        puk = jwk.JWK(**key.export_public(as_dict=True))
        jwks.add(puk)
    return jwks


def create_mock_token(
    signing_key: jwk.JWK,
    kvnr: str,
    iknr: str,
    telematik_id: str,
) -> jwt.JWT:
    popp_claims = {
        "iss": "https://popp.example.com",
        "iat": int(time.time()),
        "urn:telematik:popp:v1": {
            "subject": {
                "auth_method": "pki",
                "auth_time": int(time.time()) - 2 * 60 * 60,
                "identifier": {
                    "type": "telematik-id",
                    "value": telematik_id,
                },
                "profession_oid": "1.2.276.0.76.4.50",
            },
            "patient": {
                "identifier": {
                    "type": "kvid-10",
                    "value": kvnr,
                },
                "insurer": {
                    "identifier": {
                        "type": "iknr",
                        "value": iknr,
                    },
                },
                "proof_method": "ehc",
                "proof_time": int(time.time()) - 1,
            },
        },
    }

    token = jwt.JWT(
        header={
            "alg": "ES256",
            "jku": "https://popp.example.com/popp/api/v1/public/jwks",
            "kid": signing_key.kid,
            "typ": "vnd.telematik.popp+jwt",
        },
        claims=popp_claims,
    )

    token.make_signed_token(signing_key)

    return token
