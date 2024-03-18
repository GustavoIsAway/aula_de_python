a = input("Introduza os números para a média separados pro espaço: ").split()
a = list(map(int, a))
media = sum(a) / len(a)
print(media)