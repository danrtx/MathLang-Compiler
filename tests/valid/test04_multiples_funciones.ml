// Test 04: Funciones que se llaman entre si
func cuadrado(x) {
    return x * x;
}
func sumaCuadrados(a, b) {
    return cuadrado(a) + cuadrado(b);
}
res = sumaCuadrados(3, 4);
print(res);
