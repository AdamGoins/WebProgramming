
    
    function startFalling(character) {
    var char = document.createElement("char");    
    
    char.innerHTML = character;
    char.style.left = getRandom(0, 1920) + "px";
    char.style.color = "aqua"  
    char.style.position = "absolute";
    
    document.body.appendChild(char);
    
    var op = 1.0;
    var pos = 170;
    var id = setInterval(frame, 10);
    var exitPos = 600;
    
    function frame() {
        if (pos == exitPos) {
            document.body.removeChild(char);
            clearInterval(id);
        } else {
            pos++;
            char.style.top = pos + 'px';
            
             if (pos % 25 == 0) {
                char.style.opacity = op;
                op -= 0.1;
            }
        }
    }
    }
    
  
    
    function createFallingChar(textfield) {
     
        var value = textfield.value;
        var char = String(value).substring(value.length - 1);
        
        startFalling(char);
        
    }
    
