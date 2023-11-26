from src.database import Base
from sqlalchemy import Column, Integer, String

class Publicacao(Base):
    __tablename__ = "publicacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    link = Column(String)
    id_pessoa = Column(Integer, nullable=True)
    like_count = Column(Integer, default=0)
    