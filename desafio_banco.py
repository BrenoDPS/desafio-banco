# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
# devemos implementar apenas 3 operações: depósito, saque e extrato
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, 
# dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
# Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 = R$ 1500.45


menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor desejado para depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação inválida, digite outro valor.")

    elif opcao == "s":
        valor = float(input("Informe o valor desejado para sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida devido a falta de saldo na conta para realizar essa tarefa.")

        elif excedeu_limite:
            print("Operação inválida devido ao valor desejado para saque ser maior do que o limite acordado de R$500.")

        elif excedeu_saques:
            print("Operação inválida devido ao fato de que o número de saques é maior do que o acordado de 3 saques máximos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida, digite outro valor.")

    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")