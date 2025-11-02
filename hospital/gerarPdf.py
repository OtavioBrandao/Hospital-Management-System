from fpdf import FPDF
from abc import ABC, abstractmethod

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

# Template Method Pattern (Esqueleto para montagem de relatórios do hospital)
class RelatorioTemplate(ABC):
    def gerar_relatorio(self, data):
        try:
            pdf = PDF()
            pdf.add_page()
            pdf.chapter_title(self.get_titulo(data))
            self.adicionar_conteudo(pdf, data)
            nome_arquivo = self.get_nome_arquivo(data)
            pdf.output(nome_arquivo)
            print(f"Relatório salvo em: {nome_arquivo}")
            return True
        except (OSError, IOError) as e:
            print(f"ERRO ao salvar relatório: Problema de arquivo - {e}")
            return False
        except AttributeError as e:
            print(f"ERRO ao gerar relatório: Dados inconsistentes - {e}")
            return False
        except Exception as e:
            print(f"ERRO inesperado ao gerar relatório: {e}")
            return False
    
    @abstractmethod
    def get_titulo(self, data):
        pass
    
    @abstractmethod
    def adicionar_conteudo(self, pdf, data):
        pass
    
    @abstractmethod
    def get_nome_arquivo(self, data):
        pass

class RelatorioPaciente(RelatorioTemplate):
    def get_titulo(self, paciente):
        return f'Relatório do Paciente: {paciente.nome}'
    
    def get_nome_arquivo(self, paciente):
        return f"relatorio_{paciente.nome.lower().replace(' ', '_')}.pdf"
    
    def adicionar_conteudo(self, pdf, paciente):
        self._adicionar_info_basica(pdf, paciente)
        self._adicionar_historico(pdf, paciente)
        self._adicionar_prontuarios(pdf, paciente)
        self._adicionar_receitas(pdf, paciente)
        self._adicionar_consultas(pdf, paciente)
        self._adicionar_exames(pdf, paciente)
    
    def _adicionar_info_basica(self, pdf, paciente):
        info = []
        info.append(f"CPF: {paciente.cpf or 'Não informado'}")
        info.append(f"Cartão SUS: {paciente.cartao_sus or 'Não informado'}")
        info.append(f"Idade: {paciente.idade or 'Não informado'}")
        info.append(f"Altura: {paciente.altura}cm" if paciente.altura else "Altura: Não informado")
        info.append(f"Peso: {paciente.peso}kg" if paciente.peso else "Peso: Não informado")
        info.append(f"IMC: {paciente.imc:.2f}" if paciente.imc else "IMC: Não calculável")
        info.append(f"Tipo Sanguíneo: {paciente.tipo_sanguineo.value}" if paciente.tipo_sanguineo else "Tipo Sanguíneo: Não informado")
        info.append(f"Gênero: {paciente.genero.value}" if paciente.genero else "Gênero: Não informado")
        info.append(f"Tipo de Plano: {paciente.tipo_plano.value}" if paciente.tipo_plano else "Tipo de Plano: Não informado")
        info.append(f"Convênio: {paciente.tipo_convenio.value}" if paciente.tipo_convenio else "Convênio: Não informado")
        info.append(f"Telefone: {paciente.telefone}" if paciente.telefone else "Telefone: Não informado")
        info.append(f"Contato de Emergência: {paciente.contato_emergencia}" if paciente.contato_emergencia else "Contato de Emergência: Não informado")
        pdf.chapter_body("\n".join(info))
    
    def _adicionar_historico(self, pdf, paciente):
        pdf.chapter_title('Histórico Médico')
        historico = paciente.historico_medico.resumo() if paciente.historico_medico else "Nenhum histórico médico registrado."
        pdf.chapter_body(historico if historico != "Nenhum histórico registrado" else "Nenhum histórico médico registrado.")
    
    def _adicionar_prontuarios(self, pdf, paciente):
        pdf.chapter_title('Prontuários Médicos')
        if paciente.prontuarios:
            pdf.chapter_body("\n".join(f"- {p}" for p in paciente.prontuarios))
        else:
            pdf.chapter_body("Nenhum prontuário registrado.")
    
    def _adicionar_receitas(self, pdf, paciente):
        pdf.chapter_title('Receitas Médicas')
        if paciente.receitas:
            pdf.chapter_body("\n".join(f"- {r}" for r in paciente.receitas))
        else:
            pdf.chapter_body("Nenhuma receita registrada.")
    
    def _adicionar_consultas(self, pdf, paciente):
        pdf.chapter_title('Consultas Agendadas')
        if paciente.consultas:
            pdf.chapter_body("\n".join(f"- Dia {dia} com Dr(a). {medico}" for dia, medico in paciente.consultas))
        else:
            pdf.chapter_body("Nenhuma consulta agendada.")
    
    def _adicionar_exames(self, pdf, paciente):
        pdf.chapter_title('Exames Solicitados')
        if paciente.exames:
            pdf.chapter_body("\n".join(f"- {e}" for e in paciente.exames))
        else:
            pdf.chapter_body("Nenhum exame solicitado.")

