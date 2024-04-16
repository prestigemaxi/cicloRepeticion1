#solicitar cantidad de pasajes
#crear ciclo de repeticion for
#solicitar precio del pasaje
#validar con try except
#totalingresos
#romper bucle con break
#mostrar info del total de pasajes
totalIngresos = 0
banderaCantidad = True
banderaPrecio = True
while banderaCantidad:
    try:
    
    
        cantidad = int(input("ingrese cantidad de pasajes\n"))
        for x in range(cantidad):
            while banderaPrecio:
                try:
                     precio = int(input(f"ingrese precio para pasaje n{x+1}\n"))
                     totalIngresos = totalIngresos + precio
                     break
                except:
                   print("precio no existe")
        break              
    except:
         print("opcion no valida")
    print(f"para los {cantidad} pasajes, el valor a pagar es : ${totalIngresos}")

    
    
    
    
