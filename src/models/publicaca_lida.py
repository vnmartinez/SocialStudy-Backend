from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class PublicacaoLida(Base):
    __tablename__ = "publicacoes_lidas"
    
    id = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey("pessoa.id"))
    id_publicacao = Column(Integer, ForeignKey("publicacoes.id"))
    
    pessoa = relationship("pessoa")
    publicacao = relationship("publicacoes")