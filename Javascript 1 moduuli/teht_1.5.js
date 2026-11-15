"use strict";

let vuosi = parseInt(prompt("Anna vuosiluku"));

let tulos = document.querySelector("#tulos")

if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0))
{
  tulos.innerHTML = `${vuosi} on karkausvuosi`;
}
else
{
  tulos.innerHTML = `${vuosi} ei ole karkausvuosi`;
}