
    
var value;
var length;
var tX;
var tY;
var lastChar;

function drop(textfield) {
    
    
    value = textfield.value;
    length = value.length;
    tX = textfield.style.left + (10 * (length + 1));
    tY = textfield.style.top;
    lastChar = value.substr(length - 1);
    var char = document.createElement("char");    
    
    char.innerHTML = lastChar;
    char.style.left = getRandom(0, 1920) + "px";
    char.style.color = "aqua"  
    char.style.position = "absolute"; 
    
    document.body.appendChild(char);
    
    var op = 1.0;
    var pos = 170;
    var id = setInterval(frame, 1);
    var exitPos = 800;
    function frame() {
        if (pos == exitPos) {
            document.body.removeChild(char);
            clearInterval(id);
        } else {
            pos++;
            char.style.top = pos + 'px';
            clone.style.top = pos + 'px';
            if (pos % 2 == 0) {
               // char.style.opacity = op;
                op -= 0.1;
            }
        }
    }
       
       function getRandom(min, max) {
    return Math.floor((Math.random() * max) + min)    
}
}

