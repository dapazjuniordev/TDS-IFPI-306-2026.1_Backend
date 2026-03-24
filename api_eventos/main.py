import sys
sys.dont_write_bytecode = True

from fastapi import FastAPI
from presetation.rotas_autenticacao import router as auth_router
from presetation.rotas_eventos import router as eventos_router
from presetation.rotas_inscricoes import router as inscricoes_router


app = FastAPI()

app.include_router(auth_router, prefix='/auth')
app.include_router(eventos_router, prefix='/eventos')
app.include_router(inscricoes_router, prefix='/inscricoes')

@app.get('/')
def home():
    return 'Página Início'