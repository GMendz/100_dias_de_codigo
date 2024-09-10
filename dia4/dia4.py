def calculadora():
   while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
      except ValueError:
        print("Por favor, insira apenas números.")
        continue

      if escolha == '1':
        print(num1, "+", num2, "=", num1 + num2)
      elif escolha == '2':
        print(num1, "-", num2, "=", num1 - num2)
      elif escolha == '3':
        print(num1, "*", num2, "=", num1 * num2)
      elif escolha == '4':
        if num2 == 0:
          print("Divisão por zero não é permitida.")
        else:
          print(num1, "/", num2, "=", num1 / num2)
    elif escolha == '5':
      break
    else:
      print("Opção inválida.")

calculadora()