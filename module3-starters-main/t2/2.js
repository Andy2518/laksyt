"use strict";

let firstItem = "First item"
let secondItem = "Second item"
let thirdItem = "Third item"

let lista = document.getElementById("target");

let li1 = document.createElement("li");
li1.textContent = firstItem;
lista.appendChild(li1);

let li2 = document.createElement("li");
li2.textContent = secondItem;
lista.appendChild(li2);

let li3 = document.createElement("li");
li3.textContent = thirdItem;
lista.appendChild(li3);