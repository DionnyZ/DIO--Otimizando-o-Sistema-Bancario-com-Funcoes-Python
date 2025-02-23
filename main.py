def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def realizar_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, / , *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(nome, data_nasc, cpf, endereco, usuarios):
    if not any(cpf in usuario.values() for usuario in usuarios):
        usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})
        print('Usuário cadastrado com sucesso.')
    else:
        print('O CPF já está cadastrado.')
    
    return usuarios

def cadastrar_conta_bancaria(cpf, usuarios, contas):
    if any(cpf in usuario.values() for usuario in usuarios):
        contas.append({'agencia': '0001','conta': len(contas) + 1, 'usuario': cpf})
        print('Conta criada com sucesso.')

    else:
        print('O CPF não está cadastrado.')

    return contas

menu = """

[c] Cadastrar usuário
[b] Cadastrar conta bancária
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == 'c':
        nome = input("Informe o nome: ")
        data_nasc = input("Informe a data de nascimento: ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
        usuarios = cadastrar_usuario(nome, data_nasc, cpf, endereco, usuarios)
        
    elif opcao == 'b':
        cpf = input("Informe o CPF: ")
        contas = cadastrar_conta_bancaria(cpf, usuarios, contas)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = realizar_deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = realizar_saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")