from pydantic import BaseModel

class User():
    id: int
    email: str
    senha: str
    nome: str