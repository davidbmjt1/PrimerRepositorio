# Array

mi_array = ["café", 1.5, True]
print(mi_array)

# Si me gusta el café tomaré uno a 1.5€
if mi_array[2]:
    print(f"me gusta el {mi_array[0]} a {mi_array[1]} €")


'''
'''

cosas_que_me_gustan = []
# respuesta = input("¿Qué te gusta? --> ")
# cosas_que_me_gustan.append(respuesta)

print("Cosas que me gustan: \n", cosas_que_me_gustan)

cuantas_cosas_te_gustan = int(input("¿Cuántas cosas te gustan? --> "))
print(type(cuantas_cosas_te_gustan))

for i in range(0, cuantas_cosas_te_gustan):
    respuesta = input("¿Qué te gusta? --> ")
    cosas_que_me_gustan.append(respuesta)
    # print("Buenos días")

print("Cosas que me gustan: \n", cosas_que_me_gustan)


contador = 1
for valor in cosas_que_me_gustan:
    print(f"{contador} - {valor}")
    contador += 1


'''
'''

diccionario_en_Python = {"nombre": "Bill", "apellido": "Gates", "ciudad": "Seatle"}
print(diccionario_en_Python["ciudad"])




alumno_1 = {"nombre": "David", "apellido": "Briones", "ciudad": "Hospi"}
alumno_2 = {"nombre": "Vicky", "apellido": "Lamas", "ciudad": "Barcelona"}


lista_alumnos = [
    {"nombre": "Bill", "apellido": "Gates", "ciudad": "Seattle"},
    {"nombre": "Steve", "apellido": "Jobs", "ciudad": "Cupertino"}
]

lista_alumnos.append(alumno_1)
lista_alumnos.append(alumno_2)

print(lista_alumnos)
