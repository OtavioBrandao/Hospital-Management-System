from entidades.exame import EXAMES_DISPONIVEIS
from entidades.paciente import PacienteBuilder, DiretorPaciente, HistoricoMedico
import os
import random


hospital = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\n--- SISTEMA DE GESTÃO HOSPITALAR ---")
    print("1  - Central de Pacientes")
    print("2  - Agendar consulta")
    print("3  - Registrar prontuário")
    print("4  - Gerar fatura")
    print("5  - Gerenciar estoque")
    print("6  - Emergências")
    print("7  - Solicitar exame")
    print("8  - Alocar leito")
    print("9  - Funcionários")
    print("10 - Receituário")
    print("11 - Relatórios")
    print("0  - Sair")
    print("-----------------------------------")

''' --- Funções para facilitar na main --- '''

def estoque_menu(hospital):
    print("\n--- ESTOQUE ---")
    print("1 - Adicionar item")
    print("2 - Ver estoque")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            item = input("Item: ")
            qtd = int(input("Quantidade: "))
            hospital.estoque.adicionar_item(item, qtd)
        elif op == '2':
            hospital.estoque.mostrar_estoque()
        else:
            print("Opção inválida.")
        print()
        op = input("Escolha: ")
    clear_screen()

def funcionarios(hospital):
    print("Deseja realizar uma queixa ou escalonar um funcionário?")
    print("1 - Queixa")
    print("2 - Escalonar funcionário")
    print("3 - Gerenciamento de funcionários")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            queixa()
            break
        elif op == '2':
            escalonamento_menu(hospital)
            break
        elif op == '3':
            funcionario_manager(hospital)
            break
    clear_screen()

def receituario_menu(hospital):
    print("\n--- RECEITUÁRIO ---")
    print("1 - Gerar receita")
    print("2 - Ver receitas")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        clear_screen()
        if op == '1':
            nome = input("Nome do paciente: ")
            medicamento = input("Medicamento: ")
            descricao = input("Descrição: ")
            profissional = input("Profissional: ") # Depois pegar o nome do profissional logado futuramente
            dosagem = input("Dosagem: ")
            hospital.registrar_receita(nome, profissional, medicamento, descricao, dosagem)
        elif op == '2':
            nome = input("Nome do paciente: ") # Depois pegar os dados do paciente logado já
            hospital.listar_receitas(nome)
        else:
            print("Opção inválida.")
        print()
        op = input("Escolha: ")

    clear_screen()

def emergencias_menu(hospital):
    print("\n--- EMERGÊNCIAS ---")
    print("1 - Registrar emergência")
    print("2 - Ver emergências")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do paciente: ")
            prioridade = input("Prioridade (alta/media/baixa): ").lower()
            hospital.emergencias.registrar_emergencia(nome, prioridade)
        elif op == '2':
            hospital.emergencias.ver_emergencias()
        else:
            print("Opção inválida.")
        op = input("Escolha: ")
    clear_screen()

        
def escalonamento_menu(hospital):
    print("\n--- ESCALONAMENTO ---")
    print("1 - Escalar funcionário")
    print("2 - Ver escalonamento")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do funcionário: ")
            turno = input("Turno (manhã/tarde/noite): ")
            hospital.escalonar_funcionario(nome, turno)
        elif op == '2':
            hospital.ver_escalonamento()
        else:
            print("Opção inválida.")
        op = input("Escolha: ")
    clear_screen()

paciente_builder = PacienteBuilder()
diretor_paciente = DiretorPaciente(paciente_builder)

def cadastro_simples():
    input_nome = input("Nome do paciente: ")
    input_cpf = input("CPF: ")
    input_cartao_sus = input("Cartão SUS(Se houver): ")

    try:
        paciente = diretor_paciente.construir_paciente_simples(input_nome, input_cpf, input_cartao_sus)
        hospital.pacientes.append(paciente)
        print(f"Paciente {input_nome} cadastrado com sucesso!")
        input("Pressione Enter para continuar...")
        return paciente
    except ValueError as ve:
        print(f"Erro no cadastro: {ve}")
        return None
    
