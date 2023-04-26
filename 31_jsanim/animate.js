// Team Cookielol:: Vanch, Brian Yang
// SoftDev pd07
// K31 -- JSanim
// 2023-04-25


var c = document.getElementById("playground");

var dotButton = document.getElementById("buttonCircle");

var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "cyan";
var requestID;

var radius = 0;
var growing = true;

var clear = (e) => {
    e.clearRect(0, 0, c.width, c.height);
}

var drawDot = () => {
  //window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(drawDot);
  clear(ctx);

  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.fill();


  if(growing){
    if (radius > c.height/2){
      growing = false;
    }
    radius += 1
  }else{
    if (radius == 0){
      growing = true;
    }else{
      radius -= 1;
    }
  }
}

var stopIt = () => {
  console.log("stopIt invoked...");
  console.log(requestID);

  window.cancelAnimationFrame(requestID);
}


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt)
