# if

llueve = False
if llueve:
    print("Tomaré un paraguas")
else:
    print("Iré de paseo")


dinero_que_tengo = 13

if dinero_que_tengo < 2:
    print("compraré algo del super")
elif dinero_que_tengo < 5:
    print("Tomaré un bocata sencillo")
elif dinero_que_tengo <=12:
    print("Tomaré un menú sencillo")
else:
    print("Tomaré un bistec en el restaurante")


print("Buen provecho")


"""
"""

dia_semana = "jueves"
match dia_semana:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case _ :
        print("Hoy no es lunes ni martes")

