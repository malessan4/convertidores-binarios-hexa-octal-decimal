def decimal_a_binario(decimal):
    # Convertir de decimal a binario
    binario = bin(decimal)
    return binario[2:]  # Retornar sin el prefijo '0b'

def decimal_a_octal(decimal):
    # Convertir de decimal a octal
    octal = oct(decimal)
    return octal[2:]  # Retornar sin el prefijo '0o'

def decimal_a_hexadecimal(decimal):
    # Convertir de decimal a hexadecimal
    hexadecimal = hex(decimal)
    return hexadecimal[2:].upper()  # Retornar sin el prefijo '0x' y en mayúsculas

# Ejemplo de uso
decimal=int(input("ingrese su número decimal: "))
print(f"Binario: {decimal_a_binario(decimal)}")
print(f"Octal: {decimal_a_octal(decimal)}")
print(f"Hexadecimal: {decimal_a_hexadecimal(decimal)}")