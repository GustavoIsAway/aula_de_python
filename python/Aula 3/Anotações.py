###CONDIÇÕES MÚLTIPLAS
a = 0
if a / 2 == 0 and a % 2 == 0: #and
  print("A é zero E par")

b = 63
if b / 2 == 10 or b % 2 == 1: #or
  print("B divido por 2 não é 10, mas ele é ímpar. Então a condição é verdade.")

c = 14
if not (c == 14): #not
  print("Isso nunca vai ser printado desse jeito. O not sempre nega verdades.")



###COLEÇÕES - Tipos que armazenam dados em um único lugar
lista = [1, "2", 3.0] #Componentes possui um index de posição. São mutáveis.
uma_tuple = (1, "2", 3.0) #Componentes possem index de posição. São imutáveis.
uma_range = range(10) #Gera um intervalo de 0 até o número entre parênteses - 1.
#Dicionários? Ainda não, pai.



##OPERAÇÕES COM LISTAS
nova_lista = [1, 2, 3]


print("CONTROLE:", nova_lista)
print("Comprimento da lista:", len(nova_lista))
print("Referenciando um elemento:", nova_lista[1])

nova_lista.append(4) #[1, 2, 3, 4] Insere o valor em parênteses como último item
print("Após o append:", nova_lista)

nova_lista.pop() #[1, 2, 3] Remove o último item
print("Após o pop:", nova_lista)

nova_lista.reverse() #[3, 2, 1] Inverte a ordem dos elementos
print("Após o reverse:", nova_lista)

nova_lista.insert(0, 4) #[4, 3, 2, 1] Insere um elemento: (index, elemento)
print("Após o insert", nova_lista)

nova_lista[0] = 5 #[5, 3, 2, 1] Associando um novo valor a um elemento
print("Associando novo valor ao index 0:", nova_lista)

del nova_lista[3]  #[5, 3, 2] Deleta um item por meio do seu index
print("Deletando index 3:", nova_lista)