from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome.title() #title é letra maiuscula no começo
        self.categoria = categoria.upper()
        self._ativo = False
        self._avalicao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} : {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria do restaurante'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
                avaliacao = Avaliacao(cliente, nota)
                self._avalicao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avalicao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avalicao) 
        quantidade_de_notas = len(self._avalicao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media