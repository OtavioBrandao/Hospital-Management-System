from datetime import datetime
from enum import Enum
import random

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

class Convenio(Enum):
    UNIMED = "Unimed"
    AMIL = "Amil"
    HAPVIDA = "Hapvida"
    BRADESCO = "Bradesco"
    SULAMERICA = "SulAmérica"
    SEM_CONVENIO = "Sem Convênio"

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
    
class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"({self.ddd}) {self.numero}"
    
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

    def resumo(self):
        partes = []
        if self.alergias:
            partes.append("Alergias: " + ", ".join(self.alergias))
        if self.doencas_cronicas:
            partes.append("Doenças Crônicas: " + ", ".join(self.doencas_cronicas))
        if self.cirurgias:
            partes.append("Cirurgias: " + ", ".join(self.cirurgias))
        if self.medicamentos:
            partes.append("Medicamentos: " + ", ".join(self.medicamentos))
        if self.observacoes.strip():
            partes.append("Observações: " + self.observacoes.strip())
        return "\n".join(partes) if partes else "Nenhum histórico registrado"

class Prontuario:
    def __init__(self, profissional, descricao):
        self.profissional = profissional
        self.descricao = descricao
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M')} - {self.profissional}: {self.descricao}"

class Paciente:
    def __init__(self, nome, cpf=None, cartao_sus=None):
        self.nome = nome
        self._cpf = None
        self._cartao_sus = None
        self.idade = None
        self.altura = None
        self.peso = None
        self.tipo_sanguineo = None
        self.genero = None
        self.tipo_plano = None
        self.tipo_convenio = None
        self.telefone = None
        self.contato_emergencia = None
        self.historico_medico = HistoricoMedico()
        
        if cpf:
            self.cpf = cpf
        if cartao_sus:
            self.cartao_sus = cartao_sus
        
        self.prontuarios = []
        self.receitas = []
        self.exames = []
        self.consultas = []

    @property
    def cpf(self):
        #Método "get" do cpf
        return self._cpf
    
    @property
    def cartao_sus(self):
        return self._cartao_sus
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def contato_emergencia(self):
        return self._contato_emergencia
    
    @property
    def altura(self):
        return self._altura
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def imc(self):
        if self._peso and self._altura:
            h = self._altura / 100.0
            return self._peso / (h*h)
        return None
    
    @property
    def tipo_sanguineo(self):
        return self._tipo_sanguineo

    @property
    def genero(self):
        return self._genero

    @property
    def tipo_plano(self):
        return self._tipo_plano

    @property
    def tipo_convenio(self):
        return self._tipo_convenio

    @telefone.setter
    def telefone(self, valor):
        if valor is None:
            self._telefone = None
            return
        if isinstance(valor, Telefone):
            self._telefone = valor
            return
        if isinstance(valor, str) and valor.isdigit() and 10 <= len(valor) <= 11:
            self._telefone = Telefone(valor[:2], valor[2:])
            return
        print("Aviso: telefone inválido."); self._telefone = None

    @contato_emergencia.setter
    def contato_emergencia(self, valor):
        if valor is None:
            self._contato_emergencia = None; return
        if isinstance(valor, ContatoEmergencia):
            self._contato_emergencia = valor; return
        # aceitar tupla: (nome, "DDD+NUM") ou (nome, Telefone)
        if isinstance(valor, tuple) and len(valor) == 2:
            nome, tel = valor
            if isinstance(tel, Telefone):
                self._contato_emergencia = ContatoEmergencia(nome, tel); return
            if isinstance(tel, str) and tel.isdigit() and 10 <= len(tel) <= 11:
                self._contato_emergencia = ContatoEmergencia(nome, Telefone(tel[:2], tel[2:])); return
        print("Aviso: contato_emergencia inválido."); self._contato_emergencia = None

    @idade.setter
    def idade(self, valor):
        if valor is None:  
            self._idade = None
            return
        if isinstance(valor, int) and valor > 0:
            self._idade = valor
        else:
            print(f"Aviso: Idade '{valor}' é inválida. Deve ser um número inteiro positivo.")
            self._idade = None

    @altura.setter
    def altura(self, valor):
        if valor is None: 
            self._altura = None
            return
        if isinstance(valor, (int, float)) and 50 <= valor <= 250:
            self._altura = valor
        else:
            print(f"Aviso: Altura '{valor}' é inválida. Deve estar entre 50 e 250 cm.")
            self._altura = None  

    @peso.setter
    def peso(self, valor):
        if valor is None: 
            self._peso = None
            return
        if isinstance(valor, (int, float)) and 2 <= valor <= 300:
            self._peso = valor
        else:
            print(f"Aviso: Peso '{valor}' é inválido. Deve estar entre 2 e 300 kg.")
            self._peso = None

    @cpf.setter
    def cpf(self, valor):
        if valor is None: 
            self._cpf = None
            return
        if isinstance(valor, str):
            # Aceita CPF de 5 dígitos ou ID temporário TMP+5 dígitos
            if (len(valor) == 5 and valor.isdigit()) or (len(valor) == 8 and valor.startswith('TMP') and valor[3:].isdigit()):
                self._cpf = valor
                return
        print(f"Aviso: CPF '{valor}' é inválido. Deve conter 5 dígitos numéricos ou formato TMP+5 dígitos.")
        self._cpf = None

    @cartao_sus.setter
    def cartao_sus(self, valor):
        if valor is None: 
            self._cartao_sus = None
            return
        if isinstance(valor, str) and len(valor) == 5 and valor.isdigit():
            self._cartao_sus = valor
        else:
            print(f"Aviso: Cartão SUS '{valor}' é inválido. Deve conter 5 dígitos numéricos.")
            self._cartao_sus = None

    @tipo_sanguineo.setter
    def tipo_sanguineo(self, valor):
        if valor is None:
            self._tipo_sanguineo = None
            return
        if isinstance(valor, str):
            try:
                self._tipo_sanguineo = TipoSanguineo[valor.upper()]
            except KeyError:
                print(f"Tipo sanguíneo inválido: {valor}")
                self._tipo_sanguineo = None
        elif isinstance(valor, TipoSanguineo):
            self._tipo_sanguineo = valor
        else:
            self._tipo_sanguineo = None

    @genero.setter
    def genero(self, valor):
        if valor is None:
            self._genero = None
            return
        if isinstance(valor, str):
            try:
                self._genero = Genero[valor.upper()]
            except KeyError:
                print(f"Gênero inválido: {valor}")
                self._genero = None
        elif isinstance(valor, Genero):
            self._genero = valor
        else:
            self._genero = None

    @tipo_plano.setter
    def tipo_plano(self, valor):
        if valor is None:
            self._tipo_plano = None
            return
        if isinstance(valor, str):
            try:
                valor_processado = valor.upper().replace('Ê', 'E')  # Convênio -> CONVENIO
                self._tipo_plano = TipoPlano[valor_processado]
            except KeyError:
                print(f"Tipo de plano inválido: {valor}")
                self._tipo_plano = TipoPlano.NAO_INFORMADO
        elif isinstance(valor, TipoPlano):
            self._tipo_plano = valor
        else:
            self._tipo_plano = TipoPlano.NAO_INFORMADO

    @tipo_convenio.setter
    def tipo_convenio(self, valor):
        if valor is None:
            self._tipo_convenio = None
            return
        if isinstance(valor, str):
            try:
                valor_processado = valor.upper().replace('É', 'E')  # SulAmérica -> SULAMERICA
                self._tipo_convenio = Convenio[valor_processado]
            except KeyError:
                print(f"Tipo de convênio inválido: {valor}")
                self._tipo_convenio = None
        elif isinstance(valor, Convenio):
            self._tipo_convenio = valor
        else:
            self._tipo_convenio = None


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

