from pydantic import BaseModel


class BaseUser():
    id: int
    email: str
    nome: str


class User():
    id: int
    email: str
    senha: str
    nome: str