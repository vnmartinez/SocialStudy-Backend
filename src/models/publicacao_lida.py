from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.pessoa import Pessoa
from src.models.publicacao import Publicacao


class PublicacaoLida(Base):
    __tablename__ = "publicacoes_lidas"

    id = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey("pessoa.id"))
    id_publicacao = Column(Integer, ForeignKey("publicacoes.id"))

    pessoa = relationship(Pessoa)
    publicacao = relationship(Publicacao)
