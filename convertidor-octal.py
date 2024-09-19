def octal_a_decimal(octal):
    decimal = int(octal, 8)
    return decimal

def octal_a_binario(octal):
    decimal = int(octal, 8)
    binario = bin(decimal)
    return binario[2:]

def octal_a_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)
    return hexadecimal[2:].upper()

octal = input("Ingrese su número octal: ")
print(f"Decimal: {octal_a_decimal(octal)}")
print(f"Binario: {octal_a_binario(octal)}")
print(f"Hexadecimal: {octal_a_hexadecimal(octal)}")