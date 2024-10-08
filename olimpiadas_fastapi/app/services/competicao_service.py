from app.repositories.competicao_repository import CompeticaoRepository
from app.models.competicao import Competicao
from app.models.resultado import Resultado

class CompeticaoService:
    def _init_(self):
        self.repository = CompeticaoRepository()

    def criar_competicao(self, nome: str, tipo: str) -> Competicao:
        competicao = Competicao(nome=nome, tipo=tipo)
        self.repository.salvar(competicao)
        return {"status": 200, "mensagem": "Competição criada com sucesso.", "competicao": competicao}

    def adicionar_resultado(self, competicao_id: int, atleta_id: int, valor: float, fase: int):
        competicao = self.repository.buscar_por_id(competicao_id)
        if not competicao:
            raise Exception("Competição não encontrada.")

        if competicao.encerrada:
            raise Exception("Competição já está encerrada, não é possível adicionar resultados.")

        resultado = Resultado(atleta_id=atleta_id, valor=valor, fase=fase)
        competicao.adicionar_resultado(resultado)
        self.repository.salvar(competicao)
        return {"status": 200, "mensagem": "Resultado adicionado com sucesso.", "resultado": resultado}

    def obter_ranking(self, competicao_id: int):
        competicao = self.repository.buscar_por_id(competicao_id)
        if not competicao:
            raise Exception("Competição não encontrada.")

        ranking = competicao.obter_ranking()
        return {"status": 200, "ranking": ranking}

    def finalizar_competicao(self, competicao_id: int):
        competicao = self.repository.buscar_por_id(competicao_id)
        if not competicao:
            raise Exception("Competição não encontrada.")

        competicao.finalizar()
        self.repository.salvar(competicao)
        return {"status": 200, "mensagem": "Competição finalizada com sucesso."}