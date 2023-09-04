var sec = localStorage.getItem("sec");
var min = localStorage.getItem("min");
var hrs = localStorage.getItem("hrs");

function tick(){
    sec++;
    if (sec >= 60) {
        sec = 0;
        min++;
        if (min >= 60) {
            min = 0;
            hrs++;
        }
    }
}

function write(){
    let hours = (hrs < 10 )? '0' + hrs : hrs,
    minutes = (min < 10)? '0' + min : min,
    seconds = (sec < 10)? '0' + sec : sec;
    try{
        document.getElementById('clock').innerHTML = 'Время сессии: ' + hours + ':' + minutes + ':' + seconds;
    }
    catch(err){
       ;   
    }
    finally{
        localStorage.setItem("sec", sec)
        localStorage.setItem("min", min)
        localStorage.setItem("hrs", hrs)
        tick()
        setTimeout(write, 1000)
    }
}
write()
