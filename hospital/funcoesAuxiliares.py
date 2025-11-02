from entidades.exame import EXAMES_DISPONIVEIS
from entidades.paciente import PacienteBuilder, DiretorPaciente, HistoricoMedico
from entidades.exceptions import (EstoqueInvalidoException, CampoObrigatorioException, PacienteNaoEncontradoException, 
ProfissionalNaoEncontradoException, ContatoInvalidoException, FuncionarioDuplicadoException, 
RegistroInvalidoException, DadosInvalidosException, EstoqueMaximoException, LeitoIndisponivelException)
import os

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

def validar_item_estoque(item, quantidade):
    if not item:
        raise CampoObrigatorioException("Item de estoque")
    if quantidade <= 0:
        raise EstoqueInvalidoException(quantidade, item)
    if quantidade > 1000:
        raise EstoqueMaximoException(item)
    if item.strip().isdigit():
        raise ValueError("❌ ERRO: Nome do item não pode ser apenas números.")
    
    if not any(char.isalpha() for char in item):
        raise ValueError("❌ ERRO: Nome do item deve conter pelo menos uma letra.")

    for char in item:
        if not (char.isalnum() or char.isspace()):
            raise ValueError("❌ ERRO: Nome do item contém caracteres inválidos.")

def estoque_menu(hospital):
    while True:
        clear_screen()
        print("\n--- ESTOQUE ---")
        print("1 - Adicionar item")
        print("2 - Ver estoque")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            try:
                item = input("Item: ")
                qtd_input = input("Quantidade: ")
                try:
                    qtd = int(qtd_input)
                except ValueError:
                    print(DadosInvalidosException("Quantidade"))
                    input("Pressione Enter para continuar...")
                    continue
                validar_item_estoque(item, qtd)
                hospital.add_item_estoque(item, qtd)
                input("Item adicionado. Pressione Enter para continuar...")
            except (CampoObrigatorioException, EstoqueInvalidoException, EstoqueMaximoException, ValueError) as e:
                print(f"{e}")
                input("Pressione Enter para continuar...")
        elif op == '2':
            hospital.ver_estoque()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def funcionarios(hospital):
    while True:
        clear_screen()
        print("\n--- FUNCIONÁRIOS ---")
        print("1 - Queixa")
        print("2 - Escalonar funcionário")
        print("3 - Gerenciamento de funcionários")
        print("4 - Ver notificações de emergência")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            queixa()
        elif op == '2':
            escalonamento_menu(hospital)
        elif op == '3':
            funcionario_manager(hospital)
        elif op == '4':
            hospital.notificacoes_emergencia()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def receituario_menu(hospital):
    while True:
        clear_screen()
        print("\n--- RECEITUÁRIO ---")
        print("1 - Gerar receita")
        print("2 - Ver receitas")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            nome = input("Nome do paciente: ")
            medicamento = input("Medicamento: ")
            descricao = input("Descrição: ")
            profissional = input("Profissional: ")
            dosagem = input("Dosagem: ")
            hospital.receita(nome, profissional, medicamento, descricao, dosagem)
            input("Receita gerada. Pressione Enter para continuar...")
        elif op == '2':
            nome = input("Nome do paciente: ")
            hospital.receitas(nome)
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def emergencias_menu(hospital):
    while True:
        clear_screen()
        print("\n--- EMERGÊNCIAS ---")
        print("1 - Registrar emergência")
        print("2 - Ver emergências")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            nome = input("Nome do paciente: ")
            try:
                hospital.encontrar_paciente(nome)
            except PacienteNaoEncontradoException as e:
                print(e)
                input("Pressione Enter para continuar...")
                return

            prioridade = input("Prioridade (alta/media/baixa): ").lower()
            if hospital.registrar_emergencia(nome, prioridade):
                print("Emergência registrada com sucesso!")
                if prioridade == 'alta':
                    try:
                        hospital.alocar_leito(nome)
                        print(f"Paciente {nome} foi automaticamente alocado em um leito devido à prioridade alta.")
                    except LeitoIndisponivelException as e:
                        print(e)
                    except Exception as e:
                        print(f"⚠️  Erro inesperadono alocamento automático: {e}")
                input("Pressione Enter para continuar...")
            else:
                input("Pressione Enter para continuar...")
        elif op == '2':
            hospital.ver_emergencias()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

        
