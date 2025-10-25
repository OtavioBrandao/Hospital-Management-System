
from hospital import Hospital

class HospitalFacade:

    "Fachada para simplificar a interface e facilitar o uso do sistema."

    def __init__(self, hospital = None):
        self._hospital = hospital or Hospital() # Singleton por trás

    # Mesmo que não esteja declarado na fachada, repassa chamadas para o hospital, ou seja posso utilizar pela fachada sem problemas
    def __getattr__(self, name):
        return getattr(self._hospital, name)

    # Pacientes
    def listar_pacientes(self):
        self._hospital.listarPacientes() 

    def detalhes_paciente(self, nome: str):
        self._hospital.mostrarPaciente(nome) 

    # Consultas
    def agendar(self, nome_paciente: str, dia: str, tipo_profissional: str):
        self._hospital.agendar_consulta(nome_paciente, dia, tipo_profissional)

    def remarcar(self, nome_paciente: str, indice_consulta: int, novo_dia: str):
        self._hospital.remarcar_consulta(nome_paciente, indice_consulta, novo_dia)

    def cancelar(self, nome_paciente: str, indice_consulta: int):
        self._hospital.cancelar_consulta(nome_paciente, indice_consulta)

    # Prontuário e receita
    def prontuario(self, nome_paciente: str, profissional: str, descricao: str):
        self._hospital.registrar_prontuario(nome_paciente, profissional, descricao)

    def receita(self, nome_paciente: str, profissional: str, medicamento: str, descricao: str, dosagem: str):
        self._hospital.registrar_receita(nome_paciente, profissional, medicamento, descricao, dosagem)

    def receitas(self, nome_paciente: str):
        self._hospital.listar_receitas(nome_paciente)

    # Faturamento (Strategy já está plugado por trás)
    def faturar(self, nome_paciente: str):
        self._hospital.faturar_paciente(nome_paciente)

    # Exames (polimorfismo dos profissionais já está por trás)
    def exame(self, nome_paciente: str, nome_profissional: str, codigo_exame: str):
        self._hospital.solicitar_exame(nome_paciente, nome_profissional, codigo_exame)

    # Leitos
    def alocar(self, nome_paciente: str):
        self._hospital.alocar_leito(nome_paciente)

    # Escalonamento
    def escalar(self, nome_funcionario: str, turno: str):
        self._hospital.escalonar_funcionario(nome_funcionario, turno)

    def ver_escalas(self):
        self._hospital.ver_escalonamento()

    # Estoque 
    def add_item_estoque(self, item: str, qtd: int):
        self._hospital.estoque.adicionar_item(item, qtd)

    def ver_estoque(self):
        self._hospital.estoque.mostrar_estoque()

    # Funcionários (Factory Method já existe por trás)
    def adicionar_funcionario(self, tipo: str, nome: str, registro: str,
                              especialidade: str | None = None,
                              email: str | None = None,
                              whatsapp: str | None = None):
        self._hospital.adicionar_funcionario(tipo, nome, registro, especialidade, email, whatsapp)

    def remover_funcionario(self, nome: str, registro: str | None = None):
        self._hospital.remover_funcionario(nome, registro)

    def listar_funcionarios(self):
        self._hospital.listar_funcionarios()

    # Emergências (Observer + Adapters já plugados por trás)
    def registrar_emergencia(self, nome_paciente: str, prioridade: str):
        self._hospital.emergencias.registrar_emergencia(nome_paciente, prioridade)

    def ver_emergencias(self):
        self._hospital.emergencias.ver_emergencias()

    def notificacoes_emergencia(self):
        self._hospital.mostrar_notificacoes_emergencia()

    # Relatórios (Template Method já plugado por trás)
    def relatorio_paciente(self, nome_paciente: str):
        self._hospital.gerar_pdf_paciente(nome_paciente)

    def relatorio_equipe(self):
        self._hospital.gerar_pdf_equipe()

    def relatorio_hospital(self):
        self._hospital.gerar_pdf_hospital()
