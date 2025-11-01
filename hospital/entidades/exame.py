from abc import ABC, abstractmethod

class Exame():
    def __init__(self,nome,codigo):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return self.nome

# Exames que podem ser solicitados
EXAMES_DISPONIVEIS = {
    # Médico
    "hemograma": Exame("Hemograma Completo", "hemograma"),
    "raio-x": Exame("Raio-X de Tórax", "raio-x"),
    "urina": Exame("Exame de Urina", "urina"),
    "tomografia":Exame("Tomografia computadorizada", "tomografia"),
    "ecocardiograma": Exame("EcoCardiograma", "ecocardiograma"),
    "eletrocardiograma": Exame("Eletrocardiograma", "eletrocardiograma"),
    "ultrassom": Exame("Ultrassonografia", "ultrassom"),
    "ressonancia": Exame("Ressonância Magnética", "ressonancia"),
    "endoscopia": Exame("Endoscopia Digestiva", "endoscopia"),
    "colonoscopia": Exame("Colonoscopia", "colonoscopia"),
    "biópsia": Exame("Biópsia", "biópsia"),
    "cintilografia": Exame("Cintilografia", "cintilografia"),
    "angiografia": Exame("Angiografia", "angiografia"),
    "densitometria": Exame("Densitometria Óssea", "densitometria"),
    "papanicolau": Exame("Papanicolau", "papanicolau"),
    "mamografia": Exame("Mamografia", "mamografia"),
    "teste_alergia": Exame("Teste de Alergia", "teste_alergia"),

    # Dentista
    "radiografia_dentaria": Exame("Radiografia Dentária", "radiografia_dentaria"),
    "limpeza": Exame("Limpeza e Profilaxia", "limpeza"),
    "tomografia":Exame("Tomografia computadorizada", "tomografia"),
    "exame_periodontal": Exame("Exame Periodontal", "exame_periodontal"),
    "exame_caries": Exame("Exame de Cáries", "exame_caries"),
    "exame_endodontico": Exame("Exame Endodôntico", "exame_endodontico"),
    "exame_ortodontico": Exame("Exame Ortodôntico", "exame_ortodontico"),
    "exame_implante": Exame("Exame de Implante Dentário", "exame_implante"),
    "exame_protese": Exame("Exame de Prótese Dentária", "exame_protese"),
    "exame_siso": Exame("Exame de Siso", "exame_siso"),

    # Enfermeiro
    "glicemia": Exame("Teste de Glicemia Capilar", "glicemia"),
    "pressao": Exame("Aferição de Pressão Arterial", "pressao"),
    "pulso": Exame("Aferição de Pulso", "pulso"),
    "temperatura": Exame("Aferição de Temperatura", "temperatura"),
    "saturacao": Exame("Oximetria de Pulso", "saturacao"),
    "monitoramento": Exame("Monitoramento Cardíaco", "monitoramento"),
    # Psicólogo (não solicita exames, mas encaminha)
    "encaminhamento": Exame("Encaminhamento para Psiquiatra", "encaminhamento")

}

# Preços para o Particular
VALORES_EXAMES = {
    # Médico
    "hemograma": 40,
    "raio-x": 80,
    "urina": 30,
    "tomografia": 200,
    "ecocardiograma": 120,
    "eletrocardiograma": 90,
    "ultrassom": 100,
    "ressonancia": 350,
    "endoscopia": 150,
    "colonoscopia": 300,
    "biópsia": 250,
    "cintilografia": 400,
    "angiografia": 500,
    "densitometria": 120,
    "papanicolau": 60,
    "mamografia": 180,
    "teste_alergia": 150,

    # Dentista
    "radiografia_dentaria": 60,
    "limpeza": 120,
    "exame_periodontal": 100,
    "exame_caries": 70,
    "exame_endodontico": 250,
    "exame_ortodontico": 150,
    "exame_implante": 300,
    "exame_protese": 150,
    "exame_siso": 120,

    # Enfermeiro
    "glicemia": 20,
    "pressao": 15,
    "pulso": 15,
    "temperatura": 10,
    "saturacao": 20,
    "monitoramento": 100,

    # Psicólogo (encaminhamento)
    "encaminhamento": 10
}

