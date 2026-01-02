def calcular_risco(demanda: int, controle: int, apoio: int):
    score = demanda + controle + apoio

    if score <= 6:
        return {
            "nivel": "Baixo",
            "cor": "verde",
            "descricao": "Risco psicossocial baixo. Situação controlada."
        }

    elif score <= 10:
        return {
            "nivel": "Moderado",
            "cor": "amarelo",
            "descricao": "Risco psicossocial moderado. Requer atenção."
        }

    else:
        return {
            "nivel": "Alto",
            "cor": "vermelho",
            "descricao": "Risco psicossocial alto. Ação imediata recomendada."
        }
