'''class Paciente:
    def __init__(self, nome): #construtor
        self.nome = nome
        self.prontuario = []
        self.receitas = []
        self.exames = []
        self.consultas = []

    def registrar_prontuario(self, info):
        self.prontuario.append(info)

    def adicionar_receita(self, receita):
        self.receitas.append(receita)

    def solicitar_exame(self, exame):
        self.exames.append(exame)

    def agendar_consulta(self, dia, medico):
        self.consultas.append((dia, medico))

    def __str__(self):
        return f"Paciente: {self.nome}"

'''
class funcionarioSaude:
    def __init__(self,nome,profissao, registroProfissional):
        self.nome = nome
        self.funcionario = []
        self.profissao = profissao
        self.registroProfissional = registroProfissional
    
    def addFuncionario(self,nome):
        self.funcionario.append(nome)

    def removerFuncionario(self):
        self.funcionario.pop()
    
    def atualizarFuncionario(self):
        #irei implementar, pois estou em duvida se faço funcionario ser uma lista ou um dicionari


'''
        
class Hospital:
    def __init__(self):
        self.pacientes = []
        self.leitos = []
        self.estoque = {}  # nome_item: quantidade
        self.funcionarios = {}  # nome: turno
        self.emergencias = []  # (nome_paciente, grau_prioridade)

    def cadastrar_paciente(self, nome):
        paciente = Paciente(nome)
        self.pacientes.append(paciente)
        print(f" Paciente {nome} cadastrado.")

    def encontrar_paciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome.lower() == nome.lower():
                return paciente
        return None

    def agendar_consulta(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            dia = input("Dia da consulta: ")
            medico = input("Especialidade do médico: ")
            paciente.consultas.append((dia, medico))
            print(f" Consulta marcada: {dia} com {medico}")
        else:
            print(" Paciente não encontrado.")

    def registrar_prontuario(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            info = input("Informe dados para o prontuário: ")
            paciente.prontuario.append(info)
            print(" Informação registrada.")
        else:
            print(" Paciente não encontrado.")

    def gerar_receita(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            receita = input("Digite a receita: ")
            paciente.receitas.append(receita)
            print("Receita gerada.")
        else:
            print(" Paciente não encontrado.")

    def solicitar_exame(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            exame = input("Exame solicitado: ")
            paciente.exames.append(exame)
            print(" Exame registrado.")
        else:
            print(" Paciente não encontrado.")

    def alocar_leito(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            leito = f"Leito-{len(self.leitos) + 1}"
            self.leitos.append((leito, paciente.nome))
            print(f" {paciente.nome} alocado no {leito}")
        else:
            print(" Paciente não encontrado.")

    def faturar(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            total = len(paciente.consultas) * 100 + len(paciente.exames) * 150
            print(f" Fatura para {paciente.nome}: R$ {total:.2f}")
        else:
            print(" Paciente não encontrado.")

    def adicionar_estoque(self):
        item = input("Item a adicionar ao estoque: ")
        qtd = int(input("Quantidade: "))
        self.estoque[item] = self.estoque.get(item, 0) + qtd
        print(f" {qtd} unidades de {item} adicionadas.")

    def mostrar_estoque(self):
        if not self.estoque:
            print(" Estoque vazio.")
            return
        print(" Estoque atual:")
        for item, qtd in self.estoque.items():
            print(f"   - {item}: {qtd} unidades")

    def escalar_funcionario(self):
        nome = input("Nome do funcionário: ")
        turno = input("Turno (manhã/tarde/noite): ")
        self.funcionarios[nome] = turno
        print(f" Funcionário {nome} escalado para o turno {turno}.")

    def ver_escalonamento(self):
        if not self.funcionarios:
            print(" Nenhum funcionário escalado.")
            return
        print("Escalonamento:")
        for nome, turno in self.funcionarios.items():
            print(f"   - {nome}: {turno}")

    def registrar_emergencia(self):
        nome = input("Nome do paciente em emergência: ")
        prioridade = input("Prioridade (alta/média/baixa): ").lower()
        self.emergencias.append((nome, prioridade))
        print("Emergência registrada.")

    def ver_emergencias(self):
        if not self.emergencias:
            print(" Nenhuma emergência no momento.")
            return
        print(" Emergências:")
        prioridades = {"alta": 1, "média": 2, "baixa": 3}
        ordenadas = sorted(self.emergencias, key=lambda x: prioridades.get(x[1], 4))
        for nome, prioridade in ordenadas:
            print(f"   - {nome}: prioridade {prioridade}")

    def menu(self):
        print("\n--- SISTEMA DE GESTÃO HOSPITALAR ---")
        print("1  - Cadastrar paciente")
        print("2  - Agendar consulta")
        print("3  - Registro médico")
        print("4  - Faturamento")
        print("5  - Gerar receita")
        print("6  - Solicitar exame")
        print("7  - Alocar leito")
        print("8  - Gerenciar estoque")
        print("9  - Escalonamento de pessoal")
        print("10 - Gerenciar emergência")
        print("0  - Sair")


# Execução
hospital = Hospital()

while True:
    hospital.menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print(" Sistema encerrado.")
        break
    elif opcao == '1':
        nome = input("Nome do paciente: ")
        hospital.cadastrar_paciente(nome)
    elif opcao == '2':
        nome = input("Nome do paciente: ")
        hospital.agendar_consulta(nome)
    elif opcao == '3':
        nome = input("Nome do paciente: ")
        hospital.registrar_prontuario(nome)
    elif opcao == '4':
        nome = input("Nome do paciente: ")
        hospital.faturar(nome)
    elif opcao == '5':
        nome = input("Nome do paciente: ")
        hospital.gerar_receita(nome)
    elif opcao == '6':
        nome = input("Nome do paciente: ")
        hospital.solicitar_exame(nome)
    elif opcao == '7':
        nome = input("Nome do paciente: ")
        hospital.alocar_leito(nome)
    elif opcao == '8':
        print("1 - Adicionar item ao estoque")
        print("2 - Ver estoque")
        print("3 - sair")
        est_opcao = input("Escolha: ")
        while est_opcao != '3':
            if est_opcao == '1':
                hospital.adicionar_estoque()
            elif est_opcao == '2':
                hospital.mostrar_estoque()
            est_opcao = input("Escolha: ")
    elif opcao == '9':
        print("1 - Escalar funcionário")
        print("2 - Ver escalonamento")
        print("3 - sair")
        esc_opcao = input("Escolha: ")
        while esc_opcao != '3':
            if esc_opcao == '1':
                hospital.escalar_funcionario()
            elif esc_opcao == '2':
                hospital.ver_escalonamento()
            esc_opcao = input("Escolha: ")
    elif opcao == '10':
        print("1 - Registrar emergência")
        print("2 - Ver emergências")
        print("3 - sair")
        em_opcao = input("Escolha: ")
        while em_opcao != '3':
            if em_opcao == '1':
                hospital.registrar_emergencia()
            elif em_opcao == '2':
                hospital.ver_emergencias()
            em_opcao = input("Escolha: ")
    else:
        print(" Opção inválida.")'''