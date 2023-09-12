import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produt'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(100), nullable=False)
    foto = Column(Integer, unique=True, nullable=False)
    grupo = Column(Integer, nullable=False)
    valor_decimal = Column(Integer, nullable=False)

    def __init__(self, id_produto, nome, descricao, foto, grupo, valor_decimal):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.grupo = grupo
        self.valor_decimal = valor_decimal