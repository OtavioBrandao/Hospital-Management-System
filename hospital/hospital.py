from entidades.paciente import Paciente
from entidades.estoque import Estoque
from entidades.administrativo import SetorAdministrativo
from entidades.emergencia import EmergenciaManager
from entidades.funcionario import Medico, Enfermeiro, Dentista, Psicologo
from gerarPdf import gerar_relatorio_paciente, gerar_relatorio_equipe, gerar_relatorio_hospital

PRECO = 10.5 #Valor estipulado de maneira avulsa
class Hospital:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hospital, cls).__new__(cls)
        return cls._instance
        
    def __init__(self):
        self.pacientes = [
            Paciente("Vitor Gabriel", "12345", "67890"),
            Paciente("Otávio", "54321", "09876")
            ] #Pacientes pre-estabelecidos
        
        self.funcionarios = [
            Medico("Saulo de Tarso", "CRM-123", "Cardiologista"),
            Enfermeiro("Agostinho de Hipona", "COREN-456"),
            Dentista("Aurora Vieira", "CRO-789"),
            Psicologo("Madalena", "CRP-101")
        ] #Funcionarios pre-estabelecidos
        self.leitos = []
        self.escalonamento = {}
        self.estoque = Estoque()
        self.administrativo = SetorAdministrativo()
        self.emergencias = EmergenciaManager()

    def cadastrar_paciente(self, nome, cpf=None, cartao_sus=None):
        paciente = Paciente(nome, cpf, cartao_sus)
        self.pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado.")

    def encontrar_paciente(self, nome):
        for p in self.pacientes:
            if p.nome.lower() == nome.lower():
                return p
        return None
    
    def listarPacientes(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
            return  # Retorna para sair da função se não houver pacientes

        print("\n--- Lista de Pacientes ---")
        for i, paciente in enumerate(self.pacientes, 1):
            nome = paciente.nome
            cpf = paciente.cpf if paciente.cpf else "Não informado"
            cartao_sus = paciente.cartao_sus if paciente.cartao_sus else "Não informado"
            print(f"{i}: Nome: {nome}, CPF: {cpf}, Cartão SUS: {cartao_sus}")

    def mostrarPaciente(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            print(f"\n--- Detalhes do Paciente: {paciente.nome} ---")
            print(f"CPF: {paciente.cpf if paciente.cpf else 'Não informado'}")
            print(f"Cartão SUS: {paciente.cartao_sus if paciente.cartao_sus else 'Não informado'}")
            
            print("\n--- Prontuários ---")
            if paciente.prontuarios:
                for prontuario in paciente.prontuarios:
                    print(prontuario)
            else:
                print("Nenhum prontuário registrado.")

            self.listar_receitas(nome)

            print("\n--- Exames Solicitados ---")
            if paciente.exames:
                for i, exame in enumerate(paciente.exames, 1):
                    print(f"{i}: {exame}")
            else:
                print("Nenhum exame solicitado.")

            print("\n--- Consultas Agendadas ---")
            if paciente.consultas:
                for i, (dia, medico) in enumerate(paciente.consultas, 1):
                    print(f"{i}: Dia {dia} com Dr(a). {medico}")
            else:
                print("Nenhuma consulta agendada.")
        else:
            print("Paciente não encontrado.")

    '''Nesta função é onde implementamos o polimorfismo:
        - Cada profissional da saúde tem o seu "jeito" de atender o paciente
        - Então usamos o polimorfismo para que o profissional desejado atenda o paciente
    '''
    #Contem polimorfismo
    # Adicionar aqui a possibilidade de cancelar consulta e remarcar consulta
    def agendar_consulta(self, nome_paciente, dia, tipo_profissional):
        paciente = self.encontrar_paciente(nome_paciente)
        if not paciente:
            print("Paciente não encontrado.")
            return

        profissional_encontrado = None #Inicialmente nenhum profissional é encontrado
        # Polimorfismo em ação: procuramos por um objeto que seja da classe desejada
        # (ex: Medico, Dentista)

        for funcionario in self.funcionarios:
            #Aqui não precisamos saber exatamente o tipo de profissional buscado, 
            # apenas comparamos o nome da classe com o tipo de profissional solicitado

            if funcionario.__class__.__name__.lower() == tipo_profissional.lower():
                profissional_encontrado = funcionario
                break # Encontramos o profissional, podemos parar o loop

        if profissional_encontrado: #Encontramos o profissional que queremos
            # Usamos o nome do objeto encontrado para agendar
            paciente.agendar_consulta(dia, profissional_encontrado.nome)
            print(f"Consulta agendada para {paciente.nome} com {tipo_profissional} {profissional_encontrado.nome} no dia {dia}.")
            # Exemplo de polimorfismo: chamar o método do profissional encontrado
            profissional_encontrado.atenderPaciente(paciente)
        else:
            print(f"Não foi encontrado um profissional do tipo '{tipo_profissional}' disponível.")
    
    def remarcar_consulta(self, nome_paciente, indice_consulta, novo_dia):
        paciente = self.encontrar_paciente(nome_paciente)
        if not paciente:
            print("Paciente não encontrado.")
            return
        if 0 <= indice_consulta < len(paciente.consultas):
            consulta = list(paciente.consultas[indice_consulta])
            consulta[0] = novo_dia
            paciente.consultas[indice_consulta] = tuple(consulta)
            print(f"Consulta remarcada para o dia {novo_dia}.")
        else:
            print("Índice de consulta inválido.")
   
    def cancelar_consulta(self, nome_paciente, indice_consulta):
        paciente = self.encontrar_paciente(nome_paciente)
        if not paciente:
            print("Paciente não encontrado.")
            return
        if 0 <= indice_consulta < len(paciente.consultas):
            consulta = paciente.consultas.pop(indice_consulta)
            print(f"Consulta removida: {consulta[0]} com {consulta[1]}.")
        else:
            print("Índice de consulta inválido.")
  

    def registrar_prontuario(self, nome, profissional, descricao):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            paciente.adicionar_prontuario(profissional, descricao)
            print("Prontuário registrado.")
        else:
            print("Paciente não encontrado.")

    def registrar_receita(self, nome, profissional, medicamento, descricao, dosagem):
        paciente = self.encontrar_paciente(nome)
        
        if paciente:
            paciente.adicionar_receita(profissional, medicamento, descricao, dosagem)
        else:
            print("Paciente não encontrado.")
    
    def listar_receitas(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            if paciente.receitas:
                print(f"\n--- Receitas de {paciente.nome} ---")
                for i, receita in enumerate(paciente.receitas, 1):
                    print(f"{i}: {receita}")
            else:
                print(f"\n--- Receitas de {paciente.nome} ---")
                print("Nenhuma receita registrada.")
        else:
            print("Paciente não encontrado.")

    def faturar_paciente(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            total = len(paciente.consultas) * PRECO + len(paciente.exames) * PRECO
            print(f"Fatura para {paciente.nome}: R$ {total:.2f}")
        else:
            print("Paciente não encontrado.")

    #Contem polimorfismo
    def solicitar_exame(self, nomePaciente, nomeProfissional, nomeExame):
        paciente = self.encontrar_paciente(nomePaciente)
        if not paciente:
            print("Paciente não encontrado.")
            return

        profissional = None
        for funcionario in self.funcionarios: #Procuramos o profissional
            if funcionario.nome.lower() == nomeProfissional.lower():
                profissional = funcionario
                break
        
        if not profissional:
            print(f"Profissional {nomeProfissional} não encontrado.")
            return

        # Polimorfismo: O hospital não sabe os detalhes, apenas
        # manda o objeto profissional requisitar o exame.
        profissional.requisitarExame(paciente, nomeExame)
        
    # Adicionar opção de ver leitos alocados e situação do hospital
    def alocar_leito(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            leito = f"Leito-{len(self.leitos)+1}"
            self.leitos.append((leito, paciente.nome))
            print(f"{paciente.nome} alocado no {leito}.")
        else:
            print("Paciente não encontrado.")

    def escalonar_funcionario(self, nome, turno):
        self.escalonamento[nome ] = turno
        print(f"{nome} escalado para o turno {turno}.")

    def ver_escalonamento(self):
        if not self.escalonamento:
            print("Nenhum funcionário escalado.")
        else:
            for nome, turno in self.escalonamento.items():
                print(f"{nome}: {turno}")

    #PDF
    def gerar_pdf_paciente(self, nome_paciente):
        paciente = self.encontrar_paciente(nome_paciente)
        if paciente:
            gerar_relatorio_paciente(paciente)
        else:
            print("Paciente não encontrado.")

    def gerar_pdf_equipe(self):
        gerar_relatorio_equipe(self.funcionarios)
    
    def gerar_pdf_hospital(self):
        gerar_relatorio_hospital(self)