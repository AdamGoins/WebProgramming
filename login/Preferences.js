
const PARSING_TOKEN = "!"


var preferences = {};

window.onload = loadPreferences();

function loadPreferences() 
{

    console.log("Prefs");
    var prefs = document.createElement('prefs');
    prefs.id = 'prefs';
    prefs.style.display = 'none';
    document.body.appendChild(iframe);
    prefs.src = 'preferences/Preferences.pref';
    setTimeout(function(){
        var data = document.getElementById('pref').contentDocument.body.firstChild.innerHTML;
        alert(data);
        
        var dataArray = data.split(PARSING_TOKEN);
        var key = dataArray[0];
        var value = dataArray[1];
        
        preferences[key] = value;
    }, 1000);
}


function getPref(key)
{
    return preferences[key];
}

function getPreferences()
{
    return preferences;
}
