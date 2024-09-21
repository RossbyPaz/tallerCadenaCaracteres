#Punto 1
name ="Luis"
age=27
favouriteFood="Pasta con salsa Boloñesa"

presentacion=f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(presentacion)

#Punto 2

nombre = input("Hola, Ingresa tu nombre completo: ")

contarNombre = len(nombre.replace(" ", ""))


saludo = f"Hola, {nombre}! Tu nombre tiene {contarNombre} letras."

# Mostrar el mensaje
print(saludo)

#punto 3
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
mensaje = f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y los ingresos crecieron un {revenueGrowthPercent:.2f}%."
print(mensaje)

# Punto 4

secretMessage = "aS!Ir waQm VL!eDafrcnXi n=gS .P,yytahgoln.!"

# Decodificar el mensaje: omitir los primeros tres caracteres y luego tomar cada segundo carácter
decodedMessage = secretMessage[3::2]

# Mostrar el mensaje decodificado
print(decodedMessage)