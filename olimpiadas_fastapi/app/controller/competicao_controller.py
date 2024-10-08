from fastapi import APIRouter, HTTPException
from app.services.competicao_service import CompeticaoService

router = APIRouter()

# Instancia o serviço de competição
service = CompeticaoService()

@router.post("/competicoes")
def criar_competicao(nome: str, tipo: str):
    try:
        return service.criar_competicao(nome, tipo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/competicoes/{competicao_id}/resultados")
def adicionar_resultado(competicao_id: int, atleta_id: int, valor: float, fase: int):
    try:
        return service.adicionar_resultado(competicao_id, atleta_id, valor, fase)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/competicoes/{competicao_id}/ranking")
def obter_ranking(competicao_id: int):
    try:
        return service.obter_ranking(competicao_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/competicoes/{competicao_id}/finalizar")
def finalizar_competicao(competicao_id: int):
    try:
        return service.finalizar_competicao(competicao_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))