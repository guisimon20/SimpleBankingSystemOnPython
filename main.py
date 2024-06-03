import datetime

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3
contador_extrato = 0
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")

print("=" * 30)
print("SISTEMA BANCÁRIO".center(30))
print(f"Data: {data_formatada}".center(30))
print("=" * 30)

while True:
  menu = f"""
  Saldo Atual: R${saldo}

  O que deseja fazer?
  [D] Depósito
  [S] Saque
  [E] Extrato
  [Q] Sair

  =>"""
  opcao = input(menu)
  
  if opcao.lower() == "d":
    print("Depósito".center(30, "-"))
    deposito = int(input("Quanto deseja depositar? "))
    saldo += deposito
    contador_extrato += 1
    extrato += f"{contador_extrato} - Depósito de R${deposito} \n"
    print(f"Seu depósito de R${deposito} foi concluído")
  elif opcao.lower() == "s":
    print("Saque".center(30, "-"))
    saque = int(input("Quanto deseja sacar? "))
    if saque <= limite and numero_saques < LIMITES_SAQUES:
      numero_saques += 1
      saldo -= saque
      contador_extrato += 1
      extrato += f"{contador_extrato} - Saque de R${saque} \n"
      print(f"Seu saque de R${saque} foi concluído")
    elif saque <= limite and numero_saques >= LIMITES_SAQUES:
      print("Foi excedido o número de saques diário!")
    elif saque > limite and numero_saques < LIMITES_SAQUES:
      print("Seu limite de saque foi excedido!")
    else:
      print("Seu limite de saque e número de saques diário foram excedidos!")
  elif opcao.lower() == "e":
    print("Extrato".center(30, "-"))
    print(extrato)
    print(f"Saldo: R${saldo}")
  elif opcao.lower() == "q":
    break
  else:
    print("Erro! Opção Inexistente, Tente Novamente!")
print("Programa Finalizado, Muito Obrigado!")

