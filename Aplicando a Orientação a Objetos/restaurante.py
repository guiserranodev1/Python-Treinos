class Restaurante:

    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome.title() #title é letra maiuscula no começo
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} : {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome} : {restaurante.categoria} : {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()


