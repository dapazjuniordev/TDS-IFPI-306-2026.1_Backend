from pydantic import BaseModel


class Evento(BaseModel):
    id:int
    nome:str
    data_inicio:str
    data_fim: str
    endereco:str