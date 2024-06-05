import datetime
from time import sleep

banco_cadastros = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3
contador_extrato = 0
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")
total_sacado = 0
numero_conta_global = 0


# Função Login
def aba_login():
  while True:
    global banco_cadastros
    cpf = input("Digite seu CPF: ")
    numero_conta = int(input("Digite o n° de sua conta: "))
    senha = input("Digite sua senha: ")
    if verificar_login(banco_cadastros, cpf, senha, numero_conta):
      print("Seja Bem-Vindo!")
      conta(extrato = extrato, 
           contador_extrato = contador_extrato, 
           numero_saques = numero_saques,
           total_sacado = total_sacado,
           limite = limite,
           numero_conta = numero_conta)
    else: 
      opcao = input("Erro! Tentar novamente? [S/N] ")
      if opcao.lower() == "n":
        login_e_cadastro()
      elif opcao.lower() == "s":
        print()
      else:
        print("Digite um valor válido!")
    
# Função Cadastro
def aba_cadastro():
  global numero_conta_global
  while True:
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite uma senha: ")
    saldo = 0
    if (nome.isalpha()) and cpf.isnumeric() and len(cpf) == 11 and len(data_de_nascimento) == 10:
      numero_conta_global += 1
      lista = [nome, data_de_nascimento, cpf, senha, numero_conta_global, saldo]
      print(f"""Dados de sua conta:
            Nome: {nome.capitalize()}
            Data de nascimento: {data_de_nascimento}
            CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}
            Senha: {senha}
            N° da conta: {numero_conta_global}
            """)
      return lista
    else:
      opcao = input("Erro! Tentar novamente? [S/N] ")
      if opcao.lower() == "n":
        login_e_cadastro()
      elif opcao.lower() == "s":
        print()

def aba_conta(numero_conta):
  global banco_cadastros
  nome = banco_cadastros[numero_conta-1][0]
  data_de_nascimento = banco_cadastros[numero_conta-1][1]
  cpf = banco_cadastros[numero_conta-1][2]
  senha = banco_cadastros[numero_conta-1][3]
  
  print(f"""
      Dados de sua conta:
      Nome: {nome.capitalize()}
      Data de nascimento: {data_de_nascimento}
      CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}
      Senha: {senha}
      N° da conta: {numero_conta}
  """)
  
# Verificação de cpf
def verificar_cpf(banco_cadastros, cpf):
  return any(cpf in sublista for sublista in banco_cadastros)

# Verificação de cpf e senha
def verificar_login(banco_cadastros, cpf, senha, numero_conta):
  return any(cpf in sublista and senha in sublista and numero_conta in sublista for sublista in banco_cadastros)
  
# Função Depósito
def aba_depositos(saldo, extrato, contador_extrato):
  print("Depósito".center(30, "-"))
  deposito = input("Quanto deseja depositar?")
  if deposito.isnumeric() and int(deposito) > 0:
    deposito = int(deposito)
    saldo += deposito
    contador_extrato += 1
    extrato += f"{contador_extrato} - Depósito de R${deposito} \n"
    print(f"Seu depósito de R${deposito} foi concluído")
    return saldo, extrato
  else:
    print("O valor digitado não é válido!")
    print("Redirecionando para o menu...")
    sleep(1)

# Função Saque
def aba_saques(saldo, extrato, numero_saques,
               contador_extrato, total_sacado):

  print("Saque".center(30, "-"))
  saque = input("Quanto deseja sacar? ")
  if saque.isnumeric() and int(saque) > 0:
    saque = int(saque)
    if saque <= limite and numero_saques < LIMITES_SAQUES and saque <= saldo:
      numero_saques += 1
      saldo -= saque
      contador_extrato += 1
      total_sacado += saque
      extrato += f"{contador_extrato} - Saque de R${saque} \n"
      print(f"Seu saque de R${saque} foi concluído")
      return numero_saques,saldo,extrato,total_sacado
    elif saque <= limite and numero_saques >= LIMITES_SAQUES:
      print("Foi excedido o número de 3 saques diário!")
    elif saque > limite and numero_saques < LIMITES_SAQUES:
      print("Seu limite de saque foi excedido!")
    else:
      print("Sem saldo suficiente para concluir operação!")
  else:
    print("O valor digitado não é válido!")
    print("Redirecionando para o menu...")
    sleep(1)

