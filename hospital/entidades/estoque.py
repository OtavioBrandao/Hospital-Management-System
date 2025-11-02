from entidades.exceptions import EstoqueMaximoException

class Estoque:
    def __init__(self):
        self.itens = {
            "máscaras": 100,
            "luvas": 200,
            "álcool em gel": 150,
            "medicamentos": 300  
        }

    def adicionar_item(self, item, quantidade):
        try:
            item_normalizado = item.lower().strip()
            soma = self.itens.get(item_normalizado, 0) + quantidade
            if soma > 1000:
                raise EstoqueMaximoException(item_normalizado)
            self.itens[item_normalizado] = soma
        except EstoqueMaximoException as e:
            print(f"{e}")

    def mostrar_estoque(self):
        if not self.itens:
            print("Estoque vazio.")
        else:
            for item, qtd in self.itens.items():
                print(f"{item}: {qtd} unidades")
