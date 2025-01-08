# nombre="Diego RIVERA"
# edad=64

# print("Mi nombre es ",nombre, " y mi edad es ",edad)

# print("Ingrese un numero")
# num1=int(input())
# print("Ingrese otro numero")
# num2=int(input())

# print(num1+num2)


# print("Ingrese un numero")
# num1=int(input())
# if num1>0:
#     print("El numero es positivo")
# else:
#     print("El numero es negativo o cero")

# print("Ingrese un numero")
# num1=int(input())
# print("Ingrese otro numero")
# num2=int(input())
# print("Ingrese un tercer numero")
# num3=int(input())
# print((num1+num2+num3)/3)


# Parque nacional que tiene los siguientes valores

# Menor de 12 $500
# Entre 13 y 18 $1000
# entre 19 y 64 $2000
# mas de 65 $700

# BONUS * pregunte cauntas entradas son

# Pertenece a la Florida?
# No = Gracias por visitar
# Si= Continua la sig

# Tiene carnet de socio?
# No= Creque su carnet acá (*Crea carnet*)
# Si= Ingrese su numero

# Es jubilado?
# NO= paga monto total 
# SI= paga monto con descuento (25%)

# Su total a pagar es {total}

# print("Ingrese un numero")
# num1=int(input())
# if num1 >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

# print("ingrese un numero")
# num1=int(input())
# num2=int(input())
# num3=int(input())
# promedio=(num1+num2+num3)//3

# print("su promedio es", promedio)


#EJERCICIO ENTRADAS
# Total=int(input("cuantas entradas desea"))
# valor=0
# for i in range(Total):

#     print("Ingrese su edad")
#     edad=int(input())
#     if edad < 12 :
#         print("El precio de la entrada es de 500$")
#         valor=valor+500
#     else:
#         if edad >= 13 or edad <=18:
#             print("el costo de su entrada es de $1000")
#             valor=valor+1000
#         else:
#             if edad >= 19 or edad <= 64:
#                 print("el precio de su entrada es de $2000")
#                 valor=valor+2000

#             else:
#                 print("El precio de su entrada es de 700")
#                 valor=valor+700
        
# print(f"El valor total es de {valor}")

direc=input("¿Pertenece a comuna la florida?/SI-NO")
monto=5000
if direc == "si":
    # print("continue con la siguiente fase")
    carnet=input("Tiene carnet de socio?").lower()
    if carnet == "si":
        int(input("Ingrese su numero de carnet"))
        print("Perfecto pase a la siguiente fase")
        jub=input("Es jubilado?").lower()
        if jub == "si":
            print("Debe pagar el monto de $5000 , pero con un descuento del 25%")
            desc=monto*0.75
            print(f"Su monto a cancelar es de{desc}")

        else:
            print("Cancele el monto completo")
            print(f"El monto a cancelar es de {monto}")

    else:
        print("Debe crear su carnet")
        Nombre=input("Ingrese su nombre completo")
        Rut=int(input("ingrese su rut sin guion"))
        telf=int(input("Ingrese su numero de telefono"))
        print("Carnet creado correctamente")
        int(input("Ingrese su numero de carnet"))
        print("Perfecto pase a la siguiente fase")
        jub=input("Es jubilado?")
        if jub == "si":
            print("Debe pagar el monto de $5000 , pero con un descuento del 25%")
            desc=monto*0.75
            print(f"Su monto a cancelar es de{desc}")

        else:
            print("Cancele el monto")
            print(f"El monto a cancelar es de {monto}")
else:
    print("Gracias por visitar")
    
#variable boleana
lider_abierto=True
leche_sin_lactosa=True
caja_habilitada=True
sistema_de_pago=False
    
if lider_abierto:
    print("Puede entar al super")
    if leche_sin_lactosa:
        print("Hay leche sin lactosa")
        if caja_habilitada:
            print("Hay cajas habilitadas")
            if sistema_de_pago:
                print("Puede pagar con debito")
            else:
                print("Puede pagar con efectivo")
    
    
    
