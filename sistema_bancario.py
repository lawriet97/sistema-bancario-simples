saldo = 0
numero_saque = 0
LIMITE_SAQUE = 3
menu = """
>>>>>menu<<<<<
S. saque
E. extrato
D. depósito
Q. sair
"""

while True:
    operacao = input(menu)

    if operacao == "d":
        valor = float(input("qual o valor? "))
        
        if valor > 0:
            saldo += valor
            print(f"extrato: deposito de {valor} e saldo {saldo} ")
        
        else:
            print("operação falhou")
    
    elif operacao == "s":
        valor = float(input("qual o valor? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = numero_saque > LIMITE_SAQUE
        
        if excedeu_saldo:
            print("saldo insuficiente")
        
        elif excedeu_limite:
            print("ultrapassou limite para saques diarios")
        
        elif valor <= saldo:
            saldo -= valor
            numero_saque += 1 
            print("saque realizado com sucesso")
            print(f"extrato: seu saque R${valor} e saldo {saldo} ")
    
    elif operacao == "e":
        print(f"extrato: saldo R${saldo}")

    elif operacao == "q":
        break

    else:
        print("digite uma operação válida")