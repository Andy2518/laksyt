"use strict";

let lista = [];

for (let numero = 0; numero < 5; numero++) {
    let numerot = parseInt(prompt(`Anna numero ${numero + 1}/5:`));
    lista.push(numerot)
}

for (let numero = lista.length - 1; numero >= 0; numero--) {
    console.log(lista[numero]);
}

