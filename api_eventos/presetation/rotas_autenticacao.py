from fastapi import APIRouter, status, HTTPException

from persisence.autenticacao_repository import AutenticacaoRepository
from presetation.dto.autenticacao_dtos import SignupDTO, SigninDTO
from domain.modelos_autenticacao import BaseUser

router = APIRouter()
repo = AutenticacaoRepository()

@router.post('/signup',
             response_model=BaseUser,
             status_code=status.HTTP_201_CREATED)
def signup(dados: SignupDTO):
    usuario = repo.create(email=dados.email,
                          senha=dados.senha,
                          nome=dados.nome)
    return usuario


@router.post('/signin')
def signin(dados: SigninDTO):
    usuario_encontrado = repo.getByEmail(email=dados.email)

    if not usuario_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário não localizado")
    
    if usuario_encontrado.senha != dados.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta")
    
    return {"acess_token": f"Fake_Token[{usuario_encontrado.id}]-1234567"}

@router.get('/me')
def me():
    return ''