function repetir(valor, multiplicador) {
    array = []
    for(i = 0; i < multiplicador; i++) {
        array.push(valor);
    }
    return array;
}

console.log(repetir(7, 3))