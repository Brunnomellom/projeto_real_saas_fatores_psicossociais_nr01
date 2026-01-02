from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.risco_psicossocial import (
    calcular_mpf,
    calcular_jss,
    classificar_karasek,
    calcular_risco_nr01
)

from app.database.database import SessionLocal
from app.database.models import Avaliacao

router = APIRouter(prefix="/avaliacao", tags=["Avaliação Psicossocial"])


class AvaliacaoRequest(BaseModel):
    mpf: List[int]
    demanda: List[int]
    controle: List[int]
    apoio: List[int]
    severidade: int


@router.post("/")
def avaliar(dados: AvaliacaoRequest):
    db = SessionLocal()

    mpf_resultado = calcular_mpf(dados.mpf)

    jss_resultado = calcular_jss(
        dados.demanda,
        dados.controle,
        dados.apoio
    )

    karasek = classificar_karasek(
        jss_resultado["demanda"],
        jss_resultado["controle"]
    )

    if karasek == "Alto risco psicossocial":
        probabilidade = 3
    elif karasek == "Risco moderado":
        probabilidade = 2
    else:
        probabilidade = 1

    nr01 = calcular_risco_nr01(probabilidade, dados.severidade)

    avaliacao = Avaliacao(
        mpf_media=mpf_resultado["media"],
        mpf_nivel=mpf_resultado["nivel"],
        demanda=jss_resultado["demanda"],
        controle=jss_resultado["controle"],
        apoio=jss_resultado["apoio"],
        karasek=karasek,
        probabilidade=nr01["probabilidade"],
        severidade=nr01["severidade"],
        risco=nr01["risco"],
        risco_nivel=nr01["nivel"]
    )

    db.add(avaliacao)
    db.commit()
    db.refresh(avaliacao)
    db.close()

    return {
        "id": avaliacao.id,
        "nr01": nr01
    }
@router.get("/")
def listar_avaliacoes():
    db = SessionLocal()
    avaliacoes = db.query(Avaliacao).all()
    db.close()

    return avaliacoes