def escalonamento_menu(hospital):
    while True:
        clear_screen()
        print("\n--- ESCALONAMENTO ---")
        print("1 - Escalar funcionário")
        print("2 - Ver escalonamento")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            try:
                nome = input("Nome do funcionário: ")
                hospital.encontrar_funcionario(nome)
            except ProfissionalNaoEncontradoException as e:
                print(e)
                input("Pressione Enter para continuar...")
                return
            try:
                turno = input("Turno (manhã/tarde/noite): ")
                if turno not in ['manhã', 'tarde', 'noite']:
                    raise ValueError("Turno inválido.")
                hospital.escalar(nome, turno)
                input("Funcionário escalado. Pressione Enter para continuar...")
            except ValueError as e:
                print(f"ERRO: {e}")
                input("Pressione Enter para continuar...")
        elif op == '2':
            hospital.ver_escalas()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

paciente_builder = PacienteBuilder()
diretor_paciente = DiretorPaciente(paciente_builder)

def cadastro_simples():
    clear_screen()
    print("\n--- CADASTRO SIMPLES ---")
    try:
        input_nome = input("Nome do paciente: ")
        if not input_nome:
            raise CampoObrigatorioException("Nome")
    except CampoObrigatorioException as e:
        print(f"{e}")
        input("Pressione Enter para continuar...")
        return None
    
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
        input("Pressione Enter para continuar...")
        return None
    
