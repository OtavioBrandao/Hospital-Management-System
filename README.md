
# Sistema de Gestão Hospitalar (POO REFATORADO)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Sistema de gestão hospitalar desenvolvido em Python com foco em Programação Orientada a Objetos (POO). O software permite o gerenciamento completo de pacientes, consultas, exames, leitos, estoque, equipe de saúde e emergências, com a funcionalidade de gerar relatórios em PDF.

## Funcionalidades Implementadas (☑️ Para os refatorados)

- ☑️ **Cadastro de Pacientes:** Registro de novos pacientes com nome, CPF e cartão do SUS. (Possibilidade de fazer um cadastro completo)
- ☑️ **Agendamento de Consultas:** Marcação de consultas com profissionais específicos (Médico, Dentista, etc.), aplicando polimorfismo. (Adicionado a possibilidade de remarcar e cancelar consultas).
- ✅ **Prontuário Médico:** Registro de informações no prontuário do paciente.
- ✅ **Solicitação de Exames:** Cada profissional de saúde pode solicitar exames específicos de sua área a partir de uma lista predefinida.
- ✅ **Gerenciamento de Leitos:** Alocação de leitos para internação.
- ✅ **Controle de Estoque:** Adição e visualização de materiais hospitalares.
- ✅ **Escalonamento de Turnos:** Definição de turnos de trabalho para a equipe.
- ✅ **Gerenciamento de Emergências:** Registro de casos de emergência com sistema de prioridade.
- ✅ **Faturamento:** Cálculo automático de faturas por atendimentos.
- ☑️ **Prescrição de receitas**: Funcionalidade implementada que não tinha antes.
- ☑️ **Geração de Relatórios em PDF:**
    - ☑️ Relatório individual de pacientes.
    - ☑️ Relatório completo da equipe de saúde.
    - ☑️ Relatório geral do hospital (pacientes e equipe).

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

## Design Patterns utilizados
- **Singleton**: Utilizado para garantir que hospital seja instanciado apenas uma vez e não tenhamos hospitais diferentes, gerando incoerência nos dados. Foi implementado para ser instanciado como uma váriavel global por todo o código, seguindo a estrutura de Singleton com __new__ e etc.
- **Builder**: Utilizado para a criação de pacientes de forma personalizada, onde posso criar um paciente simples ou um mais complexo, preenchendo os dados que eu quero e ainda realizando uma atualização que segue a mesma lógica do builder com reset. Além disso, foi adicionada uma classe diretora que irá coordenar a partir desse builder a construção específica de pacientes. Ele basicamente chama os métodos 'com' para validações básicas E junta eles junto com o 'construir' no final para terminar a construção, como se fosse bloquinho por bloquinho.
- **Factory Method**: Utilizado para a criação de funcionários da saúde para o hospital em si. É uma forma de criar o funcionário de uma forma organizada, recebendo o tipo e chamando a fábrica de acordo com esse tipo, com algumas validações simples.


## Funcionalidades Futuras

- [ ] **Sistema de Login:** Criar perfis de acesso para pacientes e funcionários.
- [ ] **Interface Gráfica (GUI):** Desenvolver uma interface visual para facilitar o uso do sistema.
- [ ] **Banco de Dados:** Substituir o armazenamento em memória por um banco de dados (SQLite, por exemplo) para persistência dos dados.
- [ ] **Testes Unitários:** Implementar testes para garantir a estabilidade do código.
