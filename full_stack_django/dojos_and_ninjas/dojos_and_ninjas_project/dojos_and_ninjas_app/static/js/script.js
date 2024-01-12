// Script for bike_footer

var mouseCurrent = 0;
var mouseX = 0, mouseY = 0;
var follower = document.querySelector("#image");

document.addEventListener("mousemove", function(e) {
mouseX = e.pageX;
mouseY = e.pageY;

if (mouseX > mouseCurrent) {
    follower.classList.remove("flipped");
} else if (mouseX === mouseCurrent) {
    // no change
} else {
    follower.classList.add("flipped");
}

mouseCurrent = mouseX;
});

var xp = 0, yp = 0;
var loop = setInterval(function() {
xp += (mouseX - xp) / 32; //32
// yp += (mouseY - yp) / 20; //20
follower.style.left = xp + "px";
}, 30);

document.addEventListener("mousedown", function(e) {
follower.classList.add("jumping");
});

document.addEventListener("mouseup", function(e) {
follower.classList.remove("jumping");
});