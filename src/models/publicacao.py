from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.pessoa import Pessoa

class Publicacao(Base):
    __tablename__ = "publicacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    link = Column(String)
    id_pessoa = Column(Integer, ForeignKey("pessoa.id"))
    like_count = Column(Integer, default=0)
    
    pessoa = relationship(Pessoa)
    