const trataDinheiro = (din) => {return `R$${din.toFixed(2).replace('.', ',')}`;}

console.log(trataDinheiro(0.3000000000000000004));