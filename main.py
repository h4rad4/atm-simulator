def atm(valor: int):
    valores = [100, 50, 10, 5, 1]
    qtd = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        while valor >= valores[i]:
            qtd[i] += 1
            valor -= valores[i]

    return qtd


valores = [100, 50, 10, 5, 1]
valor = float(input("Qual o valor de saque? "))
qtd = atm(valor)

for i in range(0, 5):
    if qtd[i] != 0 and qtd[i] > 1:
        print(f"{qtd[i]} notas de {valores[i]}", end=", ")
    elif qtd[i] == 1:
        print(f"1 nota de {valores[i]}", end=", ")

print("\b\b  ")
