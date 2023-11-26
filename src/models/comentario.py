from src.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.models.user import User
from src.models.publicacao import Publicacao
from sqlalchemy.orm import relationship

class comentarios(Base):
    __tablename__ = "comentarios"
    
    id = Column(Integer, primary_key=True, index=True)
    texto_comentario = Column(String)
    id_pessoa = Column(Integer, ForeignKey("Pessoa.id"))
    id_publicacao = Column(Integer, ForeignKey("publicacoes.id"))