def cadastro_completo():
    dados = {}

    dados['nome'] = input("Nome do paciente: ") 
    dados['cpf'] = input("CPF: ") or None
    dados['cartao_sus'] = input("Cartão SUS(Se houver): ") or None
    
    idade_input = input("Idade: ").strip()
    if idade_input:
        try:
            dados['idade'] = int(idade_input)
        except ValueError:
            print("Idade inválida, será definida como None")
            dados['idade'] = None
    else:
        dados['idade'] = None
    

    altura_input = input("Altura (em cm): ").strip()
    if altura_input:
        try:
            dados['altura'] = float(altura_input)
        except ValueError:
            print("Altura inválida, será definida como None")
            dados['altura'] = None
    else:
        dados['altura'] = None
    
    peso_input = input("Peso (em kg): ").strip()
    if peso_input:
        try:
            dados['peso'] = float(peso_input)
        except ValueError:
            print("Peso inválido, será definido como None")
            dados['peso'] = None
    else:
        dados['peso'] = None
    
    dados['tipo_sanguineo'] = input("Tipo Sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip() or None
    dados['genero'] = input("Gênero (Masculino, Feminino, Outro): ").strip() or None
    dados['tipo_plano'] = input("Tipo de Plano (Particular, SUS, Convênio): ").strip() or None
    dados['telefone'] = input("Telefone (apenas números): ").strip() or None
    

    nome_emergencia = input("Nome do contato de emergência: ").strip()
    tel_emergencia = input("Telefone do contato de emergência (apenas números): ").strip()
    
    if nome_emergencia and tel_emergencia:
        dados['contato_emergencia'] = (nome_emergencia, tel_emergencia)
    else:
        dados['contato_emergencia'] = None

    dados['historico_medico'] = coletar_historico_medico()

    try:
        paciente = diretor_paciente.construir_paciente_completo(dados)
        hospital.pacientes.append(paciente)
        print(f"Paciente {dados['nome']} cadastrado com sucesso!")
        input("Pressione Enter para continuar...")
        return paciente
    except ValueError as ve:
        print(f"Erro no cadastro: {ve}")
        return None
    except Exception as e:
        print(f"Erro inesperado no cadastro: {e}")
        return None
    
def coletar_historico_medico():
    h = HistoricoMedico()
    while True:
        print("\n--- HISTÓRICO MÉDICO ---")
        print("1 - Adicionar alergia")
        print("2 - Adicionar doença crônica")
        print("3 - Adicionar cirurgia")
        print("4 - Adicionar medicação de uso")
        print("5 - Adicionar observação")
        print("6 - Ver resumo atual")
        print("0 - Finalizar histórico")
        op = input("Escolha: ").strip()

        if op == '1':
            txt = input("Alergia (ex: Dipirona): ").strip()
            if txt: h.adicionar_alergia(txt)
        elif op == '2':
            txt = input("Doença crônica (ex: Hipertensão): ").strip()
            if txt: h.adicionar_doenca_cronica(txt)
        elif op == '3':
            txt = input("Cirurgia (ex: Apendicectomia - 2019): ").strip()
            if txt: h.adicionar_cirurgia(txt)
        elif op == '4':
            txt = input("Medicação (ex: Losartana 50mg 1cp/dia): ").strip()
            if txt: h.adicionar_medicamento(txt)
        elif op == '5':
            txt = input("Observação livre: ").strip()
            if txt: h.adicionar_observacao(txt)
        elif op == '6':
            print("\n>>> Resumo parcial:")
            print(h.resumo() or "Nenhum histórico registrado.")
        elif op == '0':
            clear_screen()
            return h
        else:
            print("Opção inválida.")     
    
   

def editar_historico_medico(paciente):
    print("\n--- EDITAR HISTÓRICO MÉDICO ---")
    print("Histórico atual:")
    print(paciente.historico_medico.resumo() or "Nenhum histórico registrado.")
    resp = input("Deseja alterar/adicionar informações? (s/n): ").strip().lower()
    if resp != 's':
        return

    h = paciente.historico_medico  
    while True:
        print("\n1-Alergia  2-Doença crônica  3-Cirurgia  4-Medicação  5-Observação  6-Ver resumo  0-Finalizar")
        op = input("Escolha: ").strip()
        if op == '1':
            t = input("Alergia: ").strip()
            if t: h.adicionar_alergia(t)
        elif op == '2':
            t = input("Doença crônica: ").strip()
            if t: h.adicionar_doenca_cronica(t)
        elif op == '3':
            t = input("Cirurgia: ").strip()
            if t: h.adicionar_cirurgia(t)
        elif op == '4':
            t = input("Medicação: ").strip()
            if t: h.adicionar_medicamento(t)
        elif op == '5':
            t = input("Observação: ").strip()
            if t: h.adicionar_observacao(t)
        elif op == '6':
            print("\n>>> Resumo parcial:")
            print(h.resumo() or "Nenhum histórico registrado.")
        elif op == '0':
            input("Histórico atualizado. Pressione Enter para continuar...")
            clear_screen()
            return
        else:
            print("Opção inválida.")


def atualizar_dados_paciente():
    nome = input("Nome do paciente a atualizar: ").strip()
    paciente = hospital.encontrar_paciente(nome)
    if not paciente:
        print("Paciente não encontrado.")
        return None

    print(f"Atualizando dados de: {paciente.nome}")
    print("Deixe em branco os campos que não deseja alterar.")

    try:
        b = paciente_builder.resetar()
        novo_nome = input(f"Nome atual: {paciente.nome} | Novo nome: ").strip()
        if novo_nome:
            b.com_nome(novo_nome)
        novo_cpf = input(f"CPF atual: {paciente.cpf} | Novo CPF: ").strip()
        if novo_cpf:
            b.com_cpf(novo_cpf)
        novo_cartao_sus = input(f"Cartão SUS atual: {paciente.cartao_sus} | Novo Cartão SUS: ").strip()
        if novo_cartao_sus:
            b.com_cartao_sus(novo_cartao_sus)
        nova_idade = input(f"Idade atual: {paciente.idade} | Nova idade: ").strip()
        if nova_idade:
            try:
                b.com_idade(int(nova_idade))
            except ValueError:
                print("Idade inválida, mantendo valor atual")
        nova_altura = input(f"Altura atual: {paciente.altura} | Nova altura (em cm): ").strip()
        if nova_altura:
            try:
                b.com_altura(float(nova_altura))
            except ValueError:
                print("Altura inválida, mantendo valor atual")
        novo_peso = input(f"Peso atual: {paciente.peso} | Novo peso (em kg): ").strip()
        if novo_peso:
            try:
                b.com_peso(float(novo_peso))
            except ValueError:
                print("Peso inválido, mantendo valor atual")
        novo_ts = input(
            f"Tipo Sanguíneo atual: {paciente.tipo_sanguineo} | Novo (A+, A-, B+, B-, AB+, AB-, O+, O-): "
        ).strip()
        if novo_ts:
            b.com_tipo_sanguineo(novo_ts)
        novo_genero = input(
            f"Gênero atual: {paciente.genero} | Novo Gênero (Masculino, Feminino, Outro): "
        ).strip()
        if novo_genero:
            b.com_genero(novo_genero)
        novo_plano = input(
            f"Tipo de Plano atual: {paciente.tipo_plano} | Novo Tipo de Plano (Particular, SUS, Convênio): "
        ).strip()
        if novo_plano:
            b.com_tipo_plano(novo_plano)
        novo_tel = input(
            f"Telefone atual: {paciente.telefone} | Novo Telefone (apenas números): "
        ).strip()
        if novo_tel:
            b.com_telefone(novo_tel)
        print(f"Contato de Emergência atual: {paciente.contato_emergencia}")
        novo_nome_emerg = input("Novo nome do contato de emergência: ").strip()
        novo_tel_emerg = input("Novo telefone do contato de emergência (apenas números): ").strip()
        if novo_nome_emerg and novo_tel_emerg:
            b.com_contato_emergencia((novo_nome_emerg, novo_tel_emerg))
        elif novo_nome_emerg or novo_tel_emerg:
            print("Para atualizar o contato de emergência, forneça nome e telefone juntos.")


        editar = input("Deseja editar o histórico médico? (s/n): ").strip().lower()
        if editar == 's':
            editar_historico_medico(paciente)  
            b.com_historico_medico(paciente.historico_medico)

        paciente_atualizado = b.atualizar(paciente)
        print(f"Paciente {paciente_atualizado.nome} atualizado com sucesso!")
        input("Pressione Enter para continuar...")
        clear_screen()
        return paciente_atualizado

    except Exception as e:
        print(f"Erro ao atualizar paciente: {e}")
        return None

    
# Função de cadastro modificada para funcionar com Builder
def cadastroPaciente():
    print("--- CADASTRO DE PACIENTE ---")
    print("1 - Cadastro simples")
    print("2 - Cadastro completo")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            cadastro_simples()
            break
        elif op == '2':
            cadastro_completo()
            break
        else:
            print("Opção inválida.")

#Função mais robusta para cadastrar e ver os pacientes
def cadastro():
    print("\n--- CENTRAL DE PACIENTES ---")
    print("1 - Cadastrar paciente")
    print("2 - Ver pacientes cadastrados")
    print("3 - Dados de um paciente")
    print("4 - Atualizar dados do paciente")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            cadastroPaciente() 
        elif op == '2':
            hospital.listarPacientes()
        elif op == '3':
            nome = input("Digite o nome do paciente: ")
            hospital.mostrarPaciente(nome)
        elif op == '4':
            atualizar_dados_paciente()
        else:
            print("Opção inválida.")
        op = input("Escolha: ")

    clear_screen()


def funcionario_manager(hospital):
    print("\n--- GERENCIAR FUNCIONÁRIOS ---")
    print("1 - Adicionar funcionário")
    print("2 - Remover funcionário")
    print("3 - Listar funcionários")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do funcionário: ")
            registro = input("Registro profissional: ")
            tipo = input("Tipo (Medico, Enfermeiro, Dentista, Psicologo, Nutricionista, Fisioterapeuta): ").strip().lower()
            print("Especialidades disponíveis: Cardiologista, Ortopedista, Pediatra, Neurologista, Clínico Geral, Dermatologista, Oftalmologista")
            especialidade = input("Especialidade (caso for Médico): ")
           
            try:
                hospital.adicionar_funcionario(tipo, nome, registro, especialidade)
                break
            except ValueError as ve:
                print(f"Erro ao adicionar funcionário: {ve}")
        elif op == '2':
            nome = input("Nome do funcionário a remover: ")
            registro = input("Registro profissional: ")
            hospital.remover_funcionario(nome, registro)
            break
        elif op == '3':
            hospital.listar_funcionarios()
            break
        else:
            print("Opção inválida.")
    clear_screen()


#Funções para agendamento
def agendarConsulta():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        dia = input("Data da consulta (dd/mm): ")
        # Peça o tipo de profissional
        tipo_profissional = input("Tipo de profissional (Medico, Dentista, etc.): ")
        hospital.agendar_consulta(nome, dia, tipo_profissional)
    else:
        print("Paciente não encontrado.")
        resposta = input("Deseja cadastrá-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome)
            dia = input("Data da consulta (dd/mm): ")
            tipo_profissional = input("Tipo de profissional (Medico, Dentista, etc.): ")
            hospital.agendar_consulta(nome, dia, tipo_profissional)

def remarcarConsulta():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
       if paciente.consultas:
           for i, (dia, medico) in enumerate(paciente.consultas, 1):
               print(f"{i}: Dia {dia} com Dr(a). {medico}")
           escolha = int(input("Escolha o número da consulta a remarcar: ")) - 1
           novo_dia = input("Novo dia da consulta: ")
           hospital.remarcar_consulta(nome, escolha, novo_dia)
       else:
           print("Nenhuma consulta agendada.")
    else:
       print("Paciente não encontrado.")

def cancelarConsulta():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        if paciente.consultas:
            for i, (dia, medico) in enumerate(paciente.consultas, 1):
                print(f"{i}: Dia {dia} com Dr(a). {medico}")
            escolha = int(input("Escolha o número da consulta a cancelar: ")) - 1
            hospital.cancelar_consulta(nome, escolha)
        else:
            print("Nenhuma consulta agendada.")
    else:
        print("Paciente não encontrado.")

def menu_agendamento():
    print("\n--- AGENDAMENTO ---")
    print("1 - Agendar consulta")
    print("2 - Remarcar consulta")
    print("3 - Cancelar consulta")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            agendarConsulta()
        elif op == '2':
            remarcarConsulta()
        elif op == '3':
            cancelarConsulta()
        else:
            print("Opção inválida.")
        op = input("Escolha: ")
    clear_screen()

#Função para prontuario
def prontuarioMedico():
    nome = input("Digite o nome do paciente: ")
    #nome = "Davi Celestino"
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        profissional = input("Nome do profissional de saúde: ")
        descricao = input("Descrição do prontuário: ")
        hospital.registrar_prontuario(nome, profissional, descricao)
        input("Prontuário registrado. Pressione Enter para continuar...")
        clear_screen()
    else:
        print("Paciente não encontrado")
        resposta = input("Deseja cadastrá-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente()
            profissional = input("Nome do profissional de saúde: ")
            descricao = input("Descrição do prontuário: ")
            hospital.registrar_prontuario(nome, profissional, descricao)
            input("Prontuário registrado. Pressione Enter para continuar...")
            clear_screen()

#Solicitação de exame
def solicitarExame():
    nome_paciente = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome_paciente)

    if not paciente:
        print("Paciente não encontrado.")
        # Lógica opcional para cadastrar o paciente
        resposta = input("Deseja cadastrá-lo? (sim/nao) ")
        if resposta.lower() == "sim":
            cadastroPaciente()
            solicitarExame() # Tenta novamente
        return

    # 1. Escolher o profissional
    print("\n--- Profissionais Disponíveis ---")
    for func in hospital.funcionarios:
        print(f"- {func.nome} ({func.__class__.__name__})")
    
    nome_profissional = input("Nome do profissional que está solicitando: ")

    # 2. Encontrar o objeto do profissional
    profissional_encontrado = None
    for func in hospital.funcionarios:
        if func.nome.lower() == nome_profissional.lower():
            profissional_encontrado = func
            break
    
    if not profissional_encontrado:
        print(f"Profissional '{nome_profissional}' não encontrado.")
        return

    # 3. Mostrar apenas os exames permitidos para esse profissional
    print(f"\n--- Exames que {profissional_encontrado.nome} pode solicitar ---")
    
    # Importa o dicionário de exames
    #from entidades.exame import EXAMES_DISPONIVEIS 
    
    # Verifica se o profissional tem exames permitidos
    if not profissional_encontrado.exames_permitidos:
        print("Este profissional não solicita exames.")
        return

    # Itera sobre a lista de exames permitidos do profissional
    for codigo_exame in profissional_encontrado.exames_permitidos:
        # Pega o nome completo do exame do dicionário principal
        exame_obj = EXAMES_DISPONIVEIS.get(codigo_exame)
        if exame_obj:
            print(f"- {codigo_exame}: {exame_obj.nome}")

    # 4. Solicitar o exame
    codigo_selecionado = input("Digite o código do exame a solicitar: ").lower()
    #codigo_selecionado = "limpeza"
    
    # Chama a função do hospital, que aplicará o polimorfismo
    hospital.solicitar_exame(nome_paciente, nome_profissional, codigo_selecionado)

def queixa():
    print("\n--- REGISTRO DE QUEIXAS ---")
    print("1 - Registrar queixa")
    print("2 - Ver queixa")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            print("Registre uma queixa: ")
            funcionario = input("Digite o nome do funcionário: ")
            descricao = input("Descreva o ocorrido: ")
            hospital.administrativo.registrar_queixa(funcionario,descricao)
        elif op == '2':
            hospital.administrativo.exibir_queixas()
        else: 
            print("Opção inválida!")
        print()
        op = input("Escolha: ")
    clear_screen()

def relatorios_menu(hospital):
    print("\n--- GERAÇÃO DE RELATÓRIOS ---")
    print("1 - Relatório de Paciente")
    print("2 - Relatório da Equipe de Saúde")
    print("3 - Relatório Geral do Hospital")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do paciente: ")
            hospital.gerar_pdf_paciente(nome)
        elif op == '2':
            hospital.gerar_pdf_equipe()
        elif op == '3':
            hospital.gerar_pdf_hospital()
        else:
            print("Opção inválida.")
        
        print()
        op = input("Escolha: ")
    clear_screen()