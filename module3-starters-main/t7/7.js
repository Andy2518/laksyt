"use strict";

let tulostus1 = document.getElementById("trigger");
let tulostus2 = document.getElementById("target");

tulostus1.addEventListener("mouseover", () => {
    tulostus2.src = "img/picB.jpg";
})

tulostus1.addEventListener("mouseout", () => {
    tulostus2.src = "img/picA.jpg";
})

