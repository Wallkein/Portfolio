var btn = document.getElementById("myBtn");
var modal = document.getElementById("myModal");
var clos = document.getElementById("myClose");
var content = document.getElementById("cont");

function opacity1() {
    content.style.opacity = 1;
}

function none() {
    modal.style.display = "none";
}

btn.onclick = function() {
    modal.style.display = "block";
    setTimeout(opacity1, 100);
}

clos.onclick = function() {
    content.style.opacity = "0";
    setTimeout(none, 1000);
}
