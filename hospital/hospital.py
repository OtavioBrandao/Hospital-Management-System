from entidades.paciente import Paciente
from entidades.estoque import Estoque
from entidades.administrativo import SetorAdministrativo
from entidades.emergencia import EmergenciaManager, FuncionarioObserver
from entidades.funcionario import Medico, Enfermeiro, Dentista, Psicologo, Nutricionista, Fisioterapeuta, GerenciadorFuncionariosSaude
from gerarPdf import gerar_relatorio_paciente, gerar_relatorio_equipe, gerar_relatorio_hospital
from entidades.faturamento import estrategia_para_faturar
from entidades.paciente import PacienteBuilder
from entidades.exceptions import *

funcionarios_manager = GerenciadorFuncionariosSaude()

# Implementação do padrão Singleton para a classe Hospital
class Hospital:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hospital, cls).__new__(cls)
        return cls._instance
        
    def __init__(self):
        if Hospital._initialized:
            return
        Hospital._initialized = True

        builder = PacienteBuilder()

        # Vitor Gabriel - Particular, perfil completo
        vitor = builder.resetar()\
            .com_nome("Vitor Gabriel")\
            .com_cpf("12345")\
            .com_cartao_sus("67890")\
            .com_idade(25)\
            .com_altura(175)\
            .com_peso(70)\
            .com_tipo_sanguineo("O+")\
            .com_genero("MASCULINO")\
            .com_tipo_plano("PARTICULAR")\
            .com_telefone("82999887766")\
            .construir()

        vitor.historico_medico.adicionar_alergia("Dipirona")
        vitor.historico_medico.adicionar_observacao("Paciente pratica atividades físicas regularmente")

        # Otávio - Convênio Unimed
        otavio = builder.resetar()\
            .com_nome("Otávio")\
            .com_cpf("54321")\
            .com_cartao_sus("09876")\
            .com_idade(32)\
            .com_altura(180)\
            .com_peso(85)\
            .com_tipo_sanguineo("A+")\
            .com_genero("MASCULINO")\
            .com_tipo_plano("CONVENIO")\
            .com_tipo_convenio("UNIMED")\
            .com_telefone("82988776655")\
            .construir()

        otavio.historico_medico.adicionar_doenca_cronica("Hipertensão")
        otavio.historico_medico.adicionar_medicamento("Losartana 50mg - 1cp/dia")

        # Kaique Silva - SUS
        kaique = builder.resetar()\
            .com_nome("Kaique Silva")\
            .com_cpf("11223")\
            .com_cartao_sus("44556")\
            .com_idade(19)\
            .com_altura(168)\
            .com_peso(65)\
            .com_tipo_sanguineo("B+")\
            .com_genero("MASCULINO")\
            .com_tipo_plano("SUS")\
            .com_telefone("82987654321")\
            .construir()

        # Ygor - Convênio Amil
        ygor = builder.resetar()\
            .com_nome("Ygor")\
            .com_cpf("33445")\
            .com_cartao_sus("66778")\
            .com_idade(28)\
            .com_altura(172)\
            .com_peso(78)\
            .com_tipo_sanguineo("AB+")\
            .com_genero("MASCULINO")\
            .com_tipo_plano("CONVENIO")\
            .com_tipo_convenio("AMIL")\
            .com_telefone("82986543210")\
            .construir()


        ygor.historico_medico.adicionar_cirurgia("Apendicectomia - 2018")

        # Marco Gomes - Convênio Bradesco
        marco = builder.resetar()\
            .com_nome("Marco Gomes")\
            .com_cpf("55667")\
            .com_cartao_sus("77889")\
            .com_idade(45)\
            .com_altura(178)\
            .com_peso(92)\
            .com_tipo_sanguineo("O-")\
            .com_genero("MASCULINO")\
            .com_tipo_plano("CONVENIO")\
            .com_tipo_convenio("BRADESCO")\
            .com_telefone("82985432109")\
            .construir()

        marco.historico_medico.adicionar_doenca_cronica("Diabetes tipo 2")
        marco.historico_medico.adicionar_medicamento("Metformina 850mg - 2cp/dia")
        marco.historico_medico.adicionar_alergia("Penicilina")

        self.pacientes = [vitor, otavio, kaique, ygor, marco]

        self.funcionarios = [
        Medico("Dr. House", "CRM-999", "dr.house@hospital.com", "5582999999999", "Diagnóstico"),
        Medico("Saulo de Tarso", "CRM-123", "saulo@hospital.com", "5582988888888", "Cardiologista"),
        Medico("Maria", "CRM-456", "maria@hospital.com", "5582977777777", "Ortopedista"),
        Medico("Joana D'Arc", "CRM-789", "joana@hospital.com", "5582966666666", "Pediatra"),
        Medico("Cláudio", "CRM-101", "claudio@hospital.com", "5582955555555", "Neurologista"),
        Medico("Augusto", "CRM-202", "augusto@hospital.com", "5582944444444", "Clínico Geral"),
        Medico("César", "CRM-303", "cesar@hospital.com", "5582933333333", "Dermatologista"),
        Medico("Caio Calheiros", "CRM-404", "caio@hospital.com", "5582922222222", "Oftalmologista"),
        
        Enfermeiro("Pedro", "COREN-101", "pedro@hospital.com", "5582911111111"),
        Enfermeiro("Josemir", "COREN-102", "josemir@hospital.com", "5582900000000"),
        Enfermeiro("Karina", "COREN-202", "karina@hospital.com", "5582899999999"),
        Enfermeiro("Ana", "COREN-456", "ana@hospital.com", "5582888888888"),
        Enfermeiro("Agostinho de Hipona", "COREN-789", "agostinho@hospital.com", "5582877777777"),
        
        Dentista("Aurora Vieira", "CRO-789", "aurora@hospital.com", "5582866666666"),
        Dentista("Beatriz Silva", "CRO-456", "beatriz@hospital.com", "5582855555555"),
        Dentista("Carlos Eduardo", "CRO-123", "carlos@hospital.com", "5582844444444"),
        Dentista("Daniela Costa", "CRO-321", "daniela@hospital.com", "5582833333333"),
        
        Psicologo("Madalena", "CRP-101", "madalena@hospital.com", "5582822222222"),
        Psicologo("Mariana", "CRP-202", "mariana@hospital.com", "5582811111111"),
        Psicologo("Marcos", "CRP-303", "marcos@hospital.com", "5582800000000"),
        Psicologo("Suzana", "CRP-404", "suzana@hospital.com", "5582799999999")
        ]
        self.leitos = []
        self.escalonamento = {
            "Saulo de Tarso": "Manhã",
            "Caio Calheiros": "Tarde",
            "Dr. House": "Noite",
            "Pedro": "Tarde",
            "Josemir": "Noite",
            "Karina": "Manhã",
            "Suzana": "Noite"
        }
        self.estoque = Estoque()
        self.administrativo = SetorAdministrativo()
        self.emergencias = EmergenciaManager()

        for nome, turno in self.escalonamento.items():
            funcionario = next((f for f in self.funcionarios if f.nome == nome), None)
            if funcionario:
                observer = FuncionarioObserver(funcionario, email=funcionario.email, whatsapp=funcionario.whatsapp)
                self.emergencias.adicionar_observer(observer, turno)
    
    def adicionar_paciente(self, paciente):
        """Adiciona um paciente após verificar duplicação"""
        duplicado, mensagem = self._verificar_paciente_duplicado(paciente.nome, paciente.cpf)
        if duplicado:
            raise ValueError(mensagem)
        
        self.pacientes.append(paciente)
        return paciente

    def adicionar_funcionario(self, tipo, nome, registro, especialidade=None, email=None, whatsapp=None):
        for funcionario in self.funcionarios:
            if funcionario.registro == registro:
                print("Já existe um funcionário com esse registro.")
                return
            
        if not tipo in funcionarios_manager.factories:
            print(f"Tipo de funcionário '{tipo}' inválido.")
            return

        try:
            funcionario = funcionarios_manager.criar_funcionario(tipo, nome, registro, especialidade, email, whatsapp)
            self.funcionarios.append(funcionario)
            # Automaticamente alocar o novo funcionário em um turno padrão
            self._alocar_turno_padrao(funcionario)
            print(f"{tipo.capitalize()} {nome} adicionado ao hospital e alocado em turno.")
        except ValueError as e:
            print(f"Erro ao adicionar funcionário: {e}")
    
    def _alocar_turno_padrao(self, funcionario):
        """Aloca automaticamente um novo funcionário em um turno padrão"""
        # Distribuição simples: conta quantos funcionários já estão em cada turno
        turnos = ["Manhã", "Tarde", "Noite"]
        contagem_turnos = {turno: 0 for turno in turnos}
        
        for nome, turno in self.escalonamento.items():
            if turno in contagem_turnos:
                contagem_turnos[turno] += 1
        
        # Escolhe o turno com menos funcionários
        turno_escolhido = min(contagem_turnos, key=contagem_turnos.get)
        self.escalonar_funcionario(funcionario.nome, turno_escolhido)
        
        # Adiciona o observer para emergências
        from entidades.emergencia import FuncionarioObserver
        observer = FuncionarioObserver(funcionario, email=funcionario.email, whatsapp=funcionario.whatsapp)
        self.emergencias.adicionar_observer(observer, turno_escolhido)

    def remover_funcionario(self, nome, registro=None):
        for f in self.funcionarios:
            if f.nome.lower() == nome.lower() and (registro is None or f.registro == registro):
                self.funcionarios.remove(f)
                print(f"Funcionário {nome} removido.")
                return
        print("Funcionário não encontrado.")
    
    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return 

        print("\n--- Lista de Funcionários ---")
        for i, funcionario in enumerate(self.funcionarios, 1):
            nome = funcionario.nome
            registro = funcionario.registro if funcionario.registro else "Não informado"
            especialidade = getattr(funcionario, 'especialidade', 'N/A')
            print(f"{i}: Nome: {nome}, Registro: {registro}, Especialidade: {especialidade}")
    
    def mostrar_notificacoes_emergencia(self):
        if not self.emergencias.log:
            print("Nenhuma notificação de emergência.")
            return
        for log in self.emergencias.log:
            print(f"🕒 {log[0]} - {log[1].nome} recebeu a notificação: {log[2]}")

    def encontrar_paciente(self, nome):
        for p in self.pacientes:
            if p.nome.lower() == nome.lower():
                return p
        raise PacienteNaoEncontradoException(nome)

    def _verificar_paciente_duplicado(self, nome, cpf, id_temp=None):
        """Verifica se já existe um paciente com o mesmo CPF ou ID temporário"""
        for p in self.pacientes:
            # Verifica duplicação por CPF (se ambos tiverem CPF)
            if cpf and p.cpf and not p.cpf.startswith('TMP') and not cpf.startswith('TMP'):
                if p.cpf == cpf:
                    return True, f"Já existe um paciente cadastrado com o CPF {cpf}"
            
            # Verifica duplicação por ID temporário
            if cpf and cpf.startswith('TMP') and p.cpf == cpf:
                return True, f"Já existe um paciente com o ID temporário {cpf}"
                
        return False, ""
    
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
        try:
            paciente = self.encontrar_paciente(nome)
            print(f"\n--- Detalhes do Paciente: {paciente.nome} ---")
            
            # Dados básicos
            print(f"CPF: {paciente.cpf if paciente.cpf else 'Não informado'}")
            print(f"Cartão SUS: {paciente.cartao_sus if paciente.cartao_sus else 'Não informado'}")
            
            print(f"Idade: {paciente.idade if paciente.idade else 'Não informado'}")
            print(f"Altura: {paciente.altura}cm" if paciente.altura else "Altura: Não informado")
            print(f"Peso: {paciente.peso}kg" if paciente.peso else "Peso: Não informado")
            
            # IMC calculado automaticamente
            if paciente.imc:
                print(f"IMC: {paciente.imc:.2f}")
            else:
                print("IMC: Não calculável")
            
            # Enums
            print(f"Tipo Sanguíneo: {paciente.tipo_sanguineo.value if paciente.tipo_sanguineo else 'Não informado'}")
            print(f"Gênero: {paciente.genero.value if paciente.genero else 'Não informado'}")
            print(f"Tipo de Plano: {paciente.tipo_plano.value if paciente.tipo_plano else 'Não informado'}")
            print(f"Convênio: {paciente.tipo_convenio.value if paciente.tipo_convenio else 'Não informado'}")
            
            # Contato
            print(f"Telefone: {paciente.telefone if paciente.telefone else 'Não informado'}")
            print(f"Contato de Emergência: {paciente.contato_emergencia if paciente.contato_emergencia else 'Não informado'}")
            
            # Histórico médico
            print(f"\n--- Histórico Médico ---")
            if paciente.historico_medico:
                resumo = paciente.historico_medico.resumo()
                print(resumo if resumo != "Nenhum histórico registrado" else "Nenhum histórico registrado.")
            else:
                print("Nenhum histórico registrado.")
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
        except PacienteNaoEncontradoException as e:
            print(e)


    '''Nesta função é onde implementamos o polimorfismo:
        - Cada profissional da saúde tem o seu "jeito" de atender o paciente
        - Então usamos o polimorfismo para que o profissional desejado atenda o paciente
    '''
    #Contem polimorfismo
    # Adicionar aqui a possibilidade de cancelar consulta e remarcar consulta
    def agendar_consulta(self, nome_paciente, dia, tipo_profissional, nome_profissional=None):
        try:
            paciente = self.encontrar_paciente(nome_paciente)
            if not paciente:
                print("Paciente não encontrado.")
                return

            profissional_encontrado = None
        
            if nome_profissional:
                for funcionario in self.funcionarios:
                    if (funcionario.nome.lower() == nome_profissional.lower() and 
                        funcionario.__class__.__name__.lower() == tipo_profissional.lower()):
                        profissional_encontrado = funcionario
                        break
            else:
                # Caso contrário, pegar o primeiro profissional do tipo solicitado
                for funcionario in self.funcionarios:
                    if funcionario.__class__.__name__.lower() == tipo_profissional.lower():
                        profissional_encontrado = funcionario
                        break

            if profissional_encontrado:
                paciente.agendar_consulta(dia, profissional_encontrado.nome)
                print(f"Consulta agendada para {paciente.nome} com {tipo_profissional} {profissional_encontrado.nome} no dia {dia}.")
                profissional_encontrado.atenderPaciente(paciente)
            else:
                if nome_profissional:
                    print(f"Profissional '{nome_profissional}' do tipo '{tipo_profissional}' não encontrado.")
                else:
                    print(f"Não foi encontrado um profissional do tipo '{tipo_profissional}' disponível.")
        except PacienteNaoEncontradoException as e:
            print(e)
    
    def remarcar_consulta(self, nome_paciente, indice_consulta, novo_dia):
        try:
            paciente = self.encontrar_paciente(nome_paciente)
            try:
                consulta = list(paciente.consultas[indice_consulta])
                consulta[0] = novo_dia
                paciente.consultas[indice_consulta] = tuple(consulta)
                print(f"Consulta remarcada para o dia {novo_dia}.")
            except IndexError:
                print("Índice de consulta inválido.")
        except PacienteNaoEncontradoException as e:
            print(e)
   
    def cancelar_consulta(self, nome_paciente, indice_consulta):
        try:
            paciente = self.encontrar_paciente(nome_paciente)
            try:
                consulta = paciente.consultas.pop(indice_consulta)
                print(f"Consulta removida: {consulta[0]} com {consulta[1]}.")
            except IndexError:
                print("Índice de consulta inválido.")
        except PacienteNaoEncontradoException as e:
            print(e)

    def registrar_prontuario(self, nome, profissional, descricao):
        try:
            paciente = self.encontrar_paciente(nome)
            paciente.adicionar_prontuario(profissional, descricao)
            print("Prontuário registrado.")
        except PacienteNaoEncontradoException as e:
            print(e)

    def registrar_receita(self, nome, profissional, medicamento, descricao, dosagem):
        try:
            paciente = self.encontrar_paciente(nome)
            paciente.adicionar_receita(profissional, medicamento, descricao, dosagem)
        except PacienteNaoEncontradoException as e:
            print(e)

    def listar_receitas(self, nome):
        try:
            paciente = self.encontrar_paciente(nome)
            if paciente:
                if paciente.receitas:
                    print(f"\n--- Receitas de {paciente.nome} ---")
                for i, receita in enumerate(paciente.receitas, 1):
                    print(f"{i}: {receita}")
            else:
                print(f"\n--- Receitas de {paciente.nome} ---")
                print("Nenhuma receita registrada.")
        except PacienteNaoEncontradoException as e:
            print(e)

    def faturar_paciente(self, nome):
        try:
            paciente = self.encontrar_paciente(nome)
        except PacienteNaoEncontradoException as e:
            print(e)
            return

        estrategia = estrategia_para_faturar(paciente) # Objeto de acordo com a estratégia 
        valor = estrategia.calcular_faturamento(paciente)

        print(f"\nFatura de {paciente.nome}")
        print(f"Tipo de Plano: {paciente.tipo_plano}")
        if paciente.tipo_convenio:
            print(f"Convênio: {paciente.tipo_convenio}")
        print(f"Consultas: {len(paciente.consultas)}")
        print(f"Exames: {len(paciente.exames)}")
        print(f"TOTAL: R$ {valor:.2f}")


    #Contem polimorfismo
    def solicitar_exame(self, nomePaciente, nomeProfissional, nomeExame):
        try:
            paciente = self.encontrar_paciente(nomePaciente)
        except PacienteNaoEncontradoException as e:
            print(e)
            return

        profissional = None
        for funcionario in self.funcionarios: #Procuramos o profissional
            if funcionario.nome.lower() == nomeProfissional.lower():
                profissional = funcionario
                break
        # Colocar Try e Except aqui tbm
        if not profissional:
            print(f"Profissional {nomeProfissional} não encontrado.")
            return

        # Polimorfismo: O hospital não sabe os detalhes, apenas
        # manda o objeto profissional requisitar o exame.
        profissional.requisitarExame(paciente, nomeExame, True)
    
    def solicitar_pacote_exames(self, nome_paciente, nome_profissional, codigo_pacote):
        from entidades.exame import PACOTES_EXAMES

        try:
            paciente = self.encontrar_paciente(nome_paciente)
        except PacienteNaoEncontradoException as e:
            print(e)
            return
        
        profissional = next((f for f in self.funcionarios if f.nome.lower() == nome_profissional.lower()), None)
        if not profissional:
            print("Profissional não encontrado.")
            return
        
        pacote = PACOTES_EXAMES.get(codigo_pacote)
        if not pacote:
            print("Pacote não encontrado.")
            return
        
        print(f"\n📋 Pacote: {pacote.nome}")
        print(f"📝 Descrição: {pacote.descricao}")
        print(f"💰 Valor total: R$ {pacote.obter_custo():.2f}")
        print(f"📝 Exames inclusos: {', '.join(pacote.listar_exames())}")
        
        confirma = input("\nConfirmar solicitação? (s/n): ")
        if confirma.lower() == 's':
            pacote.executar(profissional, paciente)
            print("✅ Pacote solicitado com sucesso!")
            
    # Adicionar opção de ver leitos alocados e situação do hospital
    def alocar_leito(self, nome):
        try:
            paciente = self.encontrar_paciente(nome)
        except PacienteNaoEncontradoException as e:
            print(e)
            return

        leito = f"Leito-{len(self.leitos)+1}"
        self.leitos.append((leito, paciente.nome))
        print(f"{paciente.nome} alocado no {leito}.")

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
        try:
            paciente = self.encontrar_paciente(nome_paciente)
        except PacienteNaoEncontradoException as e:
            print(e)
            return
        gerar_relatorio_paciente(paciente)

    def gerar_pdf_equipe(self):
        gerar_relatorio_equipe(self.funcionarios)
    
    def gerar_pdf_hospital(self):
        gerar_relatorio_hospital(self)