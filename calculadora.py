# calculadora
#Criação das variaveis das operações
def soma(num1, num2):
  try: # tratamento de erro,se por exemplo o usuário digitar um caracter inválido,uma letra etc.
   soma = num1 + num2
   return soma
  except : # tratamento de erro. Mensagem que deve ser exibida ao usuário
    print("Erro: Valor inválido!")
def subtracao(num1, num2):
  try:
    subtracao = num1 - num2
    return subtracao
  except:
    print("Erro: Valor inválido!")
def multiplicacao(num1, num2):
  try:
    multiplicacao = num1 * num2
    return multiplicacao
  except :
    print("Erro: Valor Inválido!")
def divisao(num1, num2):
  try:
    divisao = num1 / num2
    return divisao
  except :
    divisao = num1 / 0 # tratamento para não permitir a divisão por zero
    print("Erro: Valor inválido!")

#loop se o usuário decide continuar fazendo operações

while True:
  try:
        num1 = float(input("Olá, digite o primeiro número: "))
        acao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        result = input("digite memoria para imprimir o resultado:").upper()


#execução das operações
        if result == "MEMORIA":

          if acao == "+":
            print(f'Resultado = {soma(num1, num2)}')
          elif acao == "-":
            print(f'Resultado = {subtracao(num1, num2)}')
          elif acao == "*":
            print(f'Resultado = {multiplicacao(num1, num2)}')
          elif acao == "/":
            print(f'Resultado = {divisao(num1, num2)}')




#tomada de decisão do usuário
        stop = input("deseja continuar (s/n)").upper()
        if stop != "S":
           break
  except:
        print ("Erro: Valor inválido!")
