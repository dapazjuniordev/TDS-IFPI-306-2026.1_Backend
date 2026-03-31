from fastapi import APIRouter, status, HTTPException

from persisence.autenticacao_repository import AutenticacaoRepository
from presetation.dto.autenticacao_dtos import SignupDTO, SigninDTO
from domain.modelos_autenticacao import BaseUser
from infrastructure import hash_provider, jwt_provider

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
    
    if not hash_provider.verify_hash(dados.senha, usuario_encontrado.senha):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta")
    
    access_token = jwt_provider.generate({'sub': usuario_encontrado.id})
    return {"access_token": access_token}

@router.get('/me')
def me():
    ...