from domain.modelos_autenticacao import User

class AutenticacaoRepository():

    def __init__(self):
        self.users: list[User] = []
        self.proximo_id = 1


    def create(self, email: str, senha: str, nome:str):
        new_user = User(id=1, email=email, senha=senha, nome=nome)
        self.users.append(new_user)
        self.proximo_id += 1
    

    def getByEmail(self, email:str):
        for user in self.users:
            if user.email == email:
                return user
        
        return None
    

    def getById(self, id:int):
        for user in self.users:
            if user.id == id:
                return user
        
        return None