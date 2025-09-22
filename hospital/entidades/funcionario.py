from abc import ABC, abstractmethod
from .paciente import Paciente
from .exame import EXAMES_DISPONIVEIS 

# Ver se é necessário fazer mais coisa aqui
class FuncionarioSaude(ABC):
    def __init__(self, nome, registro):
        self.nome = nome
        self.registro = registro
        self.exames_permitidos = [] # Cada filho definirá seus exames
        #espaço para implementar queixa para cada funcionario

    @abstractmethod
    def requisitarExame(self, paciente, nome_exame):
        pass
    
    @abstractmethod
    def atenderPaciente(self, paciente):
        pass

    def registrarProntuario(self, paciente, descricao):
        paciente.adicionar_prontuario(self.nome, descricao)
        print("Prontuário registrado")

    def __str__(self):
        return f"{self.nome} ({self.registro})"

class Medico(FuncionarioSaude):
    def __init__(self, nome, registro, especialidade=None):
        super().__init__(nome, registro)
        self.especialidade = especialidade
        # Define os exames que o médico pode solicitar
        self.exames_permitidos = ["hemograma", "raio-x", "urina","tomografia"]

    def atenderPaciente(self, paciente):
        print(f"O médico {self.nome} está diagnosticando o paciente: {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame):
        if nome_exame in self.exames_permitidos:
            exame_obj = EXAMES_DISPONIVEIS[nome_exame]
            paciente.solicitar_exame(exame_obj)
            print(f"Dr(a). {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        else:
            print(f"Exame '{nome_exame}' não pode ser solicitado por um Médico.")

    def receitar_medicamento(self, paciente, receita):
        paciente.adicionar_receita(receita)

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)
        self.exames_permitidos = ["glicemia", "pressao"]

    def atenderPaciente(self, paciente):
        print(f"O enfermeiro {self.nome} está checando os sinais vitais do paciente {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame):
        if nome_exame in self.exames_permitidos:
            exame_obj = EXAMES_DISPONIVEIS[nome_exame]
            paciente.solicitar_exame(exame_obj)
            print(f"Enfermeiro(a) {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        else:
            print(f"Exame '{nome_exame}' não pode ser solicitado por um Enfermeiro.")

class Dentista(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)
        self.exames_permitidos = ["radiografia_dentaria", "limpeza","tomografia"]

    def atenderPaciente(self, paciente):
        print(f"A dentista {self.nome} está fazendo uma análise bucal no paciente: {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame):
        if nome_exame in self.exames_permitidos:
            exame_obj = EXAMES_DISPONIVEIS[nome_exame]
            paciente.solicitar_exame(exame_obj)
            print(f"Dentista {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        else:
            print(f"Exame '{nome_exame}' não pode ser solicitado por um Dentista.")

class Psicologo(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)
        self.exames_permitidos = ["encaminhamento"]
    
    def atenderPaciente(self, paciente):
        print(f"A psicóloga {self.nome} está realizando uma sessão de terapia com o paciente {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame):
        # Psicólogo tem um comportamento diferente (polimorfismo)
        if nome_exame in self.exames_permitidos:
            exame_obj = EXAMES_DISPONIVEIS[nome_exame]
            print(f"Psicóloga {self.nome} gerou um '{exame_obj}' para {paciente.nome}.")
        else:
            print(f"'{nome_exame}' não é uma ação válida para um Psicólogo.")