# Função Limite
def aba_limites(limite, total_sacado, numero_saques,):
  global LIMITES_SAQUES
  print("Limites".center(30, "-"))
  print(f"Você usou R${total_sacado}/{limite}")
  print(f"Você sacou {numero_saques}/{LIMITES_SAQUES} vezes")
  esc = input("Deseja alterar o limite de saque? [S/N] ")
  if esc.lower() == "s":
    limite = input("Qual será seu novo limite?")
    return limite
  elif esc.lower() == "n":
    print("Redirecionando para o menu...")
    sleep(1)
  else:
    print("Erro! Opção Inválida.")
    sleep(1)
    print("Redirecionando para o menu...")
    sleep(1)

# Função Extrato
def aba_extrato(saldo, extrato):
  print("Extrato".center(30, "-"))
  print(extrato)
  print(f"Saldo: R${saldo}")

# Função Login e Cadastro
def login_e_cadastro():
  global banco_cadastros
  while True:
    login = """
    Entre na sua conta!
    [L] Fazer Login
    [C] Cadastrar uma nova conta
    [Q] Finalizar
    =>"""
    opcaologin = input(login)
  
    if opcaologin.lower() == "l":
      aba_login()
      break
    elif opcaologin.lower() == "c":
      lista = aba_cadastro()
      if aba_cadastro is not None:
        cpf = lista[2]
        if verificar_cpf(banco_cadastros, cpf):
          print(f"CPF {cpf} já cadastrado!")
        else:
          print("Usuário cadastrado com sucesso!")
          banco_cadastros.append(lista)
      
    elif opcaologin.lower() == "q":
      print("Finalizando Execução...")
      sleep(1)
      print("Programa Finalizado!")
      exit()
    else:
      print("Erro! Opção Inválida.")

def conta(extrato, contador_extrato, numero_saques, total_sacado, limite, numero_conta):
  global banco_cadastros
  while True:
    saldo = banco_cadastros[numero_conta-1][5]
    menu = f"""
    Saldo Atual: R${saldo}

    O que deseja fazer?
    [D] Depósito
    [S] Saque
    [E] Extrato
    [L] Limites
    [C] Conta
    [Q] Sair
    =>"""
    opcao = input(menu)

    if opcao.lower() == "d":
      deposito_concluido = aba_depositos(saldo,extrato,contador_extrato)
      if deposito_concluido is not None:
        saldo = deposito_concluido[0]
        extrato = deposito_concluido[1]
        contador_extrato += 1
        banco_cadastros[numero_conta-1][5] = saldo

    elif opcao.lower() == "s":
      saque_concluido = aba_saques(saldo=saldo, extrato=extrato, 
                                   numero_saques=numero_saques, 
                                   contador_extrato=contador_extrato,
                                   total_sacado=total_sacado)
      if saque_concluido is not None:
        numero_saques = saque_concluido[0]
        saldo = saque_concluido[1]
        extrato = saque_concluido[2]
        total_sacado = saque_concluido[3]
        contador_extrato += 1
        banco_cadastros[numero_conta-1][5] = saldo

    elif opcao.lower() == "e":
      aba_extrato(saldo, extrato = extrato)
    
    elif opcao.lower() == "l":
      limite_concluido = aba_limites(limite = limite, total_sacado = total_sacado, 
                                     numero_saques = numero_saques)
      if limite_concluido is not None:
        limite = int(limite_concluido)

    elif opcao.lower() == "c":
      aba_conta(numero_conta)
    
    elif opcao.lower() == "q":
      login_e_cadastro()
      return numero_saques, saldo, extrato, total_sacado, contador_extrato
    else:
      print("Erro! Opção Inexistente, Tente Novamente!")

# Heading
print("=" * 30)
print("SISTEMA BANCÁRIO".center(30))
print(f"Data: {data_formatada}".center(30))
print("=" * 30)

# Login e Cadastro
login_e_cadastro()
 
# Dentro da conta

retorno_conta = conta( extrato = extrato, 
      contador_extrato = contador_extrato, 
      numero_saques = numero_saques,
      total_sacado = total_sacado,
      limite = limite,
      numero_conta = numero_conta)

numero_saques = retorno_conta[0]
saldo =  retorno_conta[1]
extrato = retorno_conta[2]
total_sacado = retorno_conta[3]
contador_extrato = retorno_conta[4]