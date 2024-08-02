from enum import Enum
from pydantic import BaseModel


class AuthMethod(str, Enum):
    pki = "pki"


class Subject(BaseModel):
    auth_method: AuthMethod
    auth_time: int

    class Config:
        use_enum_values = True


class ProofMethod(str, Enum):
    ehc = "ehc"
    ehc_nfc = "ehc-nfc"
    oidf = "oidf"

    class Config:
        use_enum_values = True


CLAIM_POPP_SUBJECT = "urn:telematik:popp:subject"
CLAIM_POPP_PATIENT = "urn:telematik:popp:patient"


class Patient(BaseModel):
    proof_method: ProofMethod
