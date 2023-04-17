print("Bom dia, eu sou a Calculadora Universal. Pode me chamar de CU. Ainda estou em desenvolvimento mas espero atender suas expectativas")

n1 = int(input("Qual o primeiro número do cálculo? "))
n2 = int(input("E o segundo número? "))
calculo = input("Qual operação você deseja fazer? Soma, subtração, multiplicação ou divisão? ")
print("Espere um pouco enquanto eu calculo....")

if(calculo == "soma"):
  resultado = n1 + n2
elif(calculo == "subtração"):
  resultado = n1 - n2
elif(calculo == "multiplicação"):
  resultado = n1 * n2
elif(calculo == "divisão"):
  resultado = n1 / n2
else:
  print("Operação inválida. Tente novamente.")
  exit()

print("O resultado do seu cálculo é " + str(resultado))
print("Espero ter ajudado, até a próxima")