def cadastro_completo():
    clear_screen()
    print("\n--- CADASTRO COMPLETO ---")
    dados = {}
    try:
        dados['nome'] = input("Nome do paciente: ")
        if not dados['nome']:
            raise CampoObrigatorioException("Nome")
    except CampoObrigatorioException as e:
        print(f"{e}")
        input("Pressione Enter para continuar...")
        return None
    
    dados['cpf'] = input("CPF: ") or None
    dados['cartao_sus'] = input("Cartão SUS(Se houver): ") or None
    
    try:
        idade_input = input("Idade: ").strip()
        if idade_input:
            dados['idade'] = int(idade_input)
        else:
            dados['idade'] = None
    except ValueError:
        print(DadosInvalidosException("Idade"))
        dados['idade'] = None
    
    try:
        altura_input = input("Altura (em cm): ").strip()
        if altura_input:
            dados['altura'] = float(altura_input)
        else:
            dados['altura'] = None
    except ValueError:
        print(DadosInvalidosException("Altura"))
        dados['altura'] = None
    
    try:
        peso_input = input("Peso (em kg): ").strip()
        if peso_input:
            dados['peso'] = float(peso_input)
        else:
            dados['peso'] = None
    except ValueError:
        print(DadosInvalidosException("Peso"))
        dados['peso'] = None
    
    try:
        tipo_sanguineo_input = input("Tipo Sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip()
        if tipo_sanguineo_input:
            tipos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
            if tipo_sanguineo_input not in tipos_validos:
                raise ValueError("Tipo sanguíneo inválido")
            dados['tipo_sanguineo'] = tipo_sanguineo_input
        else:
            dados['tipo_sanguineo'] = None
    except ValueError:
        print(DadosInvalidosException("Tipo Sanguíneo"))
        dados['tipo_sanguineo'] = None
    
    try:
        genero_input = input("Gênero (Masculino, Feminino, Outro): ").strip()
        if genero_input:
            generos_validos = ['masculino', 'feminino', 'outro']
            if genero_input.lower() not in generos_validos:
                raise ValueError("Gênero inválido")
            dados['genero'] = genero_input
        else:
            dados['genero'] = None
    except ValueError:
        print(DadosInvalidosException("Gênero"))
        dados['genero'] = None
    
    try:
        tipo_plano_input = input("Tipo de Plano (Particular, SUS, Convênio): ").strip()
        if tipo_plano_input:
            planos_validos = ['particular', 'sus', 'convenio', 'convênio']
            if tipo_plano_input.lower() not in planos_validos:
                raise ValueError("Tipo de plano inválido")
            dados['tipo_plano'] = tipo_plano_input
        else:
            dados['tipo_plano'] = None
    except ValueError:
        print(DadosInvalidosException("Tipo de Plano"))
        dados['tipo_plano'] = None
    
    # Se o tipo de plano for Convênio, perguntar qual convênio
    if dados['tipo_plano'] and (dados['tipo_plano'].lower() == 'convenio' or dados['tipo_plano'].lower() == 'convênio'):
        try:
            print("Convênios disponíveis: Unimed, Amil, Hapvida, Bradesco, SulAmérica")
            convenio_input = input("Tipo de Convênio: ").strip()
            if convenio_input:
                convenios_validos = ['unimed', 'amil', 'hapvida', 'bradesco', 'sulamérica']
                if convenio_input.lower() not in convenios_validos:
                    raise ValueError("Convênio inválido")
                dados['tipo_convenio'] = convenio_input
            else:
                dados['tipo_convenio'] = None
        except ValueError:
            print(DadosInvalidosException("Tipo de Convênio"))
            dados['tipo_convenio'] = None
    else:
        dados['tipo_convenio'] = None
    
    try:
        telefone_input = input("Telefone (DDD) XXXX-XXXX: ").strip()
        if telefone_input:
            if not telefone_input.isdigit() or len(telefone_input) < 10:
                raise ValueError("Telefone inválido")
            dados['telefone'] = telefone_input
        else:
            dados['telefone'] = None
    except ValueError:
        print(DadosInvalidosException("Telefone"))
        dados['telefone'] = None
    
    try:
        nome_emergencia = input("Nome do contato de emergência: ").strip()
        tel_emergencia = input("Telefone do contato de emergência (DDD) XXXX-XXXX: ").strip()
        
        if nome_emergencia and tel_emergencia:
            if not tel_emergencia.isdigit() or len(tel_emergencia) < 10:
                raise ValueError("Telefone de emergência inválido")
            dados['contato_emergencia'] = (nome_emergencia, tel_emergencia)
        else:
            dados['contato_emergencia'] = None
    except ValueError:
        print(DadosInvalidosException("Contato de Emergência"))
        dados['contato_emergencia'] = None

    dados['historico_medico'] = coletar_historico_medico()

    try:
        paciente = diretor_paciente.construir_paciente_completo(dados)
        hospital.pacientes.append(paciente)
        print(f"Paciente {dados['nome']} cadastrado com sucesso!")
        input("Pressione Enter para continuar...")
        return paciente
    except Exception as e:
        print(f"Erro inesperado no cadastro: {e}")
        input("Pressione Enter para continuar...")
        return None
    
def coletar_historico_medico():
    h = HistoricoMedico()
    while True:
        clear_screen()
        print("\n--- HISTÓRICO MÉDICO ---")
        print("1 - Adicionar alergia")
        print("2 - Adicionar doença crônica")
        print("3 - Adicionar cirurgia")
        print("4 - Adicionar medicação de uso")
        print("5 - Adicionar observação")
        print("6 - Ver resumo atual")
        print("0 - Finalizar histórico")
        op = input("Escolha: ").strip()

        if op == '0':
            return h
        elif op == '1':
            txt = input("Alergia (ex: Dipirona): ").strip()
            if txt: 
                h.adicionar_alergia(txt)
                print("Alergia adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '2':
            txt = input("Doença crônica (ex: Hipertensão): ").strip()
            if txt: 
                h.adicionar_doenca_cronica(txt)
                print("Doença crônica adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '3':
            txt = input("Cirurgia (ex: Apendicectomia - 2019): ").strip()
            if txt: 
                h.adicionar_cirurgia(txt)
                print("Cirurgia adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '4':
            txt = input("Medicação (ex: Losartana 50mg 1cp/dia): ").strip()
            if txt: 
                h.adicionar_medicamento(txt)
                print("Medicação adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '5':
            txt = input("Observação livre: ").strip()
            if txt: 
                h.adicionar_observacao(txt)
                print("Observação adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '6':
            print("\n>>> Resumo parcial:")
            print(h.resumo() or "Nenhum histórico registrado.")
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")     
    
   

def editar_historico_medico(paciente):
    clear_screen()
    print("\n--- EDITAR HISTÓRICO MÉDICO ---")
    print("Histórico atual:")
    print(paciente.historico_medico.resumo() or "Nenhum histórico registrado.")
    resp = input("Deseja alterar/adicionar informações? (s/n): ").strip().lower()
    if resp != 's':
        return

    h = paciente.historico_medico  
    while True:
        clear_screen()
        print("\n--- EDITAR HISTÓRICO MÉDICO ---")
        print("1 - Adicionar alergia")
        print("2 - Adicionar doença crônica")
        print("3 - Adicionar cirurgia")
        print("4 - Adicionar medicação")
        print("5 - Adicionar observação")
        print("6 - Ver resumo")
        print("0 - Finalizar")
        op = input("Escolha: ").strip()
        
        if op == '0':
            input("Histórico atualizado. Pressione Enter para continuar...")
            return
        elif op == '1':
            t = input("Alergia: ").strip()
            if t: 
                h.adicionar_alergia(t)
                print("Alergia adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '2':
            t = input("Doença crônica: ").strip()
            if t: 
                h.adicionar_doenca_cronica(t)
                print("Doença crônica adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '3':
            t = input("Cirurgia: ").strip()
            if t: 
                h.adicionar_cirurgia(t)
                print("Cirurgia adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '4':
            t = input("Medicação: ").strip()
            if t: 
                h.adicionar_medicamento(t)
                print("Medicação adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '5':
            t = input("Observação: ").strip()
            if t: 
                h.adicionar_observacao(t)
                print("Observação adicionada!")
                input("Pressione Enter para continuar...")
        elif op == '6':
            print("\n>>> Resumo atual:")
            print(h.resumo() or "Nenhum histórico registrado.")
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


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
        try:
            nova_idade = input(f"Idade atual: {paciente.idade} | Nova idade: ").strip()
            if nova_idade:
                b.com_idade(int(nova_idade))
        except ValueError:
            print(DadosInvalidosException("Idade"))
        
        try:
            nova_altura = input(f"Altura atual: {paciente.altura} | Nova altura (em cm): ").strip()
            if nova_altura:
                b.com_altura(float(nova_altura))
        except ValueError:
            print(DadosInvalidosException("Altura"))
        
        try:
            novo_peso = input(f"Peso atual: {paciente.peso} | Novo peso (em kg): ").strip()
            if novo_peso:
                b.com_peso(float(novo_peso))
        except ValueError:
            print(DadosInvalidosException("Peso"))
        
        try:
            novo_ts = input(
                f"Tipo Sanguíneo atual: {paciente.tipo_sanguineo} | Novo (A+, A-, B+, B-, AB+, AB-, O+, O-): "
            ).strip()
            if novo_ts:
                tipos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
                if novo_ts not in tipos_validos:
                    raise ValueError("Tipo sanguíneo inválido")
                b.com_tipo_sanguineo(novo_ts)
        except ValueError:
            print(DadosInvalidosException("Tipo Sanguíneo"))
        
        try:
            novo_genero = input(
                f"Gênero atual: {paciente.genero} | Novo Gênero (Masculino, Feminino, Outro): "
            ).strip()
            if novo_genero:
                generos_validos = ['masculino', 'feminino', 'outro']
                if novo_genero.lower() not in generos_validos:
                    raise ValueError("Gênero inválido")
                b.com_genero(novo_genero)
        except ValueError:
            print(DadosInvalidosException("Gênero"))
        
        try:
            novo_plano = input(
                f"Tipo de Plano atual: {paciente.tipo_plano} | Novo Tipo de Plano (Particular, SUS, Convênio): "
            ).strip()
            if novo_plano:
                planos_validos = ['particular', 'sus', 'convenio', 'convênio']
                if novo_plano.lower() not in planos_validos:
                    raise ValueError("Tipo de plano inválido")
                b.com_tipo_plano(novo_plano)
                # Se o novo plano for Convênio, perguntar qual convênio
                if novo_plano.lower() == 'convênio' or novo_plano.lower() == 'convenio':
                    try:
                        print("Convênios disponíveis: Unimed, Amil, Hapvida, Bradesco, SulAmérica")
                        novo_convenio = input(
                            f"Convênio atual: {paciente.tipo_convenio} | Novo Convênio: "
                        ).strip()
                        if novo_convenio:
                            convenios_validos = ['unimed', 'amil', 'hapvida', 'bradesco', 'sulamérica']
                            if novo_convenio.lower() not in convenios_validos:
                                raise ValueError("Convênio inválido")
                            b.com_tipo_convenio(novo_convenio)
                    except ValueError:
                        print(DadosInvalidosException("Tipo de Convênio"))
        except ValueError:
            print(DadosInvalidosException("Tipo de Plano"))
        
        try:
            novo_tel = input(
                f"Telefone atual: {paciente.telefone} | Novo Telefone (apenas números): "
            ).strip()
            if novo_tel:
                if not novo_tel.isdigit() or len(novo_tel) < 10:
                    raise ValueError("Telefone inválido")
                b.com_telefone(novo_tel)
        except ValueError:
            print(DadosInvalidosException("Telefone"))
        
        try:
            print(f"Contato de Emergência atual: {paciente.contato_emergencia}")
            novo_nome_emerg = input("Novo nome do contato de emergência: ").strip()
            novo_tel_emerg = input("Novo telefone do contato de emergência (apenas números): ").strip()
            if novo_nome_emerg and novo_tel_emerg:
                if not novo_tel_emerg.isdigit() or len(novo_tel_emerg) < 10:
                    raise ValueError("Telefone de emergência inválido")
                b.com_contato_emergencia((novo_nome_emerg, novo_tel_emerg))
            elif novo_nome_emerg or novo_tel_emerg:
                print("Para atualizar o contato de emergência, forneça nome e telefone juntos.")
        except ValueError:
            print(DadosInvalidosException("Contato de Emergência"))


        editar = input("Deseja editar o histórico médico? (s/n): ").strip().lower()
        if editar == 's':
            editar_historico_medico(paciente)  
            b.com_historico_medico(paciente.historico_medico)

        paciente_atualizado = b.atualizar(paciente)
        print(f"Paciente {paciente_atualizado.nome} atualizado com sucesso!")
        input("Pressione Enter para continuar...")
        return paciente_atualizado

    except Exception as e:
        print(f"Erro ao atualizar paciente: {e}")
        input("Pressione Enter para continuar...")
        return None

    
# Função de cadastro modificada para funcionar com Builder
def cadastroPaciente():
    while True:
        clear_screen()
        print("\n--- CADASTRO DE PACIENTE ---")
        print("1 - Cadastro simples")
        print("2 - Cadastro completo")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            cadastro_simples()
            break
        elif op == '2':
            cadastro_completo()
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

#Função mais robusta para cadastrar e ver os pacientes
def cadastro():
    while True:
        clear_screen()
        print("\n--- CENTRAL DE PACIENTES ---")
        print("1 - Cadastrar paciente")
        print("2 - Ver pacientes cadastrados")
        print("3 - Dados de um paciente")
        print("4 - Atualizar dados do paciente")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            cadastroPaciente() 
        elif op == '2':
            hospital.listar_pacientes()
            input("Pressione Enter para continuar...")
        elif op == '3':
            nome = input("Digite o nome do paciente: ")
            hospital.detalhes_paciente(nome)
            input("Pressione Enter para continuar...")
        elif op == '4':
            atualizar_dados_paciente()
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def funcionario_manager(hospital):
    while True:
        clear_screen()
        print("\n--- GERENCIAR FUNCIONÁRIOS ---")
        print("1 - Adicionar funcionário")
        print("2 - Remover funcionário")
        print("3 - Listar funcionários")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            try:
                nome = input("Nome do funcionário: ")
                if any(char.isdigit() for char in nome):
                    raise ValueError("Nome não pode conter números;")
                if not nome.strip():
                    raise ValueError("Nome não pode estar vazio;")
            except ValueError as e:
                print(f"ERRO: {e}")
                input("Pressione Enter para continuar...")
                continue
            try:
                registro = input("Registro profissional(Ex: CRM002): ")
                if not registro.strip():
                    raise RegistroInvalidoException("Registro profissional não pode estar vazio.")

            except RegistroInvalidoException as e:
                print(f"{e}")
                input("Pressione Enter para continuar...")
                continue

            try:
                tipo = input("Tipo (Médico, Enfermeiro, Dentista, Psicologo, Nutricionista, Fisioterapeuta.): ").strip().lower()
                tipo = tipo.replace("médico", "medico").replace("psicólogo", "psicologo")
                tipos_validos = ["medico", "enfermeiro", "dentista", "psicologo", "nutricionista", "fisioterapeuta"]
                if tipo not in tipos_validos:
                    raise ValueError(f"Tipo '{tipo}' inválido. Tipos válidos: {', '.join(tipos_validos)}")
            except ValueError as e:
                print(f"ERRO: {e}")
                input("Pressione Enter para continuar...")
                continue
            
            print("Especialidades disponíveis: Cardiologista, Ortopedista, Pediatra, Neurologista, Clínico Geral, Dermatologista, Oftalmologista.")
            especialidade = input("Especialidade (caso for Médico, vazio caso não for): ")
            email = input("Email (example@email.com): ")
            whatsapp = input("WhatsApp (55 (DDD) 9XXXX-XXXX): ")
        
            try:
                hospital.adicionar_funcionario(tipo, nome, registro, especialidade, email, whatsapp)
                print("Funcionário adicionado com sucesso!")
                input("Pressione Enter para continuar...")
            except (ContatoInvalidoException, FuncionarioDuplicadoException, RegistroInvalidoException, ValueError) as e:
                print(f"Erro ao adicionar funcionário: {e}")
                input("Pressione Enter para continuar...")

        elif op == '2':
            hospital.listar_funcionarios()
            nome = input("\nNome do funcionário a remover(Pressione 'Enter' duas vezes para cancelar): ")
            registro = input("Registro profissional: ")
            try:
                hospital.remover_funcionario(nome, registro)
                print("Funcionário removido com sucesso!")
            except ProfissionalNaoEncontradoException as e:
                print(f"{e}")
            input("Pressione Enter para continuar...")
        elif op == '3':
            hospital.listar_funcionarios()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


#Funções para agendamento
def agendarConsulta():
    try:
        nome = input("Nome do paciente: ")
        paciente = hospital.encontrar_paciente(nome)
    except PacienteNaoEncontradoException as e:
        print(e)
        input("Pressione Enter para continuar...")
        return
    dia = input("Data da consulta (dd/mm): ")
    tipo_profissional = input("Tipo de profissional (Medico, Dentista, etc.): ")
    hospital.agendar_consulta(nome, dia, tipo_profissional)
    print("Consulta agendada com sucesso!")


def remarcarConsulta():
    try:
        nome = input("Nome do paciente: ")
        paciente = hospital.encontrar_paciente(nome)
    except PacienteNaoEncontradoException as e:
        print(e)
        input("Pressione Enter para continuar...")
        return
    
    if paciente.consultas:
        for i, (dia, medico) in enumerate(paciente.consultas, 1):
            print(f"{i}: Dia {dia} com Dr(a). {medico}")
        try:
            escolha = int(input("Escolha o número da consulta a remarcar: ")) - 1
        except ValueError:
            print(DadosInvalidosException("Número da consulta"))
            input("Pressione Enter para continuar...")
            return
        novo_dia = input("Novo dia da consulta: ")
        hospital.remarcar_consulta(nome, escolha, novo_dia)
        print("Consulta remarcada com sucesso!")
    else:
        print("Nenhuma consulta agendada.")
  

def cancelarConsulta():
    try:
        nome = input("Nome do paciente: ")
        paciente = hospital.encontrar_paciente(nome)
    except PacienteNaoEncontradoException as e:
        print(e)
        input("Pressione Enter para continuar...")
        return
  
    if paciente.consultas:
        for i, (dia, medico) in enumerate(paciente.consultas, 1):
            print(f"{i}: Dia {dia} com Dr(a). {medico}")
        try:
            escolha = int(input("Escolha o número da consulta a cancelar: ")) - 1
        except ValueError:
            print(DadosInvalidosException("Número da consulta"))
            input("Pressione Enter para continuar...")
            return
        hospital.cancelar_consulta(nome, escolha)
        print("Consulta cancelada com sucesso!")
    else:
        print("Nenhuma consulta agendada.")
  
def menu_agendamento():
    while True:
        clear_screen()
        print("\n--- AGENDAMENTO ---")
        print("1 - Agendar consulta")
        print("2 - Remarcar consulta")
        print("3 - Cancelar consulta")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            agendarConsulta()
            input("Pressione Enter para continuar...")
        elif op == '2':
            remarcarConsulta()
            input("Pressione Enter para continuar...")
        elif op == '3':
            cancelarConsulta()
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

#Função para prontuario
def prontuarioMedico():
    try:
        nome = input("Digite o nome do paciente: ")
        paciente = hospital.encontrar_paciente(nome)
    except PacienteNaoEncontradoException as e:
        print(e)
        input("Pressione Enter para continuar...")
        return
    try:
        profissional = input("Nome do profissional de saúde: ")
        hospital.encontrar_funcionario(profissional)
    except ProfissionalNaoEncontradoException as e:
        print(e)
        input("Pressione Enter para continuar...")
        return
    descricao = input("Descrição do prontuário: ")
    hospital.registrar_prontuario(nome, profissional, descricao)
    input("Pressione Enter para continuar...")


#Solicitação de exame

def exame_menu(hospital):
    while True:
        clear_screen()
        print("\n--- SOLICITAÇÃO DE EXAMES ---")
        print("1 - Solicitar exame")
        print("2 - Pacotes de exames")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            solicitarExame()
            input("Pressione Enter para continuar...")
        elif op == '2':
            try:
                nome_paciente = input("Nome do paciente: ")
                paciente_obj = hospital.encontrar_paciente(nome_paciente)
            except PacienteNaoEncontradoException as e:
                print(e)
                input("Pressione Enter para continuar...")
                continue

            print("\n--- Profissionais Disponíveis ---")
            for func in hospital.funcionarios:
                print(f"- {func.nome} ({func.__class__.__name__})")

            try:
                nome_profissional = input("Nome do profissional: ")
                profissional_obj = hospital.encontrar_funcionario(nome_profissional)
            except ProfissionalNaoEncontradoException as e:
                print(e)
                input("Pressione Enter para continuar...")
                continue
            
            print("Pacotes disponíveis:\n" 
                  "- checkup_basico\n"
                  "- avaliacao_cardiaca\n"
                  "- pre_operatorio\n"
                  "- checkup_feminino\n"
                  "- avaliacao_odonto\n"
                  "- super_checkup")
            codigo_pacote = input("Código do pacote de exames: ").lower()

            hospital.solicitar_pacote_exames_direto(paciente_obj, profissional_obj, codigo_pacote)
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def solicitarExame():
    try:
        nome_paciente = input("Nome do paciente: ")
        paciente = hospital.encontrar_paciente(nome_paciente)
    except PacienteNaoEncontradoException as e:
        print(e)
        return
    
    print("\n--- Profissionais Disponíveis ---")
    for func in hospital.funcionarios:
        print(f"- {func.nome} ({func.__class__.__name__})")

    try:
        nome_profissional = input("Nome do profissional que está solicitando: ")
        profissional = hospital.encontrar_funcionario(nome_profissional)
    except ProfissionalNaoEncontradoException as e:
        print(e)
        return

    print(f"\n--- Exames que {profissional.nome} pode solicitar ---")
    
    # Verifica se o profissional tem exames permitidos
    if not profissional.exames_permitidos:
        print("Este profissional não solicita exames.")
        return

    # Itera sobre a lista de exames permitidos do profissional
    for codigo_exame in profissional.exames_permitidos:
        # Pega o nome completo do exame do dicionário principal
        exame_obj = EXAMES_DISPONIVEIS.get(codigo_exame)
        if exame_obj:
            print(f"- {codigo_exame}: {exame_obj.nome}")

    codigo_selecionado = input("Digite o código do exame a solicitar: ").lower()

    # Verificar se o código existe no dicionário antes de solicitar
    if codigo_selecionado not in EXAMES_DISPONIVEIS:
        print("Erro: O código não foi digitado corretamente. Verifique a escrita e tente novamente.")
        return

    hospital.solicitar_exame_direto(paciente, profissional, codigo_selecionado)

def queixa():
    while True:
        clear_screen()
        print("\n--- REGISTRO DE QUEIXAS ---")
        print("1 - Registrar queixa")
        print("2 - Ver queixa")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            print("Registre uma queixa: ")
            try:
                funcionario = input("Digite o nome do funcionário: ")
                hospital.encontrar_funcionario(funcionario)
            except ProfissionalNaoEncontradoException as e:
                print(e)
                input("Pressione Enter para continuar...")
                continue
            descricao = input("Descreva o ocorrido: ")
            hospital.administrativo.registrar_queixa(funcionario,descricao)
            input("Queixa registrada. Pressione Enter para continuar...")
        elif op == '2':
            hospital.administrativo.exibir_queixas()
            input("Pressione Enter para continuar...")
        else: 
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

def leitos_menu(hospital):
    while True:
        clear_screen()
        print("\n--- GERENCIAMENTO DE LEITOS ---")
        print("1 - Alocar leito")
        print("2 - Ver leitos ocupados")
        print("3 - Liberar leito")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            nome = input("Nome do paciente: ")
            try:
                hospital.alocar_leito(nome)
            except LeitoIndisponivelException as e:
                print(f"{e}")
            input("Pressione Enter para continuar...")
        elif op == '2':
            hospital.ver_leitos()
            input("Pressione Enter para continuar...")
        elif op == '3':
            nome = input("Nome do paciente a liberar: ")
            hospital.liberar_leito(nome)
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def relatorios_menu(hospital):
    while True:
        clear_screen()
        print("\n--- GERAÇÃO DE RELATÓRIOS ---")
        print("1 - Relatório de Paciente")
        print("2 - Relatório da Equipe de Saúde")
        print("3 - Relatório Geral do Hospital")
        print("0 - Voltar")
        op = input("Escolha: ")
        
        if op == '0':
            break
        elif op == '1':
            nome = input("Nome do paciente: ")
            hospital.gerar_pdf_paciente(nome)
            input("Relatório gerado. Pressione Enter para continuar...")
        elif op == '2':
            hospital.gerar_pdf_equipe()
            input("Relatório gerado. Pressione Enter para continuar...")
        elif op == '3':
            hospital.gerar_pdf_hospital()
            input("Relatório gerado. Pressione Enter para continuar...")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")