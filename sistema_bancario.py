#programa de sistema bancário para testes e estudo.

usuarios = [
    {"nome": "cleilson", "cpf": "123123", "senha": "123456", "saldo": 0 },
]
          

numero_saque = 0
LIMITE_SAQUE = 3

menu_1 = """

L. login
C. cadastro

"""

menu_2 = """
>>>>- menu -<<<<

S. saque
E. extrato
D. depósito
Q. sair

>>>>>>><<<<<<<
"""



def cadastro():
    while True:
        cad_nome = input("primeiro nome: ")
        cad_cpf = input("seu cpf: ")
        cad_senha = input("escolha uma senha: ")

        cpf_existe = None

        for usuario in usuarios:
            if cad_cpf == usuario["cpf"]:
                cpf_existe = True
            else:
                cpf_existe = False

        if cpf_existe == True:
            print(f"cpf {cad_cpf} já em uso")

        else:
            novo_usuario = {"nome": cad_nome, "cpf": cad_cpf, "senha": cad_senha}
            usuarios.append(novo_usuario)
            print(f"usuario {cad_nome} cadastrado com sucesso!")
            break


def login():
    while True:
        login_usuario = input("digite seu nome: ")
        login_cpf = input("digite seu cpf: ")
        login_senha = input("digite sua senha: ")

        login_existe = None

        for usuario in usuarios:
            if login_usuario == usuario["nome"] and login_cpf == usuario["cpf"] and login_senha == usuario["senha"]:
                login_existe = True
            else:
                login_existe = False
        
        if login_existe == True:
            print(f"Olá, {login_usuario}!")
            break
        else:
            print(f"erro. {login_usuario} não encontrado")


def deposito():
    while True:
        valor = float(input("qual o valor? "))
        for usuario in usuarios:
            if valor > 0:
                usuario["saldo"] += valor
                print(f"extrato: deposito de R${valor} e saldo R${usuario['saldo']} ")
                break
            else:
                print("operação falhou")



def saque():
    while True:
        valor = float(input("qual o valor? "))
        excedeu_saldo = valor > usuario["saldo"]
        excedeu_limite = numero_saque > LIMITE_SAQUE
        if excedeu_saldo:
                print("saldo insuficiente")
                break
            
        elif excedeu_limite:
            print("ultrapassou limite para saques diarios")
            break
        
        elif valor <= usuario["saldo"]:
            saldo -= usuario["valor"]
            numero_saque += 1 
            print("saque realizado com sucesso")
            print(f"extrato: seu saque R${valor} e saldo R${usuario['saldo']} ")
            break
        else:
            print("erro")
            break

while True:
    for usuario in usuarios:
        operacao = input(menu_1)
        if operacao == "c":
            cadastro()
        
        elif operacao == "l":
            login()
        while True:
            operacao_02 = input(menu_2)
            if operacao_02 == "d":
                deposito()
            elif operacao_02 == "s":
                saque()
    
            elif operacao_02 == "e":
                print(f"""
                    -------------------------
                    | extrato: saldo R${usuario['saldo']} |
                    -------------------------
                    """)

            elif operacao_02 == "q":
                break

            else:
                print("digite uma operação válida")
        else:
            print("houve um erro inesperado")       
            