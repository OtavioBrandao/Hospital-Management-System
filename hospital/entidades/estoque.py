class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, quantidade):
        self.itens[item] = self.itens.get(item, 0) + quantidade

    def mostrar_estoque(self):
        if not self.itens:
            print("Estoque vazio.")
        else:
            for item, qtd in self.itens.items():
                print(f"{item}: {qtd} unidades")
