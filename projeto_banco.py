saldo = 700.0
saques_diarios = 0
historico_saques = []
historico_deposito = []
limite_saque = 500.0

while saques_diarios <3:

        opcao = int(input("Selecione uma opção: \n [1] Sacar \n [2] Depositar \n [3] Visualizar Extrato \n opção:"))
        if opcao == 1:
            saque = float(input("Selecione um valor para saque:"))
            if saque <= 0:
                print ("saque não permitido, valor invalido")
            elif saque > limite_saque:
                  print("Saque não realizado, limite de saque é de: R$", limite_saque)
            elif saldo >= saque:
                saldo -= saque
                saques_diarios += 1
                historico_saques.append(saque)
                print (f"saque no valor de R${saque} realziado com sucesso, saldo atual é de R${saldo}")              
            elif saque > saldo:
                print ("saldo insuficiente")
            else:
                print("operação invalida")          
        elif opcao == 2:
            deposito = float(input("selecione um valor para deposito: \n valor:"))
            if deposito > 0:
                    saldo += deposito
                    historico_deposito.append(deposito)
                    print (f"você depositou o valor de R${deposito}, seu saldo atual é de R${saldo}")
            else:
                    print ("Deposito não realizado")        
        elif opcao == 3:
                print ("exibindo extrato".upper())
                print ("exibindo histórico de depositos:")
                for deposito in historico_deposito:
                      print(f"deposito de R${deposito}")
                print ("exibindo histórico de saques:")
                for saque in historico_saques:
                      print (f"saque de {saque}")
                print (f"saldo atual é de R$".upper(),saldo)
                if not historico_deposito and not historico_saques:
                      print ("não foram feitas movimentações")
        else:
              print ("Operação invalida, tente novamente")
              

print ("limite de saques atigido, você relizou três saques hoje.".upper())