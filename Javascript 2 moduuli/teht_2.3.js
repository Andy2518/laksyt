"use strict";

let lista = []

for (let numero = 0; numero < 6; numero++) {
    let koiran_nimi = prompt(`Anna koiran ${numero} nimi`);
    lista.push(koiran_nimi)
}

lista.sort((a, b) => b.localeCompare(a, "fi"));

for (let numero = 0; numero < lista.length; numero++) {
    document.getElementById("tulos").innerHTML += `<li>${lista[numero]}</li>`;
}