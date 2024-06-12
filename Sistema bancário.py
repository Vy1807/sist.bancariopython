#Variáveis
saldo = 0
voltar = False
direcao = "t"
e_deposito = None
e_saque = None
limite = 0

#Função hub 
hub = """
                            Bem vindo ao Sistema Bancário de Vyctor Trindade
        Para prosseguir, selecione o tipo de operação desejada e daremos continuidade a seu serviço!

    [e] Extrato
    [d] Depósito
    [s] Saque
    [f] Finalizar
"""
#Função repetição
while direcao != "f":

    print(hub)
    direcao = input("Digite aqui sua escolha.")
    

        #Função depósito
    if direcao == "d":
            deposito = float(input("Digite o valor que deseja depositar em conta."))
            if deposito < 0 :
                  print("Não é possível depositar valores negativos.")
            else: 
                saldo += deposito
                print(f"Após o depósito, seu saldo é R$ {saldo}")
        
        #Função saque
    elif direcao == "s":
            saque = float(input("Quanto deseja sacar?"))
            if saque > saldo:
                print("Saldo insuficiente na conta.")
            else :
                limite+1
                if limite <3:
                    saldo -= saque
                    print(f"Após o saque, seu saldo é R$ {saldo}")
                else:
                      print("Limite de saques diários atingidos.")

        #Função extrato
    elif direcao == "e":
            print(f"""
        ****Operação de saque total- R${saque}****

        ****Operação de depósito total - R${deposito}****

        ****Por fim, seu saldo é R${saldo}****
        """)
print("Obrigado por testar nosso sistema bancário!")

