"use strict";

let numero1 = parseInt(prompt("Anna numero"));
let numero2 = parseInt(prompt("Anna numero"));
let numero3 = parseInt(prompt("Anna numero"));

let sum = numero1 + numero2 + numero3;
let product = numero1 * numero2 * numero3;
let avg = numero1 + numero2 + numero3 / 3;

let tulostus = document.getElementById("tulos");

tulostus.innerHTML = `Summa: ${sum}<br>
                      Tulo: ${product}<br>
                      Keskiarvo: ${avg}`;