
# Sistema de Gestão Hospitalar (POO REFATORADO)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Sistema de gestão hospitalar desenvolvido em Python com foco em Programação Orientada a Objetos (POO). O software permite o gerenciamento completo de pacientes, consultas, exames, leitos, estoque, equipe de saúde e emergências, com a funcionalidade de gerar relatórios em PDF.

## Funcionalidades Implementadas

- ✅ **Cadastro de Pacientes:** Registro de novos pacientes com nome, CPF e cartão do SUS.
- ✅ **Agendamento de Consultas:** Marcação de consultas com profissionais específicos (Médico, Dentista, etc.), aplicando polimorfismo.
- ✅ **Prontuário Médico:** Registro de informações no prontuário do paciente.
- ✅ **Solicitação de Exames:** Cada profissional de saúde pode solicitar exames específicos de sua área a partir de uma lista predefinida.
- ✅ **Gerenciamento de Leitos:** Alocação de leitos para internação.
- ✅ **Controle de Estoque:** Adição e visualização de materiais hospitalares.
- ✅ **Escalonamento de Turnos:** Definição de turnos de trabalho para a equipe.
- ✅ **Gerenciamento de Emergências:** Registro de casos de emergência com sistema de prioridade.
- ✅ **Faturamento:** Cálculo automático de faturas por atendimentos.
- ✅ **Geração de Relatórios em PDF:**
    - ✅ Relatório individual de pacientes.
    - ✅ Relatório completo da equipe de saúde.
    - ✅ Relatório geral do hospital (pacientes e equipe).

## Estrutura do Projeto (POO)

O projeto foi estruturado utilizando os seguintes objetos principais:

- **`Hospital`**: Classe principal que gerencia todas as operações, contendo listas de pacientes, funcionários, leitos, etc.
- **`Paciente`**: Representa os pacientes e armazena suas informações pessoais, prontuários, exames e consultas.
- **`FuncionarioSaude` (Classe Abstrata)**: Modelo base para todos os profissionais de saúde, garantindo que todos implementem métodos essenciais como `atenderPaciente` e `requisitarExame`.
    - **`Medico`, `Enfermeiro`, `Dentista`, `Psicologo`**: Subclasses que herdam de `FuncionarioSaude` e implementam seus comportamentos específicos (polimorfismo).
- **`Estoque`, `SetorAdministrativo`, `EmergenciaManager`**: Classes que gerenciam subsistemas específicos do hospital.
- **`Exame`**: Classe que representa os exames predefinidos que podem ser solicitados.

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.
2.  **Instale as dependências:**
    ```bash
    pip install fpdf
    ```
3.  **Execute o programa:**
    ```bash
    python hospital/main.py
    ```



## Funcionalidades Futuras

- [ ] **Sistema de Login:** Criar perfis de acesso para pacientes e funcionários.
- [ ] **Interface Gráfica (GUI):** Desenvolver uma interface visual para facilitar o uso do sistema.
- [ ] **Banco de Dados:** Substituir o armazenamento em memória por um banco de dados (SQLite, por exemplo) para persistência dos dados.
- [ ] **Testes Unitários:** Implementar testes para garantir a estabilidade do código.
