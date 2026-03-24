from domain.modelos import Evento

class EventoRepository():
    #Conversa com BD
    
    def __init__(self):
        self.eventos = [
            Evento(id=1,
                nome='CasaCor2026',
                data_inicio='01/03/2026',
                data_fim='31/03/2026',
                endereco='A. Presidente Kennedy'),
            Evento(id=2,
                nome='Maratona de Teresina',
                data_inicio='19/03/2026',
                data_fim='19/03/2026',
                endereco='Raul Lopes')
        ]

    def all(self):
        return self.eventos
    

    def create(self, novo:Evento):
        self.eventos.append(novo)
        return novo