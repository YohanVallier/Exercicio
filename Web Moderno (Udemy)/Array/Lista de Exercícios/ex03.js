function multiplicar(numero, multiplicador) {
    numeroMultiplicado = 0
    for(i = 0; i < multiplicador; i++) {
        numeroMultiplicado += numero;
    }
    return numeroMultiplicado;
}

console.log(multiplicar(10, 5), multiplicar(0, 7));