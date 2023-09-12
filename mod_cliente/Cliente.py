from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str = None
    compra_fiado: int
    dia_fiado: int
    senha: str = None