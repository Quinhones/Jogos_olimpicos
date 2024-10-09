from app.schemas.response_generic import ResponseGeneric
from app.models.competicao import Competicao
from app.models.resultado import Resultado
from app.repositories.competicao_repository import CompeticaoRepository
from app.repositories.atleta_repository import AtletaRepository
from app.repositories.resultado_repository import ResultadoRepository
from app.schemas.competicao import CompeticaoResponse
from app.schemas.enums.status_competicao_enum import StatusCompeticaoEnum
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
           return ResponseGeneric(mensagem=f"Competição com nome '{nome}' e modalidade '{modalidade}' já existe.", status=400)
       nova_competicao = Competicao(nome=nome, modalidade=modalidade, status=StatusCompeticaoEnum.ABERTA)
       self.competicao_repository.salvar(nova_competicao)
       return ResponseGeneric(mensagem=f"Competição '{nome}' iniciada.", data={
           "id": nova_competicao.id,
           "nome": nova_competicao.nome,
           "modalidade": nova_competicao.modalidade,
           "status": nova_competicao.status
       }, status=201)
   
   def adicionar_resultado(self, competicao_id: int, atleta_nome: str, valor: float, unidade: str) -> ResponseGeneric:
       competicao = self.competicao_repository.buscar_por_id(competicao_id)
       if not competicao:
           return ResponseGeneric(mensagem="Competição não encontrada.", status=404)
       if competicao.status == "encerrada":
           return ResponseGeneric(mensagem="Competição já está encerrada. Não é possível adicionar resultados.", status=409)
       atleta = self.atleta_repository.buscar_por_nome(atleta_nome)
       if not atleta:
           atleta = self.atleta_repository.salvar(atleta_nome)
       # Verificação para modalidade de Lançamento de Dardos
       if competicao.modalidade == "LANCAMENTO_DARDO":
           tentativas = self.resultado_repository.buscar_por_competicao_e_atleta(competicao_id, atleta.id)
           if len(tentativas) >= 3:
               return ResponseGeneric(mensagem=f"O atleta {atleta.nome} já fez 3 tentativas nesta competição.", status=409)
           # Adiciona a nova tentativa
           resultado = Resultado(atleta_id=atleta.id, valor=valor, unidade=unidade)
           competicao.adicionar_resultado(resultado)
           self.competicao_repository.salvar(competicao)
           # Verifica o melhor resultado
           melhor_resultado = max(tentativas + [resultado], key=lambda r: r.valor)
           return ResponseGeneric(mensagem=f"Tentativa adicionada para o atleta {atleta.nome}. Melhor resultado até agora: {melhor_resultado.valor} {melhor_resultado.unidade}.", data={"competicao": competicao.nome, "atleta": atleta.nome, "valor": valor, "unidade": unidade}, status=200)
       # Outras modalidades (como 100m Rasos)
       else:
           if self.resultado_repository.buscar_por_competicao_e_atleta(competicao_id, atleta.id):
               return ResponseGeneric(mensagem=f"O atleta {atleta.nome} já participou desta competição.", status=409)
           resultado = Resultado(atleta_id=atleta.id, valor=valor, unidade=unidade)
           competicao.adicionar_resultado(resultado)
           self.competicao_repository.salvar(competicao)
           return ResponseGeneric(mensagem=f"Resultado adicionado para o atleta {atleta.nome} na competição {competicao.nome}", data={"competicao": competicao.nome, "atleta": atleta.nome, "valor": valor, "unidade": unidade}, status=200)
   def obter_ranking(self, competicao_id: int) -> ResponseGeneric:
       competicao = self.competicao_repository.buscar_por_id(competicao_id)
       if not competicao:
           return ResponseGeneric(mensagem="Competição não encontrada.", status=404)
       ranking = competicao.obter_ranking()  # Supondo que você tenha esse método na classe Competicao
       return ResponseGeneric(mensagem=f"Ranking da competição: {competicao.nome}", data=ranking, status=200)
   def finalizar_competicao(self, competicao_id: int) -> ResponseGeneric:
       competicao = self.competicao_repository.buscar_por_id(competicao_id)
       if not competicao:
           return ResponseGeneric(mensagem="Competição não encontrada.", status=404)
       competicao.finalizar()  # Certifique-se de que você tenha um método para finalizar a competição
       self.competicao_repository.salvar(competicao)
       ranking_final = competicao.obter_ranking()  # Novamente, supondo que você tenha esse método
       return ResponseGeneric(mensagem=f"Ranking final da competição: {competicao.nome}", data=ranking_final, status=200)