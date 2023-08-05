def atm(valor: int):
    valores = [100, 50, 10, 5, 1]
    qtd = []
    for v in valores:
        notas = valor // v
        valor %= v
        qtd.append(notas)

    return qtd

valores = [100, 50, 10, 5, 1]
valor = int(input("Qual o valor de saque? "))
qtd = atm(valor)

print("Notas entregues:")
for i in range(0, 5):
    if qtd[i] != 0 and qtd[i] > 1:
        print(f"{qtd[i]} notas de {valores[i]}", end=", ")
    elif qtd[i] == 1:
        print(f"1 nota de {valores[i]}", end=", ")
