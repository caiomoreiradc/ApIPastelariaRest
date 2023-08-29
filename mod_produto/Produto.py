from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    foto: int
    grupo: int
    valor_decimal: int = None