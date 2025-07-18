''''
    DEFINE AS CLASSES DE DOMINIO PARA ESTA APLICACAO
'''




from dataclasses import dataclass

@dataclass
class Categoria:
    id: int
    descricao: str

@dataclass
class Produto:
    id: int
    descricao: str
    preco_unitario: float
    quantidade_estoque: int
    categoria: Categoria