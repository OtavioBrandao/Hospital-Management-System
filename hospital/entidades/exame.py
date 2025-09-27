class Exame():
    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return self.nome

# Exames que podem ser solicitados
EXAMES_DISPONIVEIS = {
    # Médico
    "hemograma": Exame("Hemograma Completo"),
    "raio-x": Exame("Raio-X de Tórax"),
    "urina": Exame("Exame de Urina"),
    "tomografia":Exame("Tomografia computadorizada"),
    "ecocardiograma": Exame("EcoCardiograma"),
    "eletrocardiograma": Exame("Eletrocardiograma"),
    "ultrassom": Exame("Ultrassonografia"),
    "ressonancia": Exame("Ressonância Magnética"),
    "endoscopia": Exame("Endoscopia Digestiva"),
    "colonoscopia": Exame("Colonoscopia"),
    "biópsia": Exame("Biópsia"),
    "cintilografia": Exame("Cintilografia"),
    "angiografia": Exame("Angiografia"),
    "densitometria": Exame("Densitometria Óssea"),
    "papanicolau": Exame("Papanicolau"),
    "mamografia": Exame("Mamografia"),
    "teste_alergia": Exame("Teste de Alergia"),
    
    # Dentista
    "radiografia_dentaria": Exame("Radiografia Dentária"),
    "limpeza": Exame("Limpeza e Profilaxia"),
    "tomografia":Exame("Tomografia computadorizada"),
    "exame_periodontal": Exame("Exame Periodontal"),
    "exame_caries": Exame("Exame de Cáries"),
    "exame_endodontico": Exame("Exame Endodôntico"),
    "exame_ortodontico": Exame("Exame Ortodôntico"),
    "exame_implante": Exame("Exame de Implante Dentário"),
    "exame_protese": Exame("Exame de Prótese Dentária"),
    "exame_siso": Exame("Exame de Siso"),

    # Enfermeiro
    "glicemia": Exame("Teste de Glicemia Capilar"),
    "pressao": Exame("Aferição de Pressão Arterial"),
    "pulso": Exame("Aferição de Pulso"),
    "temperatura": Exame("Aferição de Temperatura"),
    "saturacao": Exame("Oximetria de Pulso"),
    "monitoramento": Exame("Monitoramento Cardíaco"),
    # Psicólogo (não solicita exames, mas encaminha)
    "encaminhamento": Exame("Encaminhamento para Psiquiatra")

}