from datetime import datetime

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
