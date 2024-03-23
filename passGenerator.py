import random
import string

longitud = int(input("Tamaño de la contraseña (números): "))

caracteres = string.ascii_letters + string.digits + string.punctuation

passwd = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: \n" + passwd)
