"""
# Ejercicio
"""

# Vamos a preguntar al usuario cuantos segundos
# y vamos a decirle cuantas horas, minutos y segundos son

# Por ejemplo:
# 3601
# 1 horas 0 minutos 1 segundos
# 3662
# 1 horas 1 minutos 2 segundos

# respuesta = int(input("¿Cuántos segundos?"))


print("MUESTRA LOS VALORES RESTANTES DE HORAS, MINUTOS Y SEGUNDOS.")
segundos = float(input("Introduce Cantidad en Segundos : "))
horas = round(segundos/3600)
min = round((segundos - (horas * 3600)  )/60)
seg = round(segundos - ((horas * 3600) + (min * 60)))

print("HORAS   : ", horas)
print("MINUTOS : ", min)
print("SEGUNDOS: ", seg)
