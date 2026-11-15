"use strict";

let alku = parseInt(prompt("Anna alkuvuosi"))
let loppu = parseInt(prompt("Anna loppuvuosi"))

let lista = document.getElementById("lista")

for (let vuosi = alku; vuosi <= loppu; vuosi += 1)
{
    if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0))
    {
        lista.innerHTML += `<li>${vuosi}<li>`;
    }
}