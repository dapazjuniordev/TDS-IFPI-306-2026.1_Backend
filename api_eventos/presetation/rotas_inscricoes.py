from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def list_inscricoes():
    return 'Lista inscrições'


@router.post('/')
def create_inscricao():
    return 'Confirma Inscrição num evento'

router.get('/{id}')
def details_inscricao(id:int):
    return f'Detalhes da inscrição {id}'