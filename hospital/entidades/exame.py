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
    # "tomografia": 200,  # mesma chave já definida acima
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
