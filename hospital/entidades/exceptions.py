
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
        super().__init__(f"Paciente '{nome_paciente}' não foi encontrado no sistema.")


class PacienteDuplicadoException(PacienteException):
    """Tentativa de cadastrar paciente que já existe"""
    pass

class DadosInvalidosException(PacienteException):
    """Dados do paciente são inválidos"""
    pass

class CampoObrigatorioException(PacienteException):
    """Campo obrigatório não foi preenchido"""
    pass

class DocumentoInvalidoException(PacienteException):
    """CPF ou Cartão SUS inválido"""
    pass


# ============= FUNCIONÁRIOS =============
class FuncionarioException(SistemaHospitalarException):
    """Exceção base para funcionários"""
    pass

class ProfissionalNaoEncontradoException(FuncionarioException):
    """Profissional não existe no sistema"""
    pass

class RegistroInvalidoException(FuncionarioException):
    """Registro profissional inválido"""
    pass

class ContatoInvalidoException(FuncionarioException):
    """Email ou WhatsApp inválido"""
    pass

class PermissaoNegadaException(FuncionarioException):
    """Funcionário não tem permissão para esta ação"""
    pass

class FuncionarioDuplicadoException(FuncionarioException):
    """Tentativa de cadastrar funcionário que já existe"""
    pass


# ============= EXAMES =============
"""Será feita com KeyError pois são dicionários"""


# ============= FATURAMENTO =============
class FaturamentoException(SistemaHospitalarException):
    """Exceção base para faturamento"""
    pass

class PlanoNaoEncontradoException(FaturamentoException):
    """Tipo de plano não reconhecido"""
    pass

class ConvenioNaoEncontradoException(FaturamentoException):
    """Convênio não reconhecido"""
    pass

class DadosFaturamentoIncompletosException(FaturamentoException):
    """Faltam dados para calcular faturamento"""
    pass


# ============= HOSPITAL =============
class HospitalException(SistemaHospitalarException):
    """Exceção base para operações do hospital"""
    pass

class LeitoIndisponivelException(HospitalException):
    """Não há leitos disponíveis"""
    pass

class ConsultaNaoEncontradaException(HospitalException):
    """Índice de consulta inválido"""
    pass


# ============= EMERGÊNCIAS =============
class EmergenciaException(SistemaHospitalarException):
    """Exceção base para emergências"""
    pass

class PrioridadeInvalidaException(EmergenciaException):
    """Prioridade de emergência inválida"""
    pass

class TurnoInvalidoException(EmergenciaException):
    """Turno inválido"""
    pass

class NotificacaoFalhouException(EmergenciaException):
    """Notificação não pôde ser enviada"""
    pass


# ============= RELATÓRIOS =============
class RelatorioException(SistemaHospitalarException):
    """Exceção base para geração de relatórios"""
    pass

class DadosRelatorioInvalidosException(RelatorioException):
    """Dados para relatório estão incompletos"""
    pass

class ErroGeracaoPDFException(RelatorioException):
    """PDF não pode ser gerado"""
    pass