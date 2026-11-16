function receberPrimeiroEUltimo (array) {
    listaArray = [];
    listaArray.push(array[0]);
    listaArray.push(array[array.length - 1]);
    return listaArray;
}

console.log(receberPrimeiroEUltimo([-100, 14, "aplicativo", "olá", 16]))