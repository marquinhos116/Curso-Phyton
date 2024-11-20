alert('Boas Vindas ao Jogo do Número Secreto');
let numeroSecreto  = 28;
let chute = prompt('Escolha um número entre 1 e 30')

if( chute == numeroSecreto) {
    alert(`isso ai! Você descobriu o mumero secreto ${numeroSecreto}`)
}

else{
    alert('você errou')
}