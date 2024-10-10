from app.schemas.response_generic import ResponseGeneric
from app.models.competicao import Competicao
from app.models.resultado import Resultado
from app.repositories.competicao_repository import CompeticaoRepository
from app.repositories.atleta_repository import AtletaRepository
from app.repositories.resultado_repository import ResultadoRepository
from app.schemas.resultado import ResultadoResponse
from app.schemas.enums.status_competicao_enum import StatusCompeticaoEnum
from app.schemas.enums.modalidade_enum import ModalidadeEnum
from app.schemas.ranking import RankingResponse
from sqlalchemy.orm import Session
class CompeticaoService:
   def __init__(self, db: Session):
       self.db = db
       self.competicao_repository = CompeticaoRepository(db)
       self.atleta_repository = AtletaRepository(db)
       self.resultado_repository = ResultadoRepository(db)
       
   def criar_competicao(self, nome: str, modalidade: str) -> ResponseGeneric:       
       competicao_existente = self.competicao_repository.buscar_por_nome_e_modalidade(nome, modalidade)
       if competicao_existente:
           return ResponseGeneric(
               mensagem=f"Competição com nome '{nome}' e modalidade '{modalidade}' já existe. ID da competição: {competicao_existente.id}",
               status=400
           )
       nova_competicao = Competicao(nome=nome, modalidade=modalidade, status=StatusCompeticaoEnum.ABERTA)
       self.competicao_repository.salvar(nova_competicao)
       return ResponseGeneric(
           mensagem=f"Competição '{nome}' iniciada.",
           status=201,
           id=nova_competicao.id  
       )
   def adicionar_resultado(self, competicao_id: int, atleta_nome: str, valor: float, unidade: str):
       competicao = self.competicao_repository.buscar_por_id(competicao_id)
       if not competicao:
           return ResponseGeneric(mensagem="Competição não encontrada.", status=404)
       if competicao.status == StatusCompeticaoEnum.ENCERRADA:
           return ResponseGeneric(mensagem="Competição já está encerrada.", status=409)
       atleta = self.atleta_repository.buscar_por_nome(atleta_nome)
       if not atleta:
           atleta = self.atleta_repository.salvar(atleta_nome)
       # Verificação de modalidade e registro do resultado
       if competicao.modalidade == ModalidadeEnum.LANCAMENTO_DARDO:
           tentativas = self.resultado_repository.buscar_tentativas_por_competicao_e_atleta(competicao_id, atleta.id)
           if len(tentativas) >= 3:
               return ResponseGeneric(mensagem=f"O atleta {atleta.nome} já fez 3 tentativas nesta competição.", status=409)
           novo_resultado = Resultado(atleta_id=atleta.id, valor=valor, unidade=unidade)
           competicao.resultados.append(novo_resultado)
           self.competicao_repository.salvar(competicao)
           melhor_resultado = max(tentativas + [novo_resultado], key=lambda r: r.valor)
           return ResultadoResponse(
               competicao=competicao.nome,
               atleta=atleta.nome,
               value=melhor_resultado.valor,
               unidade=melhor_resultado.unidade,
               mensagem="Tentativa adicionada com sucesso"
           )
       elif competicao.modalidade == ModalidadeEnum.CEM_METROS_RASOS:
           resultado_existente = self.resultado_repository.atleta_ja_participou(competicao_id, atleta.id)
           if resultado_existente:
               return ResponseGeneric(mensagem=f"O atleta {atleta.nome} já participou desta competição.", status=409)
           novo_resultado = Resultado(atleta_id=atleta.id, valor=valor, unidade=unidade)
           competicao.resultados.append(novo_resultado)
           self.competicao_repository.salvar(competicao)
           return ResultadoResponse(
               competicao=competicao.nome,
               atleta=atleta.nome,
               value=valor,
               unidade=unidade,
               mensagem="Resultado adicionado com sucesso"
           )
       else:
           return ResponseGeneric(mensagem="Modalidade não reconhecida.", status=400)
   
   def obter_ranking(self, competicao_id: int):
    competicao = self.competicao_repository.buscar_por_id(competicao_id)
    if not competicao:
        return ResponseGeneric(mensagem="Competição não encontrada.", status=404)
    if not competicao.resultados:
        return ResponseGeneric(mensagem=f"Sem resultados cadastrados para a competição.", status=200)
   
    ranking_finalizado = (competicao.status == StatusCompeticaoEnum.ENCERRADA)
    tipo_ranking = "Ranking final" if ranking_finalizado else "Ranking parcial"
    
    mensagem_ranking = f"{tipo_ranking} da competição '{competicao.nome}' da modalidade '{competicao.modalidade}'"
    # Organiza o ranking de acordo com a modalidade
    if competicao.modalidade == ModalidadeEnum.CEM_METROS_RASOS:
        ranking = sorted(competicao.resultados, key=lambda x: x.valor)
    elif competicao.modalidade == ModalidadeEnum.LANCAMENTO_DARDO:
        melhores_resultados = {}
        for resultado in competicao.resultados:
            if resultado.atleta_id not in melhores_resultados or melhores_resultados[resultado.atleta_id].valor < resultado.valor:
                melhores_resultados[resultado.atleta_id] = resultado
        ranking = sorted(melhores_resultados.values(), key=lambda x: x.valor, reverse=True)
    else:
        return ResponseGeneric(mensagem="Modalidade não reconhecida.", status=400)
    
    atletas_ids = [resultado.atleta_id for resultado in ranking]
    atletas = self.atleta_repository.buscar_por_ids(atletas_ids)
    atletas_dict = {atleta.id: atleta.nome for atleta in atletas}
    # Formatar o ranking
    ranking_formatado = [
        {
            "atleta": atletas_dict[resultado.atleta_id],
            "pontuacao": resultado.valor,
            "unidade": resultado.unidade,
            "posicao": index + 1
        }
        for index, resultado in enumerate(ranking)
    ]
    return RankingResponse(
        mensagem=mensagem_ranking,
        ranking=ranking_formatado
    )
   
   def finalizar_competicao(self, competicao_id: int) -> ResponseGeneric:   
    competicao = self.competicao_repository.buscar_por_id(competicao_id)
    if not competicao:
        return ResponseGeneric(mensagem="Competição não encontrada.", status=404)   
    if competicao.status == StatusCompeticaoEnum.ENCERRADA:
        return ResponseGeneric(
            mensagem=f"A competição '{competicao.nome}' da modalidade '{competicao.modalidade}' já foi finalizada.",
            status=409
        )    
    competicao.finalizar()  
    self.competicao_repository.salvar(competicao)
    return ResponseGeneric(
        mensagem=f"A competição '{competicao.nome}' da modalidade '{competicao.modalidade}' foi finalizada com sucesso.",
        status=200
    )