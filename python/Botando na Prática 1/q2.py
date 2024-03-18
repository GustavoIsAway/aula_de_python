a = float(input("Introduza o valor 1: "))
b = float(input("Introduza o valor 2: "))
c = float(input("Introduza o valor 3: "))
maior = 0

if a > c:
  if b > a:
    maior = b
  else:
    maior = a

else:
  if c > b:
    maior = c
  else:
    maior = b

print(maior)