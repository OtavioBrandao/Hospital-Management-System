from datetime import datetime
from enum import Enum

# Informações adicionais sobre o paciente

class PesoAlturaIdade:
    def __init__(self, peso, altura, idade):
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.imc = peso / (altura ** 2)

    def __str__(self):
        return f"Peso: {self.peso} kg, Altura: {self.altura} cm, IMC: {self.imc:.2f}"
    
class TipoSanguineo(Enum):
    A_POSITIVO = "A+"
    A_NEGATIVO = "A-"
    B_POSITIVO = "B+"
    B_NEGATIVO = "B-"
    AB_POSITIVO = "AB+"
    AB_NEGATIVO = "AB-"
    O_POSITIVO = "O+"
    O_NEGATIVO = "O-"

    def __str__(self):
        return self.value

class Genero(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    OUTRO = "Outro"
    NAO_INFORMADO = "Não Informado"

    def __str__(self):
        return self.value

class TipoPlano(Enum):
    SUS = "SUS"
    PARTICULAR = "Particular"
    CONVENIO = "Convênio"
    NAO_INFORMADO = "Não Informado"

    def __str__(self):
        return self.value
    
class ContatoEmergencia:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Contato de Emergência: {self.nome} - {self.telefone}"

class HistoricoMedico:
    def __init__(self):
        self.alergias = []
        self.doencas_cronicas = []
        self.cirurgias = []
        self.medicamentos = []
        self.observacoes = ""

    def adicionar_alergia(self, alergia):
        self.alergias.append(alergia)
    
    def adicionar_doenca_cronica(self, doenca):
        self.doencas_cronicas.append(doenca)

    def adicionar_cirurgia(self, cirurgia):
        self.cirurgias.append(cirurgia)

    def adicionar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)
    
    def adicionar_observacao(self, observacao):
        self.observacoes += observacao + "\n"

class Prontuario:
    def __init__(self, profissional, descricao):
        self.profissional = profissional
        self.descricao = descricao
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M')} - {self.profissional}: {self.descricao}"

class Paciente:
    def __init__(self, nome, cpf=None, cartao_sus=None):

        # Novos atributos complexos
        self.nome = nome
        self._cpf = None
        self._cartao_sus = None
        self.idade = None
        self.altura = None
        self.peso = None
        self.imc = None
        self.tipo_sanguineo = None
        self.genero = None
        self.tipo_plano = None
        self.contato_emergencia = None
        self.historico_medico = HistoricoMedico()
        
        if cpf:
            self.cpf = cpf
        if cartao_sus:
            self.cartao_sus = cartao_sus
        
        # Informações do Hospital sobre o paciente
        self.prontuarios = []
        self.receitas = []
        self.exames = []
        self.consultas = []

    @property
    def cpf(self):
        #Método "get" do cpf
        return self._cpf
    @cpf.setter
    def cpf(self, valor):
        """Este é o 'setter' para o CPF. Valida o valor antes de atribuir."""
        # Garantir que o CPF tenha 5 dígitos numéricos
        if valor and len(valor) == 5 and valor.isdigit():
            self._cpf = valor
        else:
            print(f"Aviso: CPF '{valor}' é inválido. Deve conter 5 dígitos numéricos.")
            self._cpf = None

    @property
    def cartao_sus(self):
        """Getter para o Cartão SUS."""
        return self._cartao_sus

    @cartao_sus.setter
    def cartao_sus(self, valor):
        """Setter para o Cartão SUS com validação."""
        # Garantir que o Cartão SUS tenha 5 dígitos
        if valor and len(valor) == 5 and valor.isdigit():
            self._cartao_sus = valor
        else:
            print(f"Aviso: Cartão SUS '{valor}' é inválido. Deve conter 5 dígitos numéricos.")
            self._cartao_sus = None

    def adicionar_prontuario(self, profissional, descricao):
        prontuario = Prontuario(profissional, descricao)
        self.prontuarios.append(prontuario)

    def adicionar_receita(self, profissional, medicamento, descricao, dosagem):
        receita_completa = f"Receita por {profissional}:\n Medicamento: {medicamento}\n Descrição: {descricao}\n Dosagem: {dosagem}\n"
        self.receitas.append(receita_completa)
        print("Receita adicionada.")

    def solicitar_exame(self, exame):
        self.exames.append(exame)

    def agendar_consulta(self, dia, profissional):
        self.consultas.append((dia, profissional))

    def __str__(self):
        return f"Paciente: {self.nome}"
