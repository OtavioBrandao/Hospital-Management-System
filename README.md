
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

- **Singleton**: Utilizado para garantir que hospital seja instanciado apenas uma vez e não tenhamos hospitais diferentes, gerando incoerência nos dados. Foi implementado para ser instanciado como uma váriavel global por todo o código, seguindo a estrutura de Singleton com __new__ e etc. Está sendo utilizado em hospital.py.

- **Builder**: Utilizado para a criação de pacientes de forma personalizada, onde posso criar um paciente simples ou um mais complexo, preenchendo os dados que eu quero e ainda realizando uma atualização que segue a mesma lógica do builder com reset. Além disso, foi adicionada uma classe diretora que irá coordenar a partir desse builder a construção específica de pacientes. Ele basicamente chama os métodos 'com' para validações básicas E junta eles junto com o 'construir' no final para terminar a construção, como se fosse bloquinho por bloquinho. Está sendo definido em paciente.py e utilizado em funcoesAuxiliares.py em conjunto com o seu diretor.

- **Factory Method**: Utilizado para a criação de funcionários da saúde para o hospital em si. É uma forma de criar o funcionário de uma forma organizada, recebendo o tipo e chamando a fábrica de acordo com esse tipo, com algumas validações simples. Utilizado em funcionrios.py.

## Padrões comportamentais

- **Strategy**: Utilizado para gerenciar o faturamento que antes era fixa e de forma avulsa. Basicamente, o mesmo vai criar estratégias diferentes para gerar a fatura do respectivo paciente de acordo com o plano e convênio. A função para calcular o faturamento é implementada de maneiras diferentes para cada estratégia, sendo elas o plano particular, SUS e convênio, onde temos diferentes convênios e diferentes formas de fazer o faturamento. Fundamental para facilitar a implementação de outras faturas caso seja adicionado no futuro. Utilizado em faturamento.py.

- **Template Method**: Foi utilizado para organizar a geração de PDFS, visto que antes tinha muita repetição de código. Ao montar um esqueleto que vai ser a estrutura fixa de todo o relatório, ou seja, um método fixo, ele vai obrigar todos os tipos de relatório que herdarem desse Template a ter a mesma estrutura. As únicas mudanças vão ser nos métodos abstratos que vão mudar para cada tipo de relatório, tanto no título do relatório em si como no conteúdo do mesmo. A utilização do template foi interessante pois proporcionou a possibilidade de usar menos linhas de código e deixar tudo mais organizado. Utilizado em gerarPdf.py

- **Observer**: Foi utilizado para aprimorar o gerenciamento de emergências ao notificar funcionários da saúde diferentes sobre uma eventual emergência, notificando apenas aqueles que estão de plantão escalonados no turno atual do horário local. Esta implementação permitiu uma forma mais organizada de apenas notificar a quem interessa no momento e não necessariamente todo mundo, para que os notificados tenham sua própia reação à situação de emergência. Utilizado em emergencia.py.

## Padrões estruturais

- **Adapter**: Utilizado para adaptar interfaces incompatíveis para que elas funcionem para o mesmo método, apenas de formas diferentes, reforçando a abstração A parte que vai chamar o adapter não vai precisar lidar com os serviços externos simulados, muito menos saber como é a implementação interna. Ela apenas vai chamar os adapters e eles vão adaptar tanto para E-mail como para WhatsApp o tipo de notificação gerada. Se caso o serviço externo mudar, não vou precisar mudar a lógica do meu notificador, apenas do meu adapter e ele continuará funcionando igual. Utilizado em emergencia.py.

- **Facade**: Utilizado para facilitar para o usuário e quem estiver lendo o código a leitura e entendimento geral do mesmo. Temos uma classe Hospital, que é gigantesca e responsável pela maioria dos procedimentos. O Facade vai esconder a parte verbosa e deixar mais enxuta, facilitando a visualização e entendimento, além de deixar a chamada dos métodos menos verbosa e funcionando igual a classe Hospital em si, sendo apenas algo para embelezar mesmo. A estrutura do mesmo permite que sejam criados outros procedimentos a partir de métodos existentes de forma simplificada também e ainda é possível acessar métodos que não foram declarados explicitamente na fachada a partir de getatrr. Utilizado em hospital_facade.py.

