def binario_a_decimal(binario):
    # Convertir de binario a decimal
    decimal = int(binario, 2)
    return decimal

def binario_a_octal(binario):
    # Convertir de binario a decimal y luego a octal
    decimal = int(binario, 2)
    octal = oct(decimal)
    return octal[2:]  # Retornar sin el prefijo '0o'

def binario_a_hexadecimal(binario):
    # Convertir de binario a decimal y luego a hexadecimal
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)
    return hexadecimal[2:].upper()  # Retornar sin el prefijo '0x' y en mayúsculas

# Ejemplo de uso
binario = int(input("Ingrese su número binario: "))
print(f"Decimal: {binario_a_decimal(binario)}")
print(f"Octal: {binario_a_octal(binario)}")
print(f"Hexadecimal: {binario_a_hexadecimal(binario)}")