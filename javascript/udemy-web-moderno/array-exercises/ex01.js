Array.prototype.map2 = function (callback) {
    return Array.prototype.map.call(this, callback)};

const carrinho = [ 
    '{"nome": "Borracha", "preco": 3.45}',
    '{"nome": "Caderno", "preco": 13.90}',
    '{"nome": "Caneta", "preco": 7.50}',
    '{"nome": "Kit Lápis", "preco": 41.22}',
]

let paraObjeto = (json) => JSON.parse(json)
let preco = (produto) => produto.preco

let resultado = carrinho.map(paraObjeto).map(preco)

console.log(resultado)  