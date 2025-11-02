
# ============= EXCEÇÕES BASE =============
class SistemaHospitalarException(Exception):
    """Exceção base para todo o sistema"""
    pass

# ============= PACIENTES =============
class PacienteException(SistemaHospitalarException):
    """Exceção base para erros relacionados a pacientes"""
    pass

class PacienteNaoEncontradoException(PacienteException):
    """Paciente não existe no sistema"""
    def __init__(self, nome_paciente: str):
        self.nome_paciente = nome_paciente
        super().__init__(f"❌ ERRO: Paciente '{nome_paciente}' não foi encontrado no sistema.")

class PacienteDuplicadoException(PacienteException):
    """Tentativa de cadastrar paciente que já existe"""
    def __init__(self, nome_paciente: str):
        self.nome_paciente = nome_paciente
        super().__init__(f"❌ ERRO: Paciente '{nome_paciente}' já está cadastrado no sistema.")

class DadosInvalidosException(PacienteException):
    """Dados do paciente são inválidos"""
    def __init__(self, campo: str):
        self.campo = campo
        super().__init__(f"❌ ERRO: {campo} inválido(a), será definido como 'Não Informado'.")

class CampoObrigatorioException(PacienteException):
    """Campo obrigatório não foi preenchido"""
    def __init__(self, campo: str):
        self.campo = campo
        super().__init__(f"❌ ERRO: Campo obrigatório '{campo}' não foi preenchido.")
# Ainda não utilizado, mas pode ser útil futuramente
class DocumentoInvalidoException(PacienteException):
    """CPF ou Cartão SUS inválido"""
    def __init__(self, documento: str):
        self.documento = documento
        super().__init__(f"❌ERRO: Documento '{documento}' é inválido.")


# ============= FUNCIONÁRIOS =============
class FuncionarioException(SistemaHospitalarException):
    """Exceção base para funcionários"""
    pass

class ProfissionalNaoEncontradoException(FuncionarioException):
    """Profissional não existe no sistema"""
    def __init__(self, nome_profissional: str):
        self.nome_profissional = nome_profissional
        super().__init__(f"❌ ERRO: Profissional '{nome_profissional}' não foi encontrado no sistema.")

class RegistroInvalidoException(FuncionarioException):
    """Registro profissional inválido"""
    def __init__(self, registro: str):
        self.registro = registro
        super().__init__(f"❌ ERRO: Registro profissional é inválido. '{registro}' ")

class ContatoInvalidoException(FuncionarioException):
    """Email ou WhatsApp inválido"""
    def __init__(self, contato: str):
        self.contato = contato
        super().__init__(f"❌ ERRO: Contato é inválido. ('{contato}')")
# Ainda não utilizado, mas pode ser útil futuramente
class PermissaoNegadaException(FuncionarioException):
    """Funcionário não tem permissão para esta ação"""
    def __init__(self, acao: str):
        self.acao = acao
        super().__init__(f"❌ ERRO: Funcionário não tem permissão para a ação '{acao}'.")

class FuncionarioDuplicadoException(FuncionarioException):
    """Tentativa de cadastrar funcionário que já existe"""
    def __init__(self, nome_funcionario: str):
        self.nome_funcionario = nome_funcionario
        super().__init__(f"❌ ERRO: Funcionário '{nome_funcionario}' já está cadastrado no sistema.")


# ============= EXAMES =============
"""Será feita com KeyError pois são dicionários"""


# ============= HOSPITAL =============
class HospitalException(SistemaHospitalarException):
    """Exceção base para operações do hospital"""
    pass

class LeitoIndisponivelException(HospitalException): 
    def __init__(self):
        super().__init__(f"❌ ERRO: Todos os leitos estão ocupados.")

class EstoqueInvalidoException(HospitalException):
    """Item de estoque inválido"""
    def __init__(self, quantidade: int, item: str):
        self.quantidade = quantidade
        self.item = item
        super().__init__(f"❌ ERRO: Quantidade de estoque '{quantidade}' para o item '{item}' é inválido ou insuficiente.")

class EstoqueMaximoException(HospitalException):
    """Estoque atingiu o limite máximo"""
    def __init__(self, item: str):
        self.item = item
        super().__init__(f"❌ ERRO: Estoque do item '{item}' só pode ter até 1000 unidades.")