# Design Pattern Builder parar criar pacientes de forma mais organizada, sendo ele complexo ou simples.
class PacienteBuilder:

    def __init__(self):
        self.resetar()

    def resetar(self):
        self.nome = None
        self._cpf = None
        self._cartao_sus = None
        self._idade = None
        self._altura = None
        self._peso = None
        self._imc = None
        self._tipo_sanguineo = None
        self._genero = None
        self._tipo_plano = None
        self._tipo_convenio = None
        self._contato_emergencia = None
        self._telefone = None
        self.historico_medico = None
        return self

    # Definição dos campos obrigatórios do paciente. Caso não tenha o CPF, preencher com nada e ele vai gerar um ID temporário que substituirá o CPF temporariamente.

    def com_nome(self, nome):
        self.nome = nome
        return self
    
    def com_cpf(self, cpf):
        if cpf is None or cpf.strip() == "":
            self._cpf = self._gerar_id_temporario()
        else:
            self._cpf = cpf
        return self
    
    def _gerar_id_temporario(self):
        """Gera um ID temporário no formato TMP12345"""
        return f"TMP{random.randint(10000, 99999)}"
    
    # Definição dos campos opcionais, que podem ser preenchidos depois se necessário, com algumas validações

    def com_tipo_plano(self, tipo_plano):
        if isinstance(tipo_plano, str):
            try:
                tipo_plano = TipoPlano[tipo_plano.upper()]
            except KeyError:
                print(f"Tipo de plano inválido: {tipo_plano}. Deve ser um dos seguintes: {[t.name for t in TipoPlano]}")
                tipo_plano = None

        if tipo_plano is None:
            tipo_plano = TipoPlano.NAO_INFORMADO


        self._tipo_plano = tipo_plano
        return self

    def com_tipo_convenio(self, tipo_convenio):
        if isinstance(tipo_convenio, str):
            try:
                valor_processado = tipo_convenio.upper().replace('É', 'E')  # SulAmérica -> SULAMERICA
                tipo_convenio = Convenio[valor_processado]
            except KeyError:
                print(f"Tipo de convênio inválido: {tipo_convenio}. Deve ser um dos seguintes: {[c.name for c in Convenio]}")
                tipo_convenio = None

        self._tipo_convenio = tipo_convenio
        return self

    def com_cartao_sus(self, cartao_sus):
        self._cartao_sus = cartao_sus
        return self
    
    def com_idade(self, idade):
        self._idade = idade
        return self
    
    def com_altura(self, altura):
        self._altura = altura
        return self
    
    def com_peso(self, peso):
        self._peso = peso
        return self
    
    TS = {
    "A+": "A_POSITIVO", "A-": "A_NEGATIVO",
    "B+": "B_POSITIVO", "B-": "B_NEGATIVO",
    "AB+": "AB_POSITIVO", "AB-": "AB_NEGATIVO",
    "O+": "O_POSITIVO", "O-": "O_NEGATIVO",
    }
    
    def com_tipo_sanguineo(self, tipo_sanguineo):
        if isinstance(tipo_sanguineo, str):
            S = self.TS.get(tipo_sanguineo.upper(), tipo_sanguineo)
            try:
                tipo_sanguineo = TipoSanguineo[S]
            except KeyError:
                print(f"Tipo sanguíneo inválido: {tipo_sanguineo}. Deve ser um dos seguintes: {[t.name for t in TipoSanguineo]}")
                tipo_sanguineo = None

        self._tipo_sanguineo = tipo_sanguineo
        return self
    
    def com_genero(self, genero):
        if isinstance(genero, str):
            try:
                genero = Genero[genero.upper()]
            except KeyError:
                print(f"Gênero inválido: {genero}. Deve ser um dos seguintes: {[g.name for g in Genero]}")
                genero = None

        self._genero = genero
        return self
    
    def com_contato_emergencia(self, contato_emergencia):
        self._contato_emergencia = contato_emergencia
        return self
    
    def com_telefone(self, telefone):
        self._telefone = telefone
        return self

    def com_historico_medico(self, historico_medico):
        self.historico_medico = historico_medico or HistoricoMedico()
        return self
    
    def construir(self) -> Paciente:
        if not self.nome or self.nome.strip() == "":
            raise ValueError("O nome do paciente é obrigatório.")
        
        # Gerar ID temporário se CPF não foi fornecido
        cpf_final = self._cpf if self._cpf is not None else self._gerar_id_temporario()

        paciente = Paciente(
            nome=self.nome,
            cpf=cpf_final,
            cartao_sus=self._cartao_sus
        )
        
        paciente.idade = self._idade
        paciente.altura = self._altura
        paciente.peso = self._peso
        paciente.tipo_sanguineo = self._tipo_sanguineo
        paciente.genero = self._genero
        paciente.tipo_plano = self._tipo_plano
        paciente.tipo_convenio = self._tipo_convenio
        paciente.contato_emergencia = self._contato_emergencia
        paciente.telefone = self._telefone
        paciente.historico_medico = self.historico_medico or HistoricoMedico()
        self.resetar()

        return paciente

    
    def atualizar(self, paciente: Paciente) -> Paciente:
        if self.nome:
            paciente.nome = self.nome
        if self._cpf:
            paciente.cpf = self._cpf
        if self._cartao_sus is not None:
            paciente.cartao_sus = self._cartao_sus
        if self._idade is not None:
            paciente.idade = self._idade
        if self._altura is not None:
            paciente.altura = self._altura
        if self._peso is not None:
            paciente.peso = self._peso
        if self._tipo_sanguineo is not None:
            paciente.tipo_sanguineo = self._tipo_sanguineo
        if self._genero is not None:
            paciente.genero = self._genero
        if self._tipo_plano is not None:
            paciente.tipo_plano = self._tipo_plano
        if self._tipo_convenio is not None:
            paciente.tipo_convenio = self._tipo_convenio
        if self._contato_emergencia is not None:
            paciente.contato_emergencia = self._contato_emergencia
        if self._telefone is not None:
            paciente.telefone = self._telefone
        if self.historico_medico is not None:
            paciente.historico_medico = self.historico_medico
        self.resetar()

        return paciente
    
