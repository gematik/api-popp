from jwcrypto import jwk


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
