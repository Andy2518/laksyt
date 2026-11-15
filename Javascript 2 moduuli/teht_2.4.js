"use strict";

let lista = []
let luku;
do {
    luku = parseInt(prompt("Anna luku:"))
    if (luku !== 0) {
        lista.push(luku)
    }
} while (luku !== 0);

lista.sort((a, b) => b - a);

for (let numero = 0; numero < lista.length; numero++) {
    console.log(lista[numero]);
}