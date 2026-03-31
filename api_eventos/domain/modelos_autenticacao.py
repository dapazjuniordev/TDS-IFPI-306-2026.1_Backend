from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    email: str
    nome: str


class User(BaseModel):
    id: int
    email: str
    senha: str
    nome: str