'use strict';
const names = ['John', 'Paul', 'Jones'];

let tulostus = document.getElementById("target");

for (let i = 0; i < names.length; i++) {
    tulostus.innerHTML += `<li>${names[i]}</li>`;
}
