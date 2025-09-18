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
    # Dentista
    "radiografia_dentaria": Exame("Radiografia Dentária"),
    "limpeza": Exame("Limpeza e Profilaxia"),
    "tomografia":Exame("Tomografia computadorizada"),
    # Enfermeiro
    "glicemia": Exame("Teste de Glicemia Capilar"),
    "pressao": Exame("Aferição de Pressão Arterial"),
    # Psicólogo (não solicita exames, mas encaminha)
    "encaminhamento": Exame("Encaminhamento para Psiquiatra")
}