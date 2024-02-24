def fibonacci(n):
  a, b = 0, 1
  serie = []
  for i in range(n):
    serie.append(a)
    a, b = b, a + b
  return serie
numero = 10
serie_fibonacci = fibonacci(numero)
print(f"La serie de Fibonacci hasta el {numero}-ésimo número es: {serie_fibonacci}")
