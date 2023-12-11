# Vamos a un comercio y compramos algo
# El usuario nos indica el precio y lo que paga

# Si paga menos de lo que vale indicamos que falta dinero

# Si paga correctamente devolvemos el cambio de tal manera 
# que lo haremos con los billetes y monedas de mayor valor posible

coste_del_producto = 100
pago_del_producto = 199

billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

if coste_del_producto > pago_del_producto :
    print (f"Sr cliente: faltan {coste_del_producto-pago_del_producto} €")
else :
    cambio = pago_del_producto - coste_del_producto
    respuesta_cambio = ""
    for dinero in billetes_monedas:
        if cambio >= dinero:
            respuesta_cambio += f"{cambio//dinero} de {dinero}\n"
            cambio = cambio - ((cambio//dinero) * dinero)

    print(respuesta_cambio)
