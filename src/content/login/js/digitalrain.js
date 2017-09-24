

function generateRain(numOfDroplets) 
{
 
    //for (i = 0; i < numOfDroplets; i++) 
    //{
     fall();   
    //}
    
}

function fall() {
    
    
    console.log("Falling");
    
    var dropet = document.createElement("droplet");
    
    var op = 1.0;
    var pos = 0;
    
    var dropletContents = "";
    var dropletLength = getRandom(12, 31);
    var dropletX = getRandom(0, 1920);
    
        
    dropet.style.left = dropletX + "px";
    dropet.style.backgroundColor = "grey";
    dropet.style.color = "red";
    dropet.style.position = "absolute";
    
    document.body.appendChild(dropet);
    
    
    var id = setInterval(frame, 7);
    
    function frame() {
        if (pos == 1000) {
            document.body.removeChild(dropet);
            clearInterval(id);
            fall();
        } else {
            
            pos++;
            
            var currentLength = dropletContents.length;
            
            if (currentLength < dropletLength) 
            {
                dropletContents = growDroplet(dropletContents);
            }
            
            dropet.style.top = pos + 'px';
            dropet.innerHTML = dropletContents;
            
            if (pos % 25 == 0) {
                dropet.style.opacity = op;
                op -= 0.1;
            }
        }
    }
}

function growDroplet(dropletContents) 
{
 
    
    // Roll a random chance to change a character in the droplet. 10% chance
    dropletContents = dropletContents.replace("<font color=\"white\">", "").replace("</font>", "");
    
    dropletContents = insertCharAt(dropletContents, 0, getRandomChar());
    
    if (getRandom(0, 100) <= 10) 
    {
        // Replace a random character in the string.
        dropletContents = replaceCharAt(dropletContents, getRandom(0, dropletContents.length), getRandomChar());
    }
    
    
    var whiteCharString = "<font color=\"white\">"; 

    dropletContents = insertCharAt(dropletContents, dropletContents.length - 1, whiteCharString);
    dropletContents = dropletContents + "</font>";
    
    console.log("Contents: " + dropletContents);
    return dropletContents;
    
}
function replaceCharAt(str, index, char) {
    if(index > str.length-1) return str;
    str = String(str);
    return str.substring(0, index) + char + str.substring(index+1);
}

function insertCharAt(str, index, char) {
    if(index > str.length-1) return str;
    str = String(str);
    var x = str.substring(0, index) + char + str.substring(index);
    return x;
}

function getRandom(min, max) {
    return Math.floor((Math.random() * max) + min);
}


function getRandomChar() {

    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=@#$%^&*()_+{}:<>?[]\;',./"
    
    return chars.charAt(getRandom(0, chars.length)) + "\n";
}



































