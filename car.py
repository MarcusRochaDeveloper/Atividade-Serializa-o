import json


class Carro:
    def __init__(self, posicao_x, posicao_y, velocidade=0.0):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade

    def acelerar(self, valor):
        if valor > 0:
            self.velocidade += valor

    def freiar(self, valor):
        if valor > 0:
            self.velocidade -= valor
            if self.velocidade < 0:
                self.velocidade = 0.0

    def to_dict(self):
        return {
            "posicao_x": self.posicao_x,
            "posicao_y": self.posicao_y,
            "velocidade": self.velocidade
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def salvar(self, caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self.to_dict(), arquivo, indent=4)

    @classmethod
    def carregar(cls, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return cls(
            dados["posicao_x"],
            dados["posicao_y"],
            dados["velocidade"]
        )


def menu():
    print("=== Cadastro do Carro ===")
    x = float(input("Posição X: "))
    y = float(input("Posição Y: "))
    velocidade = float(input("Velocidade inicial: "))

    carro = Carro(x, y, velocidade)

    while True:
        print("\n1 - Acelerar")
        print("2 - Frear")
        print("3 - Finalizar")

        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Quanto deseja acelerar? "))
            carro.acelerar(valor)
            print("Velocidade atual:", carro.velocidade)

        elif opcao == "2":
            valor = float(input("Quanto deseja frear? "))
            carro.freiar(valor)
            print("Velocidade atual:", carro.velocidade)

        elif opcao == "3":
            break

        else:
            print("Opção inválida")

    print("\nJSON gerado:")
    print(carro.to_json())

    carro.salvar("carro.json")

    carro_recuperado = Carro.carregar("carro.json")
    print("\nObjeto desserializado:")
    print(carro_recuperado.posicao_x, carro_recuperado.posicao_y, carro_recuperado.velocidade)


if __name__ == "__main__":
    menu()