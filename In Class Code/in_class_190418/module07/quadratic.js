/**
 * Created by ben on 6/29/15.
 */
"use strict";



function doSolve(event) {
    document.getElementById("error-message").innerHTML = "";
    //alert(event);
    let d2Input = document.getElementById("coeff2");
    let d1Input = document.getElementById("coeff1");
    let d0Input = document.getElementById("coeff0");

    let d2 = parseFloat(d2Input.value);
    let d1 = parseFloat(d1Input.value);
    let d0 = parseFloat(d0Input.value);

    let disc = d1*d1 - 4*d2*d0;
    //alert('disc is ' + disc)

    let r1Out = document.getElementById("root1");
    let r2Out = document.getElementById("root2");


    if(!d2Input.value) {
        d2Input.value = "Must provide a value"
    }
    if(!d1Input.value) {
        d1Input.value = "Must provide a value"
    }
    if(!d0Input.value) {
        d0Input.value = "Must provide a value"
    }


    if(isNaN(disc)) {
        // alert("Invalid values entered");
        document.getElementById("error-message").innerHTML =
            "There was an error in the input data"
    } else if(disc >= 0) {
        let dsq = Math.sqrt(disc);
        let root1 = (-d1 + dsq)/(2*d2);
        r1Out.innerText = root1.toString();
        let root2 = (-d1 - dsq)/(2*d2);
        r2Out.innerText = root2.toString();
    } else {
        r1Out.innerHTML = "<strong>Root is complex</strong>";
        r2Out.innerHTML = "<strong>Root is complex</strong>";
    }

}



window.addEventListener("load",
    function () {
        let compButton = document.getElementById("computeButton");
        compButton.addEventListener('click', doSolve);
    });