class RelatorioEquipe(RelatorioTemplate):
    def get_titulo(self, funcionarios):
        return 'Relatório da Equipe de Saúde'
    
    def get_nome_arquivo(self, funcionarios):
        return "relatorio_equipe_saude.pdf"
    
    def adicionar_conteudo(self, pdf, funcionarios):
        if not funcionarios:
            pdf.chapter_body("Nenhum funcionário cadastrado.")
        else:
            for funcionario in funcionarios:
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 10, f"Profissional: {funcionario.nome}", 0, 1, 'L')
                pdf.set_font('Arial', '', 12)
                info = f"  Registro: {funcionario.registro}\n  Profissão: {funcionario.__class__.__name__}"
                if hasattr(funcionario, 'especialidade') and funcionario.especialidade:
                    info += f"\n  Especialidade: {funcionario.especialidade}"
                info += f"\n  Email: {funcionario.email}\n  WhatsApp: {funcionario.whatsapp}"
                pdf.multi_cell(0, 10, info)
                pdf.ln(5)

class RelatorioHospital(RelatorioTemplate):
    def get_titulo(self, hospital):
        return 'Relatório Geral do Hospital'
    
    def get_nome_arquivo(self, hospital):
        return "relatorio_geral_hospital.pdf"
    
    def adicionar_conteudo(self, pdf, hospital):
        self._adicionar_pacientes(pdf, hospital)
        self._adicionar_funcionarios(pdf, hospital)
        self._adicionar_estoque(pdf, hospital)
        self._adicionar_leitos(pdf, hospital)
        self._adicionar_escalonamento(pdf, hospital)
        self._adicionar_queixas(pdf, hospital)
        self._adicionar_emergencias(pdf, hospital)
    
    def _adicionar_pacientes(self, pdf, hospital):
        pdf.chapter_title('Pacientes Cadastrados')
        if hospital.pacientes:
            pdf.chapter_body("\n".join(f"- {p.nome}" for p in hospital.pacientes))
        else:
            pdf.chapter_body("Nenhum paciente cadastrado.")
    
    def _adicionar_funcionarios(self, pdf, hospital):
        pdf.chapter_title('Equipe de Profissionais')
        if hospital.funcionarios:
            pdf.chapter_body("\n".join(f"- {f.nome} ({f.__class__.__name__})" for f in hospital.funcionarios))
        else:
            pdf.chapter_body("Nenhum funcionário cadastrado.")
    
    def _adicionar_estoque(self, pdf, hospital):
        pdf.chapter_title('Estoque do Hospital')
        if hospital.estoque.itens:
            pdf.chapter_body("\n".join(f"- {item}: {qtd} unidades" for item, qtd in hospital.estoque.itens.items()))
        else:
            pdf.chapter_body("Estoque vazio.")
    
    def _adicionar_leitos(self, pdf, hospital):
        pdf.chapter_title('Leitos Alocados')
        if hospital.leitos:
            pdf.chapter_body("\n".join(f"- {leito}: {paciente_nome}" for leito, paciente_nome in hospital.leitos))
        else:
            pdf.chapter_body("Nenhum leito alocado.")
    
    def _adicionar_escalonamento(self, pdf, hospital):
        pdf.chapter_title('Escalonamento de Turnos')
        if hospital.escalonamento:
            pdf.chapter_body("\n".join(f"- {nome}: {turno}" for nome, turno in hospital.escalonamento.items()))
        else:
            pdf.chapter_body("Nenhum escalonamento disponível.")
    
    def _adicionar_queixas(self, pdf, hospital):
        pdf.chapter_title('Queixas Registradas')
        if hospital.administrativo.queixas:
            pdf.chapter_body("\n\n".join(f"Funcionário: {funcionario}\nOcorrido: {descricao}" for funcionario, descricao in hospital.administrativo.queixas))
        else:
            pdf.chapter_body("Nenhuma queixa registrada.")
    
    def _adicionar_emergencias(self, pdf, hospital):
        pdf.chapter_title('Casos de Emergência')
        if hospital.emergencias.emergencias:
            pdf.chapter_body("\n\n".join(f"Paciente: {paciente}\nPrioridade: {prioridade.capitalize()}" for paciente, prioridade in hospital.emergencias.emergencias))
        else:
            pdf.chapter_body("Nenhuma emergência registrada.")


def gerar_relatorio_paciente(paciente):
    RelatorioPaciente().gerar_relatorio(paciente)

def gerar_relatorio_equipe(funcionarios):
    RelatorioEquipe().gerar_relatorio(funcionarios)

def gerar_relatorio_hospital(hospital):
    RelatorioHospital().gerar_relatorio(hospital)