- **Composite**: Utilizado para tratar exames simples e exames compostos da mesma forma, assim sendo possível ter pacotes diferentes de exames com os preços sendo exibidos corretamente, além de permitir que exames compostos tenham outros exames simples e compostos dentro do mesmo, todos sendo tratados da mesma maneira, facilitando o uso e implementação, que no caso do nosso sistema, é para facilitar a solitação de alguns exames que normalmente são feitos em conjunto como um checkup geral. Utilizado em exames.py.

### Tratamento de Exceções
- Foram criadas diversas exceções personalizadas para tratar erros específicos do domínio hospitalar, como `PacienteNaoEncontradoException`, `LeitoIndisponivelException` e `ConsultaInvalidaException`. O objetivo disso era melhorar a clareza do código e facilitar a depuração de problemas. 
- As exceções personalizadas foram definidas no arquivo exceptions.py, onde a maioria delas foi utilizada para fins de possíveis erros no sistema. As exceções foram usadas de duas diferentes formas:
    -**Validação de dados**: Ao identifiar um dado inválido ou não encontrado, uitlizei raise para subir o erro de acordo com minha exceção específica durante um try e depois terminando o aviso chamando em except.
    -**Fluxo de controle**: Em alguns casos, utilizei exceções para controlar o fluxo do programa, como interromper uma operação quando uma condição específica não é atendida.
    
# Principais exceções utilizadas:

## Exceções Base
- `SistemaHospitalarException`: Exceção base para todo o sistema hospitalar

## Exceções de Paciente (PacienteException)
- `PacienteNaoEncontradoException`: Lançada quando uma operação tenta acessar um paciente que não existe no sistema
- `PacienteDuplicadoException`: Lançada quando há tentativa de cadastrar um paciente que já existe (CPF ou ID temporário duplicado)
- `DadosInvalidosException`: Lançada quando dados do paciente são inválidos durante o **cadastro** (idade, altura, peso, telefone, etc.)
- `DadosInvalidosAtualizacaoException`: Lançada quando dados do paciente são inválidos durante a **atualização** (mantém valor anterior)
- `CampoObrigatorioException`: Lançada quando um campo obrigatório não foi preenchido (nome, item de estoque, etc.)
- `DocumentoInvalidoException`: Lançada quando CPF ou Cartão SUS é inválido (planejada para uso futuro)
- `CaracteresInvalidosException`: Lançada quando nome contém apenas números ou caracteres especiais inválidos

## Exceções de Funcionário (FuncionarioException)
- `ProfissionalNaoEncontradoException`: Lançada quando uma operação tenta acessar um funcionário que não existe no sistema
- `RegistroInvalidoException`: Lançada quando o registro profissional é inválido ou não segue o padrão esperado (CRM, COREN, CRO, etc.)
- `ContatoInvalidoException`: Lançada quando email ou WhatsApp fornecidos estão em formato inválido
- `PermissaoNegadaException`: Lançada quando funcionário não tem permissão para realizar determinada ação (planejada para uso futuro)
- `FuncionarioDuplicadoException`: Lançada quando há tentativa de cadastrar funcionário com registro profissional já existente

## Exceções de Hospital (HospitalException)
- `LeitoIndisponivelException`: Lançada quando não há leitos disponíveis para alocação (limite de 50 leitos)
- `EstoqueInvalidoException`: Lançada quando quantidade de estoque é negativa, zero ou o item é inválido
- `EstoqueMaximoException`: Lançada quando há tentativa de 

## Tratamento de Exceções Nativas do Python

Além das exceções personalizadas, o sistema utiliza exceções nativas do Python:

- **`ValueError`**: Utilizada em conjunto com exceções customizadas para conversão de tipos e validação de valores
- **`KeyError`**: Tratamento de acessos a dicionários (exames, pacotes de exames)
- **`IndexError`**: Validação de índices em listas (consultas, exames)
- **`TypeError`**: Validação de tipos de dados em operações críticas
- **`OSError` / `IOError`**: Tratamento de erros na geração de PDFs
