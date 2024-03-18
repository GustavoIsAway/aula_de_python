triangulo = input("Introduza os lados do seu triângulo separados por barra de espaço").split()


triangulo = list(map(int, triangulo))
cond = triangulo[0] + triangulo[1]


if cond > triangulo[2]:

  print("Esse triângulo existe.")

  if triangulo[0] == triangulo[1] == triangulo[2]:
    print("Esse triângulo é equilátero.")

  elif triangulo[0] != triangulo[1] and triangulo[0] != triangulo[2]:
    print("Esse triângulo é escaleno.")

  else:
    print("Esse triângulo é isósceles.")

else:
  print("Esse triângulo NÃO existe.")