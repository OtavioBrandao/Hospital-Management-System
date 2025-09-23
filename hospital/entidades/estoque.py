class Estoque:
    def __init__(self):
        self.itens = {
            "máscaras": 100,
            "luvas": 200,
            "álcool em gel": 150,
            "medicamentos": 300  
        }

    def adicionar_item(self, item, quantidade):
        self.itens[item] = self.itens.get(item, 0) + quantidade

    def mostrar_estoque(self):
        if not self.itens:
            print("Estoque vazio.")
        else:
            for item, qtd in self.itens.items():
                print(f"{item}: {qtd} unidades")
