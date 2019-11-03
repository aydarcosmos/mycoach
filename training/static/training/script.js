function random() { 
    return Math.ceil(Math.random() * 100);
}
function hello() {
    alert('пока не создано!');
}
var num = random();

elem = document.getElementById('registration');
elem.onclick = hello;