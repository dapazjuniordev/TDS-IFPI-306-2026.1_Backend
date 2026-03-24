from pydantic import BaseModel

class SignupDTO(BaseModel):
    email: str
    nome: str
    senha: str


class SigninDTO(BaseModel):
    email: str
    senha: str