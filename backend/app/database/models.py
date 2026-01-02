from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)

    mpf_media = Column(Float)
    mpf_nivel = Column(String)

    demanda = Column(Integer)
    controle = Column(Integer)
    apoio = Column(Integer)

    karasek = Column(String)

    probabilidade = Column(Integer)
    severidade = Column(Integer)
    risco = Column(Integer)
    risco_nivel = Column(String)
