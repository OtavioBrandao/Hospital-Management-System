Hospital Management Software (Etapa de Refatoramento)
Vamos refatorar esse projeto utilizando Design Patterns do Python.




READ ME ANTIGO (Ver o que modificar ou não):
Sistema de gestão hospitalar desenvolvido em Python com Programação Orientada a Objetos (POO), permitindo o gerenciamento completo de pacientes, consultas, receitas, exames, leitos, estoque, equipe médica e emergências.

    Projetando o software
        Possíveis objetos a serem usados:
            - FuncionariosSaude -> Estarão contidos os(as) médicos(as) e enfermeiros(as)
            - Médico
            - Enfermeiro
            - Paciente
            - Prontuário médico
            - Setor administrativo --> Responsável por receber queixas contra os funcionáriosSaude, organizar o faturamento do hospital e do paciente

    Possíveis atributos de cada objeto:
        - FuncionariosSaude:
            1. Nome
            2. Profissão (médico ou enfermeiro)
            3. Registro profissional ( medico - CRM; Enfermeiros - COREN)
            /*A classe FucnioraiosSaude será uma classe pai para enfermeiros e médicos*/
        
        -Médico: Vai herdar "FuncionariosSaude"
            1.Especialidade
        
        -Enfermeiro:
            --Por enquanto enfermeiro não terá nenhum atributo particular dele. Pois ainda estou pensando no cenário do enfermeiro
        
        - Paciente:
            1. Nome
            2. Cartão do SUS
            3. CPF ( Caso o paciente não possua cartão do sus)
            4. Histórico médico

        -Prontuário médico:
            1.Profissional da sáude que realizou o prontuário
            2. Informações contidas no prontuário

            obs: analisando com mais atenção, creio que seja melhor que "prontuário médico" passe a ser um atributo ou classe do paciente

        -Setor administrativo:
            1.Queixas (bool)

    Possíveis métodos de cada objeto:
        -FuncionarioSaude:
            1. adicionar funcionario;
            2. Remover funcionario;
            3. Turno dos funcionario;
            4. Atualizar informações do funcionário
        -Médico:
            1. Requisitar exames;
            2. Receitar medicação;
        -Enfermeiro:
            -- Ainda não sei o que um enfermeiro pode fazer, irei pesquisar e implementar as funções específicas para o enfermeiro
        -Paciente:
            1. Adicionar paciente
            2. Remover paciente
            3. Agendar consulta
            4. Atualizar informações do paciente
        -Setor administrativo:
            1. Registrar queixa(se houver)
            2. Faturamento do hospital
            3. Faturamento do paciente

- Funcionalidades pensadas para serem implantadas futuramente:

    1. Relatórios em PDF: Gerar um pdf com as informações do paciente

    2. Sistema de login: paciente e funcionarioSaude            


                   

Funcionalidades:
1 - Cadastro de pacientes

2 - Agendamento, cancelamento e remarcação de consultas

3 - Registro médico (prontuário do paciente)

4 - Prescrição de medicamentos

5 - Solicitação de exames laboratoriais

6 - Gerenciamento de leitos e internações

7 - Controle de estoque de materiais hospitalares

8 - Escalonamento de turnos da equipe

9 - Gerenciamento de casos de emergência (com prioridade)

10 - Faturamento automático por atendimentos


# Sistema de Gestão Hospitalar (POO)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Sistema de gestão hospitalar desenvolvido em Python com foco em Programação Orientada a Objetos (POO). O software permite o gerenciamento completo de pacientes, consultas, exames, leitos, estoque, equipe de saúde e emergências, com a funcionalidade de gerar relatórios em PDF.

## Funcionalidades Implementadas

- [x] **Cadastro de Pacientes:** Registro de novos pacientes com nome, CPF e cartão do SUS.
- [x] **Agendamento de Consultas:** Marcação de consultas com profissionais específicos (Médico, Dentista, etc.), aplicando polimorfismo.
- [x] **Prontuário Médico:** Registro de informações no prontuário do paciente.
- [x] **Solicitação de Exames:** Cada profissional de saúde pode solicitar exames específicos de sua área a partir de uma lista predefinida.
- [x] **Gerenciamento de Leitos:** Alocação de leitos para internação.
- [x] **Controle de Estoque:** Adição e visualização de materiais hospitalares.
- [x] **Escalonamento de Turnos:** Definição de turnos de trabalho para a equipe.
- [x] **Gerenciamento de Emergências:** Registro de casos de emergência com sistema de prioridade.
- [x] **Faturamento:** Cálculo automático de faturas por atendimentos.
- [x] **Geração de Relatórios em PDF:**
    - [x] Relatório individual de pacientes.
    - [x] Relatório completo da equipe de saúde.
    - [x] Relatório geral do hospital (pacientes e equipe).

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
    pip install fpdf2
    ```
    Por enquanto a função de gerar pdf não vai ser implementada por motivos técnicos de erro constante
3.  **Execute o programa:**
    ```bash
    python hospital/main.py
    ```



## Funcionalidades Futuras

- [ ] **Sistema de Login:** Criar perfis de acesso para pacientes e funcionários.
- [ ] **Interface Gráfica (GUI):** Desenvolver uma interface visual para facilitar o uso do sistema.
- [ ] **Banco de Dados:** Substituir o armazenamento em memória por um banco de dados (SQLite, por exemplo) para persistência dos dados.
- [ ] **Testes Unitários:** Implementar testes para garantir a estabilidade do código.
