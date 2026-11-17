function inverso(valor) {
    if(valor == true) {
        return false;
    }
    else if(valor == false) {
        return true;
    }
    else if (valor > 0 || valor < 1) {
        return -valor;
    }
    else {
        return `booleano ou valor numérico esperado, mas o parâmetro é do tipo ${typeof valor}`;
    }
}

console.log(inverso('Pedro'))