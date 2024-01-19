//DESAFIOS - BOAS PRÁTICAS DE PROGRAMAÇÃO

// atividade 1
console.log('Boas-vidas');

// ativdade 2 e 3
let nome = 'Victor Anibal'
console.log(`Olá, ${nome}!`)
alert(`Olá, ${nome}!`);

// atividade 4
let lang_Prog = prompt('Qual a linguagem de que você mais gosta?');
console.log(lang_Prog);

// atividade 5
let valor1 = 5;
let valor2 = 6;
let resultado = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é igual a ${resultado}.`);

// atividade 6
let resultado2 = valor1 - valor2;
console.log(`A diferença entre ${valor1} e ${valor2} é igual a ${resultado2}.`;

// atividade 7
let idade = prompt('Digite a sua idade?');
if (idade > 17) {
    console.log(('Você é maior de idade.'));
} else {
    console.log(('Você é menor de idade.'));
}

// atividade 8
numero = parseFloat(prompt("Digite um número qualquer:"))
if (numero > 0) {
    alert("O número é positivo!");
} else if (numero < 0) {
    alert("O número é negativo!");
} else {
    alert("O número é zero!");
}
// atividade 9
number = 1;
while (number <= 10) {
    console.log((number));
    number++;
}

// atividade 10
nota = 7
if (nota >= 7) {
    console.log(('Aprovado'));
} else {
    console.log(('Reprovado'));
}

// ativdade 11
let numeroAleatorio = Math.random();
console.log(numeroAleatorio);

// atividade 12
let numeroInteiroAleatorio = parseInt(Math.random() * 10 + 1); 
console.log(numeroInteiroAleatorio);

// atividade 13
let numeroInteiroAleatorio2 = parseInt(Math.random()* 1000) + 1;
console.log(numeroInteiroAleatorio2);