class EmergenciaManager:
    def __init__(self):
        self.emergencias = []

    def registrar_emergencia(self, nome, prioridade):
        self.emergencias.append((nome, prioridade))

    def ver_emergencias(self):
        if not self.emergencias:
            print("Nenhuma emergência.")
            return
        prioridades = {"alta": 1, "media": 2, "baixa": 3}
        ordenadas = sorted(self.emergencias, key=lambda x: prioridades.get(x[1], 4)) #o 4 aqui serve para caso seja colocado uma prioridade desconhecida ele coloca em ultimo lugar
        for nome, prioridade in ordenadas:
            print(f"{nome} - prioridade: {prioridade}")
