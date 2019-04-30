/**
 * Created by Ben on 10/25/2015.
 */
"use strict";


function draw_curve_full(context, A, B,  a, b, delta, start, step, num, xd, yd) {
    context.beginPath();
    let x = A*Math.cos(a*start+delta) + xd;
    let y = B*Math.sin(b*start) + yd;
    context.moveTo(x,y);
    for(let i = 1; i < num; i++ ) {
        x = A*Math.cos(a*(start+i*step) + delta) + xd;
        y = B*Math.sin(b*(start+i*step)) + yd;
        context.lineTo(x,y)
    }
    context.stroke();
}

function draw_curve(canvas, a, b, num_steps) {
    let pad = 50;
    let delta = 0;
    let start = 0;
    let end = 2*Math.PI;

    let w = canvas.width;
    let h = canvas.height;
    let A = w / 2 - pad;
    let B = h / 2 - pad;
    let xd = w / 2;
    let yd = h / 2;
    let context = canvas.getContext('2d');
    let step = (end-start)/(num_steps-1);
    context.clearRect(0,0,w,h);
    draw_curve_full(context, A, B, a, b, delta, start, step, num_steps, xd, yd);
}

function curve1() {
    let draw = document.getElementById("canvas");
    let context = draw.getContext('2d');
    draw_curve_full(context, 200, 200, 3, 4, 0,
        0, Math.PI/50, 101, 250, 250);
}


function curve2() {
    let draw = document.getElementById("canvas");
    draw_curve(draw, 5,6, 5000);
}

function input_changed(a_elem, b_elem) {
    let a = parseInt(a_elem.value);
    //par("a is ", a);
    let b = parseInt(b_elem.value);
    let canvas = document.getElementById("canvas");
    if(!isNaN(a) && !isNaN(b) && a > 0 && b > 0) {
        draw_curve(canvas, a, b, 500);
    }

}

function output() {
    let oa = document.getElementById("output-area");
    for(let i = 0; i < arguments.length; i++ ){
        let tn  = document.createTextNode(arguments[i]);
        oa.appendChild(tn);
    }
}

function par() {
    let oa = document.getElementById("output-area");
    let pe = document.createElement("p");
    oa.appendChild(pe);
    for(let i = 0; i < arguments.length; i++ ){
        let tn  = document.createTextNode(arguments[i]);
        pe.appendChild(tn);
    }
}

function setup() {
    let a_elem = document.getElementById("a");
    let b_elem = document.getElementById("b");
    a_elem.addEventListener('input',function() {
        input_changed(a_elem, b_elem);

    });
    b_elem.addEventListener('input', function() {
        input_changed(a_elem, b_elem);
    })
    //par("setup is done");
}
