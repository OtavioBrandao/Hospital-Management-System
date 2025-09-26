from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório Hospitalar', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def gerar_relatorio_paciente(paciente):
    pdf = PDF()
    pdf.add_page()
    
    pdf.chapter_title(f'Relatório do Paciente: {paciente.nome}')
    
    # Construir informações básicas
    info_basica = []
    info_basica.append(f"CPF: {paciente.cpf or 'Não informado'}")
    info_basica.append(f"Cartão SUS: {paciente.cartao_sus or 'Não informado'}")
    info_basica.append(f"Idade: {paciente.idade or 'Não informado'}")
    
    if paciente.altura:
        info_basica.append(f"Altura: {paciente.altura}cm")
    else:
        info_basica.append("Altura: Não informado")
    
    if paciente.peso:
        info_basica.append(f"Peso: {paciente.peso}kg")
    else:
        info_basica.append("Peso: Não informado")
    
    if paciente.imc:
        info_basica.append(f"IMC: {paciente.imc:.2f}")
    else:
        info_basica.append("IMC: Não calculável")
    
    if paciente.tipo_sanguineo:
        info_basica.append(f"Tipo Sanguíneo: {paciente.tipo_sanguineo.value}")
    else:
        info_basica.append("Tipo Sanguíneo: Não informado")
    
    if paciente.genero:
        info_basica.append(f"Gênero: {paciente.genero.value}")
    else:
        info_basica.append("Gênero: Não informado")
    
    if paciente.tipo_plano:
        info_basica.append(f"Tipo de Plano: {paciente.tipo_plano.value}")
    else:
        info_basica.append("Tipo de Plano: Não informado")
    
    if paciente.telefone:
        info_basica.append(f"Telefone: {paciente.telefone}")
    else:
        info_basica.append("Telefone: Não informado")
    
    if paciente.contato_emergencia:
        info_basica.append(f"Contato de Emergência: {paciente.contato_emergencia}")
    else:
        info_basica.append("Contato de Emergência: Não informado")
    
    # Juntar todas as informações
    info_completa = "\n".join(info_basica)
    pdf.chapter_body(info_completa)
    
    # Histórico Médico
    if paciente.historico_medico:
        pdf.chapter_title('Histórico Médico')
        historico_texto = paciente.historico_medico.resumo()
        if historico_texto != "Nenhum histórico registrado":
            pdf.chapter_body(historico_texto)
        else:
            pdf.chapter_body("Nenhum histórico médico registrado.")
    else:
        pdf.chapter_title('Histórico Médico')
        pdf.chapter_body("Nenhum histórico médico registrado.")

    # Prontuários
    if paciente.prontuarios:
        pdf.chapter_title('Prontuários Médicos')
        prontuarios_str = ""
        for prontuario in paciente.prontuarios:
            prontuarios_str += f"- {prontuario}\n"
        pdf.chapter_body(prontuarios_str)
    else:
        pdf.chapter_title('Prontuários Médicos')
        pdf.chapter_body("Nenhum prontuário registrado.")

    # Receitas
    if paciente.receitas:
        pdf.chapter_title('Receitas Médicas')
        receitas_str = ""
        for receita in paciente.receitas:
            receitas_str += f"- {receita}\n"
        pdf.chapter_body(receitas_str)
    else:
        pdf.chapter_title('Receitas Médicas')
        pdf.chapter_body("Nenhuma receita registrada.")

    # Consultas
    if paciente.consultas:
        pdf.chapter_title('Consultas Agendadas')
        consultas_str = ""
        for dia, medico in paciente.consultas:
            consultas_str += f"- Dia {dia} com Dr(a). {medico}\n"
        pdf.chapter_body(consultas_str)
    else:
        pdf.chapter_title('Consultas Agendadas')
        pdf.chapter_body("Nenhuma consulta agendada.")

    # Exames
    if paciente.exames:
        pdf.chapter_title('Exames Solicitados')
        exames_str = ""
        for exame in paciente.exames:
            exames_str += f"- {exame}\n"
        pdf.chapter_body(exames_str)
    else:
        pdf.chapter_title('Exames Solicitados')
        pdf.chapter_body("Nenhum exame solicitado.")

    # Salva o PDF
    nome_arquivo = f"relatorio_{paciente.nome.lower().replace(' ', '_')}.pdf"
    pdf.output(nome_arquivo)
    print(f"Relatório do paciente salvo em: {nome_arquivo}")

