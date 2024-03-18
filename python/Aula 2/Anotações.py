##Conversão de Tipos
a = int("44")
b = float("44")
c = str(44)
d = str(44.3)

print(type(a), type(b), type(c), type(d))

##Input - DEVOLVE 'str' POR PADRÃO
input() ##Input cru: trava o programa até introdução de um valor.
input("Texto indicativo: ") ##Trava o programa mostrando, antes, um texto.
int(input())  ##Procura converter o valor introduzido para inteiro
float(input())  ##Pocura converter o valor introduzido para float


##Controle de Fluxo
if a == 44: ##Condição if
  print("A é um inteiro.")
elif type(a) == int:  ##Condição elif (abreviação de else if)
  print("A é um inteiro.")
else:
  print("Nenhuma das condições anteriores é verdade.")


###Ternário para Controle de Fluxo - Resume situações if - else a uma só linha

'(resultado 1) if "condição" else (resultado 2)'

####Ao declarar uma variável
e = (3 if a == 44 else 0) #Parênteses não é obrigatório.

####Dentro de funções
print("É 3" if e == 3 else "Não é três")

####Ao realizar tarefas
print("C é string") if type(c) == str else None