class DiretorPaciente:
    def __init__(self, builder: PacienteBuilder):
        self.builder = builder

    def construir_paciente_simples(self, nome, cpf, cartao_sus):
        if not nome or nome.strip() == "":
            raise ValueError("Nome é obrigatório para cadastrar um paciente.")
        return self.builder.resetar().com_nome(nome).com_cpf(cpf or "").com_cartao_sus(cartao_sus or "").construir()
    # Aqui eu posso fazer o cadastro completo se eu quiser. Posso fazer personalizado também.
    def construir_paciente_completo(self, dados):
        if not dados.get('nome') or dados['nome'].strip() == "":
            raise ValueError("Nome é obrigatório para cadastrar um paciente.")
        
        builder = self.builder.resetar()
        builder.com_nome(dados['nome'])
        builder.com_cpf(dados['cpf'] or "")
        
        if dados.get('idade'):
            builder.com_idade(dados['idade'])
        
        if dados.get('altura'):
            builder.com_altura(dados['altura'])
        
        if dados.get('peso'):
            builder.com_peso(dados['peso'])

        if dados.get('cartao_sus'):
            builder.com_cartao_sus(dados['cartao_sus'])
                 
        if dados.get('tipo_sanguineo'):
            builder.com_tipo_sanguineo(dados['tipo_sanguineo'])
        
        if dados.get('genero'):
            builder.com_genero(dados['genero'])
        
        if dados.get('tipo_plano'):
            builder.com_tipo_plano(dados['tipo_plano'])
        
        if dados.get('tipo_convenio'):
            builder.com_tipo_convenio(dados['tipo_convenio'])
        
        if dados.get('telefone'):
            builder.com_telefone(dados['telefone'])
        
        if dados.get('contato_emergencia'):
            builder.com_contato_emergencia(dados['contato_emergencia'])
        
        if dados.get('historico_medico'):
            builder.com_historico_medico(dados['historico_medico'])
        
        return builder.construir()
