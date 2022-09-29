import random

ingles = []
espanol = []
indice = 0
with open('words.txt') as f:
	c = [i for i in f]
	for i in c:
		palabras = ""
		for j in i:
			if j == " ": break
			palabras += j
		ingles.append(palabras) 
	for i in c:
		if i[len(ingles[indice]) + 1:] == "\n": continue
		espanol.append(i[len(ingles[indice]) + 1: -1])
		indice += 1

lista = list(dict(zip(ingles, espanol)).items())
random.shuffle(lista)
correcto = 0
incorrecto = 0

while (incorrecto + correcto) <len(list(dict(zip(ingles, espanol)).items())):
	azar = random.randint(0,1)
	print("Pregunta :",lista[0][azar])
	answer = input("Respuesta : ").lower()
	if azar == 0:
		if lista[0][1] == answer: 
			print("Opción correcta")
			correcto += 1
		else:
			print("Opción incorrecta. La respuesta era:", lista[0][1])
			incorrecto += 1
	else:
		if lista[0][0] == answer:
			print("Opción correcta")
			correcto += 1
		else:
			print("Opción incorrecta. La respuesta era:", lista[0][0])
			incorrecto += 1
	del lista[0]
print("Respuestas correctas:",correcto)
print("Respuestas incorrectas:",incorrecto)
