# "Criador" de funções de potência
import logging

def calculate(x):

    def potencia(num):
        return x ** num

    return potencia


# Potência de 2 e 3
# potencia_2 = cria_potencia(2)
potencia = calculate(3)

# Resultado
# print(potencia_2(2))
print(potencia(3))
