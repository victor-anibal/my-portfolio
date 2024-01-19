alert('Boas vindas ao jogo do número secreto');
let numeroMax = 1000
let numeroSecreto = parseInt(Math.random() * numeroMax + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 0

while (chute != numeroSecreto) {

    chute = prompt(`Escolha um número de 1 a ${numeroMax}`);

    tentativas++

    //Se o número for igual ao numeroSecreto
    if (chute == numeroSecreto) {
        break;
        //Se o número não for igual ao numeroSecreto
    } else {
        if (chute < numeroSecreto) {
            alert('O número secreto é maior que ' + chute);
        }
        else {
            alert(`O número secreto é menor que o ${chute}`);
        }

    }
}
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);

// if (tentativas > 1){
//     alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas.`);
// } else{
//     alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativa.`);
// }
