def calcular_mpf(respostas):
    media = sum(respostas) / len(respostas)

    if media <= 3:
        nivel = "Baixo"
    elif media <= 6:
        nivel = "Moderado"
    else:
        nivel = "Alto"

    return {
        "media": round(media, 2),
        "nivel": nivel
    }


def calcular_jss(demanda, controle, apoio):
    score_demanda = sum(demanda)
    score_controle = sum(controle)
    score_apoio = sum(apoio)

    return {
        "demanda": score_demanda,
        "controle": score_controle,
        "apoio": score_apoio
    }


def classificar_karasek(demanda, controle):
    if demanda >= 15 and controle < 15:
        return "Alto risco psicossocial"
    elif demanda >= 15 and controle >= 15:
        return "Risco moderado"
    elif demanda < 15 and controle < 15:
        return "Risco passivo"
    else:
        return "Baixo risco"
def calcular_risco_nr01(probabilidade, severidade):
    risco = probabilidade * severidade

    if risco <= 4:
        nivel = "Baixo"
    elif risco <= 9:
        nivel = "Médio"
    else:
        nivel = "Alto"

    return {
        "probabilidade": probabilidade,
        "severidade": severidade,
        "risco": risco,
        "nivel": nivel
    }
