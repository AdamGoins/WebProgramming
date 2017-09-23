var lastChar = "";
var lastDiv;
    
    function startFalling(character) {
        
        
        var char;
        var clone;
        
        var posLeft;
        var color = "aqua";
        var positionType = "absolute";
        var opacity = 555;
        var posTop = 170;
        var intervalId = setInterval(frame, 3);
        var exitPos = 600;
        
        if (character == lastChar) 
        {
            char = lastDiv.cloneNode(true);
            posLeft = lastDiv.style.left + "px";
        }
        else
        {
            char = document.createElement("char");  
            posLeft = getRandom(0, 1920) + "px";
        }  
        
        char.innerHTML = character;
        char.style.left = posLeft;
        char.style.color = color;  
        char.style.position = positionType;
        
        clone = char.cloneNode(true);
        clone.style.color = "red";
        
        document.body.appendChild(char);
        document.body.appendChild(clone);
        
        function frame() {
            if (posTop == exitPos) {
                document.body.removeChild(char);
                if (clone) document.body.removeChild(clone);
                clearInterval(intervalId);
            } else {
                posTop++;
                char.style.top = posTop + 'px';
                clone.style.top = posTop + 'px';
                if (posTop % 20 == 0) {
                    char.style.opacity = opacity;
                    opacity-= 0.1;
                }
                if (posTop % 10 == 0) {
                    clone.style.opacity = clone.style.opacity - 0.05;
                }
            }
        }
        lastChar = character;
        lastDiv = char;
    }
    
    function createFallingChar(char) {
     
        //var keycode = e.keycode;
        //var char = getChar(keycode);
        startFalling(char);
    }
    
    function getChar(keyCode)
    {
        var chrCode = keyCode - 48 * Math.floor(keyCode / 48);
        var char = String.fromCharCode((96 <= keyCode) ? chrCode: keyCode);
        return char;
    }
  
    /**
    function createFallingChar(textfield) {
     
        var value = textfield.value;
        var char = String(value).substring(value.length - 1);
        
        startFalling(char);
        
    }
    **/
