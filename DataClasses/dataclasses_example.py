from dataclasses import dataclass, field

@dataclass
class Item:
    nome: str
    tipo: str
    poder: int

@dataclass
class Inventario:
    dono: str
    itens: list[Item] = field(default_factory=list)

    def adicionar_item(self, item: Item):
        self.itens.append(item)

# Criando itens
espada = Item("Espada Flamejante", "Arma", 50)
pocao = Item("Poção de Vida", "Cura", 20)

# Inventário do herói
inventario = Inventario("Aragorn")
inventario.adicionar_item(espada)
inventario.adicionar_item(pocao)


print(inventario)
print(inventario.dono)
print(inventario.itens)