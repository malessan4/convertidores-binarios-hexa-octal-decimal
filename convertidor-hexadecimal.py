def hexadecimal_a_decimal(hexadecimal):
    # Convertir de hexadecimal a decimal
    decimal = int(hexadecimal, 16)
    return decimal

def hexadecimal_a_binario(hexadecimal):
    # Convertir de hexadecimal a decimal y luego a binario
    decimal = int(hexadecimal, 16)
    binario = bin(decimal)
    return binario[2:]  # Retornar sin el prefijo '0b'

def hexadecimal_a_octal(hexadecimal):
    # Convertir de hexadecimal a decimal y luego a octal
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)
    return octal[2:]  # Retornar sin el prefijo '0o'

# Solicitar el valor hexadecimal al usuario
hexadecimal = input("Ingresa un número hexadecimal: ")

# Mostrar las conversiones
print(f"Decimal: {hexadecimal_a_decimal(hexadecimal)}")
print(f"Binario: {hexadecimal_a_binario(hexadecimal)}")
print(f"Octal: {hexadecimal_a_octal(hexadecimal)}")