def gerar_relatorio_equipe(funcionarios):
    pdf = PDF()
    pdf.add_page()

    pdf.chapter_title('Relatório da Equipe de Saúde')

    if not funcionarios:
        pdf.chapter_body("Nenhum funcionário cadastrado.") 
    else:
        for funcionario in funcionarios:
            # Adiciona um subtítulo para cada funcionário
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, f"Profissional: {funcionario.nome}", 0, 1, 'L')

            # Adiciona os detalhes do funcionário
            pdf.set_font('Arial', '', 12)
            info = (
                f"  Registro: {funcionario.registro}\n"
                f"  Profissão: {funcionario.__class__.__name__}"
            )
            if hasattr(funcionario, 'especialidade') and funcionario.especialidade:
                info += f"\n  Especialidade: {funcionario.especialidade}"
            
            pdf.multi_cell(0, 10, info)
            pdf.ln(5) # Adiciona um espaço entre os funcionários

    nome_arquivo = "relatorio_equipe_saude.pdf"
    pdf.output(nome_arquivo)
    print(f"Relatório da equipe salvo em: {nome_arquivo}")

def gerar_relatorio_hospital(hospital):
    pdf = PDF()
    pdf.add_page()
    
    pdf.chapter_title('Relatório Geral do Hospital')

    # Lista de Pacientes
    pdf.chapter_title('Pacientes Cadastrados')
    if hospital.pacientes:
        pacientes_str = ""
        for p in hospital.pacientes:
            pacientes_str += f"- {p.nome}\n"
        pdf.chapter_body(pacientes_str)
    else:
        pdf.chapter_body("Nenhum paciente cadastrado.")

    # Lista de Funcionários
    pdf.chapter_title('Equipe de Profissionais')
    if hospital.funcionarios:
        funcionarios_str = ""
        for f in hospital.funcionarios:
            funcionarios_str += f"- {f.nome} ({f.__class__.__name__})\n"
        pdf.chapter_body(funcionarios_str)
    else:
        pdf.chapter_body("Nenhum funcionário cadastrado.")
    
    # Estoque do Hospital
    pdf.chapter_title('Estoque do Hospital')
    if hospital.estoque.itens:
        estoque_str = ""
        for item, qtd in hospital.estoque.itens.items():
            estoque_str += f"- {item}: {qtd} unidades\n"
        pdf.chapter_body(estoque_str)
    else:
        pdf.chapter_body("Estoque vazio.")

    # Alocação de Leitos
    pdf.chapter_title('Leitos Alocados')
    if hospital.leitos:
        leitos_str = ""
        for leito, paciente_nome in hospital.leitos:
            leitos_str += f"- {leito}: {paciente_nome}\n"
        pdf.chapter_body(leitos_str)
    else:
        pdf.chapter_body("Nenhum leito alocado.")

    # Escalonamento de turnos
    pdf.chapter_title('Escalonamento de Turnos')
    if hospital.escalonamento:
        escalonamento_str = ""
        for nome, turno in hospital.escalonamento.items():
            escalonamento_str += f"- {nome}: {turno}\n"
        pdf.chapter_body(escalonamento_str)
    else:
        pdf.chapter_body("Nenhum escalonamento disponível.")
    
    # Queixas
    pdf.chapter_title('Queixas Registradas')
    if hospital.administrativo.queixas:
        queixas_str = ""
        for funcionario, descricao in hospital.administrativo.queixas:
            queixas_str += f"Funcionário: {funcionario}\nOcorrido: {descricao}\n\n"
        pdf.chapter_body(queixas_str)
    else:
        pdf.chapter_body("Nenhuma queixa registrada.")

    # Emergências
    pdf.chapter_title('Casos de Emergência')
    if hospital.emergencias.emergencias:
        emergencias_str = ""
        for paciente, prioridade in hospital.emergencias.emergencias:
            emergencias_str += f"Paciente: {paciente}\nPrioridade: {prioridade.capitalize()}\n\n"
        pdf.chapter_body(emergencias_str)
    else:
        pdf.chapter_body("Nenhuma emergência registrada.")

    nome_arquivo = "relatorio_geral_hospital.pdf"
    pdf.output(nome_arquivo)
    print(f"Relatório geral do hospital salvo em: {nome_arquivo}")