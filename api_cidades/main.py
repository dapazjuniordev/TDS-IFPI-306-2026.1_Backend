from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # BaseModel garante que os dados recebidos pela API sejam válidos e do tipo certo, sem validação manual

app = FastAPI()

# Classe Cidade completa
class Cidade(BaseModel):
    id: int
    nome: str
    uf: str
    populacao: int
    ponto_turistico: str


# NovaCidade é usado no POST e PUT, onde o usuário não deve enviar o id
class NovaCidade(BaseModel):
    nome: str
    uf: str
    populacao: int
    ponto_turistico: str


id_atual = 1

# Banco de dados em memória
cidades = []


def get_cidade_for_id(id: int):
    for cidade in cidades:
        if cidade.id == id:
            return cidade
        
    return None  


# Retorna todas as cidades, ou filtra pelo 'uf' se fornecido
@app.get('/cidades')
def cidades_list(uf: str = None):
    if uf:
        return [cidade for cidade in cidades if cidade.uf == uf]
    
    return cidades


# Busca cidade pelo id informado
@app.get('/cidades/{id}')
def cidades_detail(id: int):
    cidade = get_cidade_for_id(id)
    if cidade is None:
        raise HTTPException(status_code=404, detail='Cidade não encontrada')
    
    return cidade


# Cria uma nova cidade com id gerado automaticamente e retorna status 201
@app.post('/cidades', status_code=201)
def cidades_create(cidade: NovaCidade):
    global id_atual

    nova_cidade = Cidade(
        id=id_atual,
        nome=cidade.nome,
        uf=cidade.uf,
        populacao=cidade.populacao,
        ponto_turistico=cidade.ponto_turistico
    )
    id_atual += 1
    cidades.append(nova_cidade)

    return nova_cidade


# Atualiza uma cidade existente
@app.put('/cidades/{id}')
def cidades_atualize(id: int, dados: NovaCidade):
    cidade = get_cidade_for_id(id)
    if cidade is None:
        raise HTTPException(status_code=404, detail='Cidade não encontrada')
    
    cidade_atualizada = Cidade(
        id=cidade.id,  # mantém o id original
        nome=dados.nome,
        uf=dados.uf,
        populacao=dados.populacao,
        ponto_turistico=dados.ponto_turistico
    )
    # Como itens podem ser removidos, nem sempre o id e posição vão
    # corresponder, por isso é importante pegar a posição do objeto
    cidades[cidades.index(cidade)] = cidade_atualizada
    return cidade_atualizada


# Remove uma cidade da lista pelo id informado
@app.delete('/cidades/{id}')
def deletar_cidade(id: int):
    cidade = get_cidade_for_id(id)
    if cidade is None:
        raise HTTPException(status_code=404, detail='Cidade não encontrada')
    cidades.remove(cidade)
    return {'mensagem': f"Cidade '{cidade.nome}' deletada com sucesso"}


# Filtra cidades pelo uf do estado informado
@app.get('/estados/{sigla}/cidades')
def estado_cidade(sigla: str):
    resultado = [cidade for cidade in cidades if cidade.uf == sigla]
    if not resultado:
        raise HTTPException(status_code=404, detail='Nenhuma cidade encontrada para esse estado')
    return resultado