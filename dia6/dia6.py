def fatorial_loop(n):
  if n < 0:
    return "Fatorial não definido para números negativos."
  elif n == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, n+1):
      fatorial *= i
    return fatorial


numero = int(input("Digite um número: "))
resultado = fatorial_loop(numero)
print(f"O fatorial de {numero} é {resultado}")