function estaEntre(numero, minimo, maximo, inclusivo = false) {
    if(inclusivo) {
        return minimo < numero && numero < maximo;
    }
    else {
        return minimo <= numero && numero <= maximo;
        }
}

console.log(estaEntre(16, 100, 160))