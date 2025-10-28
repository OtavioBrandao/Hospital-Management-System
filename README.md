
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
- ☑️ **Gerenciamento de Emergências:** Registro de casos de emergência com sistema de prioridade.
- ☑️ **Faturamento:** Cálculo automático de faturas por atendimentos.
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

# Design Patterns implementados

## Padrões criacionais

- **Singleton**: Utilizado para garantir que hospital seja instanciado apenas uma vez e não tenhamos hospitais diferentes, gerando incoerência nos dados. Foi implementado para ser instanciado como uma váriavel global por todo o código, seguindo a estrutura de Singleton com __new__ e etc.

- **Builder**: Utilizado para a criação de pacientes de forma personalizada, onde posso criar um paciente simples ou um mais complexo, preenchendo os dados que eu quero e ainda realizando uma atualização que segue a mesma lógica do builder com reset. Além disso, foi adicionada uma classe diretora que irá coordenar a partir desse builder a construção específica de pacientes. Ele basicamente chama os métodos 'com' para validações básicas E junta eles junto com o 'construir' no final para terminar a construção, como se fosse bloquinho por bloquinho.

- **Factory Method**: Utilizado para a criação de funcionários da saúde para o hospital em si. É uma forma de criar o funcionário de uma forma organizada, recebendo o tipo e chamando a fábrica de acordo com esse tipo, com algumas validações simples.

## Padrões comportamentais

- **Strategy**: Utilizado para gerenciar o faturamento que antes era fixa e de forma avulsa. Basicamente, o mesmo vai criar estratégias diferentes para gerar a fatura do respectivo paciente de acordo com o plano e convênio. A função para calcular o faturamento é implementada de maneiras diferentes para cada estratégia, sendo elas o plano particular, SUS e convênio, onde temos diferentes convênios e diferentes formas de fazer o faturamento. Fundamental para facilitar a implementação de outras faturas caso seja adicionado no futuro.

- **Template Method**: Foi utilizado para organizar a geração de PDFS, visto que antes tinha muita repetição de código. Ao montar um esqueleto que vai ser a estrutura fixa de todo o relatório, ou seja, um método fixo, ele vai obrigar todos os tipos de relatório que herdarem desse Template a ter a mesma estrutura. As únicas mudanças vão ser nos métodos abstratos que vão mudar para cada tipo de relatório, tanto no título do relatório em si como no conteúdo do mesmo. A utilização do template foi interessante pois proporcionou a possibilidade de usar menos linhas de código e deixar tudo mais organizado.

- **Observer**: Foi utilizado para aprimorar o gerenciamento de emergências ao notificar funcionários da saúde diferentes sobre uma eventual emergência, notificando apenas aqueles que estão de plantão escalonados no turno atual do horário local. Esta implementação permitiu uma forma mais organizada de apenas notificar a quem interessa no momento e não necessariamente todo mundo, para que os notificados tenham sua própia reação à situação de emergência.

## Padrões estruturais

- **Adapter**: Utilizado para adaptar interfaces incompatíveis para que elas funcionem para o mesmo método, apenas de formas diferentes, reforçando a abstração A parte que vai chamar o adapter não vai precisar lidar com os serviços externos simulados, muito menos saber como é a implementação interna. Ela apenas vai chamar os adapters e eles vão adaptar tanto para E-mail como para WhatsApp o tipo de notificação gerada. Se caso o serviço externo mudar, não vou precisar mudar a lógica do meu notificador, apenas do meu adapter e ele continuará funcionando igual.

- **Facade**: Utilizado para facilitar para o usuário e quem estiver lendo o código a leitura e entendimento geral do mesmo. Temos uma classe Hospital, que é gigantesca e responsável pela maioria dos procedimentos. O Facade vai esconder a parte verbosa e deixar mais enxuta, facilitando a visualização e entendimento, além de deixar a chamada dos métodos menos verbosa e funcionando igual a classe Hospital em si, sendo apenas algo para embelezar mesmo. A estrutura do mesmo permite que sejam criados outros procedimentos a partir de métodos existentes de forma simplificada também e ainda é possível acessar métodos que não foram declarados explicitamente na fachada a partir de getatrr.

- **Composite**: Utilizado para tratar exames simples e exames compostos da mesma forma, assim sendo possível ter pacotes diferentes de exames com os preços sendo exibidos corretamente, além de permitir que exames compostos tenham outros exames simples e compostos dentro do mesmo, todos sendo tratados da mesma maneira, facilitando o uso e implementação, que no caso do nosso sistema, é para facilitar a solitação de alguns exames que normalmente são feitos em conjunto como um checkup geral.