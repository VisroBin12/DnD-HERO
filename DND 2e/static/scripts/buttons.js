let elemToClean = document.getElementsById("cleaner").children
let radios = document.getElementsByClassName("radio")
function radio(className){
    for (let e = 0; e < elemsToClean.lenght; e++){
        elemsToClean[e].style.display = "none"; //чистим форму от всех полей
    }
    for (let e = 0; e < radios.lenght; e++){
        radios[e].style.disable = true; //дуактевируем все радиокнопки
    }
    // clicketElement.style.disable = false; //делаем кнопку по которой мы нажали активной

    elemsToShow = document.getElementsByClassName(className)
    for (let e = 0; e < elemsToShow.lenght; e++){
        elemsToShow[e].style.display = "block"; //показываем элементы которые нам нужно
    }
}


//    let radios =document.getElementsByClassName("radio");
//     let elements =document.getElementsByClassName("className");
// }
// document.getElementById("")
// spells[0].style.display = "none"
// for (let e = 0; e < spells.length; e++){
//     spells[e].style.display = "none";
// };