# Composite para exames 
class ComponenteExame(ABC):

    @abstractmethod
    def executar(self, profissional, paciente):
        pass

    @abstractmethod
    def obter_custo(self):
        pass

    @abstractmethod
    def listar_exames(self):
        pass

class ExameSimples(ComponenteExame):
    def __init__(self, codigo):
        if codigo not in EXAMES_DISPONIVEIS:
            raise KeyError(f"Código de exame '{codigo}' não encontrado")
        self.codigo = codigo
        self.exame = EXAMES_DISPONIVEIS[codigo]
        self.custo = VALORES_EXAMES[codigo]

    def executar(self, profissional, paciente):
        profissional.requisitarExame(paciente, self.codigo, False)

    def obter_custo(self):
        return self.custo
    
    def listar_exames(self):
        return [self.exame.nome]
        
# Vários exames simples
class ExameComposto(ComponenteExame):
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.exames = []

    def adicionar_exame(self, exame: ComponenteExame):
        self.exames.append(exame)
        return self

    def executar(self, profissional, paciente):
        print(f"\n🔬 Solicitando pacote: {self.nome}")
        for exame in self.exames:
            exame.executar(profissional, paciente)

    def obter_custo(self):
        return sum(exame.obter_custo() for exame in self.exames)
    
    def listar_exames(self):
        nomes = []
        for exame in self.exames:
            nomes.extend(exame.listar_exames())
        return nomes
    
def criar_catalogo_pacotes():
    catalogo = {}
    # Check-up Básico
    checkup_basico = ExameComposto("Checkup Básico", "Exames de rotina")
    checkup_basico.adicionar_exame(ExameSimples("hemograma"))
    checkup_basico.adicionar_exame(ExameSimples("urina"))
    checkup_basico.adicionar_exame(ExameSimples("glicemia"))
    catalogo["checkup_basico"] = checkup_basico
    
    # Avaliação Cardíaca
    cardio = ExameComposto("Avaliação Cardíaca Completa", "Exames para avaliação do coração")
    cardio.adicionar_exame(ExameSimples("ecocardiograma"))
    cardio.adicionar_exame(ExameSimples("eletrocardiograma"))
    cardio.adicionar_exame(ExameSimples("hemograma"))
    catalogo["avaliacao_cardiaca"] = cardio
    
    # Pré-Operatório
    pre_op = ExameComposto("Pré-Operatório", "Exames necessários antes de cirurgias")
    pre_op.adicionar_exame(ExameSimples("hemograma"))
    pre_op.adicionar_exame(ExameSimples("raio-x"))
    pre_op.adicionar_exame(ExameSimples("eletrocardiograma"))
    pre_op.adicionar_exame(ExameSimples("urina"))
    catalogo["pre_operatorio"] = pre_op
    
    # Saúde da Mulher
    mulher = ExameComposto("Checkup Feminino", "Exames para a saúde da mulher")
    mulher.adicionar_exame(ExameSimples("papanicolau"))
    mulher.adicionar_exame(ExameSimples("mamografia"))
    mulher.adicionar_exame(ExameSimples("ultrassom"))
    catalogo["checkup_feminino"] = mulher

    # Saúde Bucal
    bucal = ExameComposto("Avaliação Odontológica Completa", "Exames para a saúde bucal")
    bucal.adicionar_exame(ExameSimples("radiografia_dentaria"))
    bucal.adicionar_exame(ExameSimples("exame_periodontal"))
    bucal.adicionar_exame(ExameSimples("limpeza"))
    catalogo["avaliacao_odonto"] = bucal

    # Composição da composição
    super_checkup = ExameComposto("Super Checkup", "Completo")
    super_checkup.adicionar_exame(checkup_basico)  
    super_checkup.adicionar_exame(ExameSimples("raio-x")) 
    super_checkup.adicionar_exame(ExameSimples("tomografia"))
    catalogo["super_checkup"] = super_checkup
        
    return catalogo

PACOTES_EXAMES = criar_catalogo_pacotes()