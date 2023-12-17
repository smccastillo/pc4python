with open('texto.txt', 'w') as archivo: #para guardar el texto en un archivo 
    archivo.write("En el ámbito del desarrollo de software, la colaboración es fundamental. La colaboración eficiente impulsa la eficacia y mejora la calidad del código. La calidad del código, a su vez, es esencial para la mantenibilidad del sistema. Mantener un sistema sin problemas es esencial para la satisfacción del cliente. La satisfacción del cliente, por supuesto, es un objetivo clave para cualquier equipo de desarrollo. Desarrollar estrategias para fomentar la colaboración continua y mejorar la calidad del código es una práctica que beneficia a todos los miembros del equipo y contribuye al éxito general del proyecto.")

with open('texto.txt', 'r') as archivo:
    contenido = archivo.read()
    conteo_la = contenido.lower().count("la")

print(f"La palabra 'la' aparece {conteo_la} veces en el texto.")

# Ingresar un texto agregarlo al final del archivo txt
nuevo_texto = input("Ingrese un nuevo texto: ")
with open('texto.txt', 'a') as archivo:
    archivo.write('\n' + nuevo_texto)

print("Texto agregado al final del archivo.")

with open('texto.txt', 'r') as archivo:
    contenido_actualizado = archivo.read()

print("\nContenido actualizado del archivo:")
print(contenido_actualizado)