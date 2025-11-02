
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
# Ainda não utilizado, mas pode ser útil futuramente
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
# Ainda não utilizado, mas pode ser útil futuramente
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
# Ainda não utilizado, mas pode ser útil futuramente
class LeitoIndisponivelException(HospitalException):
    """Não há leitos disponíveis"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class ConsultaNaoEncontradaException(HospitalException):
    """Índice de consulta inválido"""
    pass

# ============= RELATÓRIOS =============
class RelatorioException(SistemaHospitalarException):
    """Exceção base para geração de relatórios"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class DadosRelatorioInvalidosException(RelatorioException):
    """Dados para relatório estão incompletos"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class ErroGeracaoPDFException(RelatorioException):
    """PDF não pode ser gerado"""
    pass

"""EM ALGUNS LUGARES UTILIZAREMOS KEYERROR PARA COISAS QUE SÃO DICIONÁRIOS GERALMENTE, EXEMPLO NOS EXAMES"""