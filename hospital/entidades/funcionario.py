from abc import ABC, abstractmethod
from .paciente import Paciente
from .exame import EXAMES_DISPONIVEIS 

# Ver se é necessário fazer mais coisa aqui
class FuncionarioSaude(ABC):
    def __init__(self, nome, registro, email, whatsapp):
        self.nome = nome
        self.registro = registro
        self.email = email          
        self.whatsapp = whatsapp 
        self.exames_permitidos = [] # Cada filho definirá seus exames

    @abstractmethod
    def requisitarExame(self, paciente, nome_exame, restricao):
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
    def __init__(self, nome, registro, email, whatsapp, especialidade=None):
        super().__init__(nome, registro, email, whatsapp)
        self.especialidade = especialidade
        self.exames_permitidos = ["hemograma", "raio-x", "urina", "tomografia", "ecocardiograma",
        "eletrocardiograma", "ultrassom", "ressonancia", 
        "endoscopia", "colonoscopia", "biópsia", "cintilografia", 
        "angiografia", "densitometria", "papanicolau", "mamografia", 
        "teste_alergia"]

    def atenderPaciente(self, paciente):
        print(f"O médico {self.nome} está diagnosticando o paciente: {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Dr(a). {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"Exame '{nome_exame}' não pode ser solicitado por um Médico.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Dr(a). {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")

    def receitar_medicamento(self, paciente, medicamento, descricao, dosagem):
        paciente.adicionar_receita(self.nome, medicamento, descricao, dosagem)
        print(f"Dr(a). {self.nome} receitou {medicamento} para {paciente.nome}.")

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro, email, whatsapp):
        super().__init__(nome, registro, email, whatsapp)
        self.exames_permitidos = ["glicemia", "pressao"]

    def atenderPaciente(self, paciente):
        print(f"O enfermeiro {self.nome} está checando os sinais vitais do paciente {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Enfermeiro(a) {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"Exame '{nome_exame}' não pode ser solicitado por um Enfermeiro.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Enfermeiro(a) {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")

class Dentista(FuncionarioSaude):
    def __init__(self, nome, registro, email, whatsapp):
        super().__init__(nome, registro, email, whatsapp)
        self.exames_permitidos = ["radiografia_dentaria", "limpeza","tomografia"]

    def atenderPaciente(self, paciente):
        print(f"Dentista {self.nome} está fazendo uma análise bucal no paciente: {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Dentista {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"Exame '{nome_exame}' não pode ser solicitado por um Dentista.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Dentista {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")

class Psicologo(FuncionarioSaude):
    def __init__(self, nome, registro, email, whatsapp):
        super().__init__(nome, registro, email, whatsapp)
        self.exames_permitidos = ["encaminhamento"]
    
    def atenderPaciente(self, paciente):
        print(f"Psicólogo(a) {self.nome} está realizando uma sessão de terapia com o paciente {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        # Psicólogo tem um comportamento diferente (polimorfismo)
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Psicólogo(a) {self.nome} gerou um '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"'{nome_exame}' não é uma ação válida para um Psicólogo.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Psicólogo(a) {self.nome} gerou um '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")

class Nutricionista(FuncionarioSaude):
    def __init__(self, nome, registro, email, whatsapp):
        super().__init__(nome, registro, email, whatsapp)
        self.exames_permitidos = ["teste_alergia"]

    def atenderPaciente(self, paciente):
        print(f"Nutricionista {self.nome} está avaliando a dieta de {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Nutricionista {self.nome} solicitou '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"Exame '{nome_exame}' não pode ser solicitado por Nutricionista.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Nutricionista {self.nome} solicitou '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")
            
class Fisioterapeuta(FuncionarioSaude):
    def __init__(self, nome, registro, email, whatsapp):
        super().__init__(nome, registro, email, whatsapp)
        self.exames_permitidos = ["encaminhamento"]

    def atenderPaciente(self, paciente):
        print(f"Fisioterapeuta {self.nome} está avaliando a mobilidade de {paciente.nome}")

    def requisitarExame(self, paciente, nome_exame, restricao):
        try:
            if restricao is True:
                if nome_exame in self.exames_permitidos:
                    exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                    paciente.solicitar_exame(exame_obj)
                    print(f"Fisioterapeuta {self.nome} gerou um '{exame_obj}' para {paciente.nome}.")
                else:
                    print(f"'{nome_exame}' não é uma ação válida para Fisioterapeuta.")
            else:
                exame_obj = EXAMES_DISPONIVEIS[nome_exame]
                paciente.solicitar_exame(exame_obj)
                print(f"Fisioterapeuta {self.nome} solicitou o exame '{exame_obj}' para {paciente.nome}.")
        except KeyError:
            print(f"Erro: Código de exame '{nome_exame}' inválido.")


# Factory Method Design Pattern usado aqui para criar funcionários de saúde
class FuncionarioSaudeFactory(ABC):
    @abstractmethod
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        pass

class MedicoFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):

        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
    
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um médico.")
        if registro.startswith("CRM") and especialidade:
            pass
        else:
            raise ValueError("Registro de médico deve começar com 'CRM' e especialidade é obrigatória.")

        return Medico(nome, registro, email, whatsapp, especialidade)

class EnfermeiroFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um enfermeiro.")      
        if not registro.startswith("COREN"):
            raise ValueError("Registro de enfermeiro deve começar com 'COREN'.")

        return Enfermeiro(nome, registro, email, whatsapp)

class DentistaFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um dentista.")      
        if not registro.startswith("CRO"):
            raise ValueError("Registro de dentista deve começar com 'CRO'.")
        
        return Dentista(nome, registro, email, whatsapp)  

class PsicologoFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um psicólogo.")
        if not registro.startswith("CRP"):
            raise ValueError("Registro de psicólogo deve começar com 'CRP'.")

        return Psicologo(nome, registro, email, whatsapp)

class NutricionistaFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um nutricionista.")
        if not registro.startswith("CRN"):
            raise ValueError("Registro de nutricionista deve começar com 'CRN'.")

        return Nutricionista(nome, registro, email, whatsapp)

class FisioterapeutaFactory(FuncionarioSaudeFactory):
    def criar_funcionario(self, nome, registro, especialidade, email, whatsapp):
        if len(whatsapp) < 12:
            raise ValueError("Número de WhatsApp inválido. Verifique se o código do país está incluído e o DDD está correto.")
        if ".com" not in email or "@" not in email:
            raise ValueError("Endereço de email inválido. Verifique o formato do email.")
        if not nome or not registro:
            raise ValueError("Nome e registro são obrigatórios para criar um fisioterapeuta.")
        if not registro.startswith("CREFITO"):
            raise ValueError("Registro de fisioterapeuta deve começar com 'CREFITO'.")

        return Fisioterapeuta(nome, registro, email, whatsapp)

class GerenciadorFuncionariosSaude:
    factories = {
        "medico": MedicoFactory(),
        "enfermeiro": EnfermeiroFactory(),
        "dentista": DentistaFactory(),
        "psicologo": PsicologoFactory(),
        "nutricionista": NutricionistaFactory(),
        "fisioterapeuta": FisioterapeutaFactory()
    }

    @classmethod
    def criar_funcionario(cls, tipo, nome, registro, especialidade=None, email=None, whatsapp=None):
        factory = cls.factories.get(tipo.lower())
        if not factory:
            raise ValueError(f"Tipo de funcionário de saúde desconhecido: {tipo}")
        return factory.criar_funcionario(nome, registro, especialidade, email, whatsapp)
