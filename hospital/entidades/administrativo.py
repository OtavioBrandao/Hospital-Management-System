class SetorAdministrativo:
    def __init__(self):
        self.queixas = []

    def registrar_queixa(self, funcionario, descricao):
        self.queixas.append((funcionario, descricao))

    def exibir_queixas(self):
        if not self.queixas:
            print("Nenhuma queixa registrada.")
        for f, d in self.queixas:
            print(f"Funcionário: {f} - Queixa: {d}")
