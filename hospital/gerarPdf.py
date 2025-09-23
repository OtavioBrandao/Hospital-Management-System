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
    
    info = (
        f"CPF: {paciente.cpf or 'Não informado'}\n"
        f"Cartão SUS: {paciente.cartao_sus or 'Não informado'}"
    )
    pdf.chapter_body(info)

    if paciente.consultas:
        pdf.chapter_title('Consultas Agendadas')
        consultas_str = ""
        for dia, medico in paciente.consultas:
            consultas_str += f"- Dia {dia} com Dr(a). {medico}\n"
        pdf.chapter_body(consultas_str)

    if paciente.exames:
        pdf.chapter_title('Exames Solicitados')
        exames_str = ""
        for exame in paciente.exames:
            exames_str += f"- {exame}\n"
        pdf.chapter_body(exames_str)

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

    nome_arquivo = "relatorio_geral_hospital.pdf"
    pdf.output(nome_arquivo)
    print(f"Relatório geral do hospital salvo em: {nome_arquivo}")