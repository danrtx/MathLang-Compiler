# Codigo Python generado por MathLang Compiler
# Universidad Cooperativa de Colombia - Compiladores
import math

def cuadrado(x):
    return (x * x)

def areaCirculo(r):
    return ((3.14159 * r) * r)

def hipotenusa(a, b):
    return (cuadrado(a) + cuadrado(b))

a = 5
b = 3
c = (cuadrado(a) + b)
print(c)
radio = 7
area = areaCirculo(radio)
print(area)
hip = hipotenusa(3, 4)
print(hip)