function ladoDeTriangulo(a, b, c) {
    let resposta;
    if(a = b = c) {
        resposta = console.log("Triângulo Equilátero");
    }else if(a == b || b == c || a == c) {
        resposta = console.log("Triângulo Isósceles");
    }else if(a != b != c) {
        resposta = console.log("Triângulo Escaleno");
    }  
    return resposta;
}

ladoDeTriangulo(5, 5, 5)