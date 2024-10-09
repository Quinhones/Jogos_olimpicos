from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.competicao_service import CompeticaoService
from app.database import get_db
from app.schemas.competicao import CompeticaoCreate
from app.schemas.response_generic import ResponseGeneric

router = APIRouter()

@router.post("/competicoes", response_model=ResponseGeneric)
def criar_competicao(competicao: CompeticaoCreate, db: Session = Depends(get_db)):
   service = CompeticaoService(db)
   return service.criar_competicao(nome=competicao.nome, modalidade=competicao.modalidade)

@router.post("/competicoes/{competicao_id}/resultados", response_model=dict)
def adicionar_resultado(competicao_id: int, resultado: dict, db: Session = Depends(get_db)):
   service = CompeticaoService(db)
   return service.adicionar_resultado(competicao_id=competicao_id, atleta_nome=resultado['atleta'], valor=resultado['valor'], unidade=resultado['unidade'])

@router.get("/competicoes/{competicao_id}/ranking", response_model=dict)
def obter_ranking(competicao_id: int, db: Session = Depends(get_db)):
   service = CompeticaoService(db)
   return service.obter_ranking(competicao_id)

@router.post("/competicoes/{competicao_id}/finalizar", response_model=dict)
def finalizar_competicao(competicao_id: int, db: Session = Depends(get_db)):
   service = CompeticaoService(db)
   return service.finalizar_competicao(competicao_id)