"use strict";

let osallistujat = parseInt(prompt("Kuinka moni osallistuu?"));
let lista = []

for (let numero = 0; numero < osallistujat; numero++) {
    let nimi = prompt(`Mitkä ovat niiden ${numero + 1} nimet?`);
    lista.push(nimi);
}

lista.sort((a, b) => a.localeCompare(b, "fi"));

for (let numero = 0; numero < lista.length; numero++) {
    document.getElementById("tulos").innerHTML += `<li>${lista[numero]}<br></li>`;
}