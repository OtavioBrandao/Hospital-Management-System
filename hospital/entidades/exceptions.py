
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
        super().__init__(f"ERRO: Paciente '{nome_paciente}' não foi encontrado no sistema.")

# Ainda não utilizado, mas pode ser útil futuramente
class PacienteDuplicadoException(PacienteException):
    """Tentativa de cadastrar paciente que já existe"""
    def __init__(self, nome_paciente: str):
        self.nome_paciente = nome_paciente
        super().__init__(f"ERRO: Paciente '{nome_paciente}' já está cadastrado no sistema.")
# Ainda não utilizado, mas pode ser útil futuramente
class DadosInvalidosException(PacienteException):
    """Dados do paciente são inválidos"""
    def __init__(self, campo: str):
        self.campo = campo
        super().__init__(f"ERRO: Dados inválidos para o campo '{campo}'.")
# Ainda não utilizado, mas pode ser útil futuramente
class CampoObrigatorioException(PacienteException):
    """Campo obrigatório não foi preenchido"""
    def __init__(self, campo: str):
        self.campo = campo
        super().__init__(f"ERRO: Campo obrigatório '{campo}' não foi preenchido.")
# Ainda não utilizado, mas pode ser útil futuramente
class DocumentoInvalidoException(PacienteException):
    """CPF ou Cartão SUS inválido"""
    def __init__(self, documento: str):
        self.documento = documento
        super().__init__(f"ERRO: Documento '{documento}' é inválido.")


# ============= FUNCIONÁRIOS =============
class FuncionarioException(SistemaHospitalarException):
    """Exceção base para funcionários"""
    pass

class ProfissionalNaoEncontradoException(FuncionarioException):
    """Profissional não existe no sistema"""
    def __init__(self, nome_profissional: str):
        self.nome_profissional = nome_profissional
        super().__init__(f"ERRO: Profissional '{nome_profissional}' não foi encontrado no sistema.")
# Ainda não utilizado, mas pode ser útil futuramente
class RegistroInvalidoException(FuncionarioException):
    """Registro profissional inválido"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class ContatoInvalidoException(FuncionarioException):
    """Email ou WhatsApp inválido"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class PermissaoNegadaException(FuncionarioException):
    """Funcionário não tem permissão para esta ação"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class FuncionarioDuplicadoException(FuncionarioException):
    """Tentativa de cadastrar funcionário que já existe"""
    pass


# ============= EXAMES =============
"""Será feita com KeyError pois são dicionários"""


# ============= FATURAMENTO =============
class FaturamentoException(SistemaHospitalarException):
    """Exceção base para faturamento"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class PlanoNaoEncontradoException(FaturamentoException):
    """Tipo de plano não reconhecido"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class ConvenioNaoEncontradoException(FaturamentoException):
    """Convênio não reconhecido"""
    pass
# Ainda não utilizado, mas pode ser útil futuramente
class DadosFaturamentoIncompletosException(FaturamentoException):
    """Faltam dados para calcular faturamento"""
    pass


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