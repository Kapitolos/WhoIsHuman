
function sendguess() {
  console.log("function fired");
  var isselected = document.getElementsByClassName("cardselect");
  document.getElementById('hiddenField').value = isselected[0].value;
  document.getElementById("guessform").submit();
  console.log(isselected[0]);
  console.log(isselected[1]);
  }


function cardselect() {
    document.getElementById("card").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card");
}



function cardselect2() {
    document.getElementById("card2").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card2");
}

function cardselect3() {
    document.getElementById("card3").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card3");
}

function cardselect4() {
    document.getElementById("card4").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card4");
}

function cardselect5() {
    document.getElementById("card5").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card5");
}

function cardselect6() {
    document.getElementById("card6").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card6");
}

function cardselect7() {
    document.getElementById("card7").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card7");
}

function cardselect8() {
    document.getElementById("card8").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card8");
}

function cardselect9() {
    document.getElementById("card9").id = ("cardisolate");
    var x, i;
    x = document.querySelectorAll(".cardselect");
    for (i = 0; i < x.length; i++) {
      x[i].className = "card";
    }
    document.getElementById("cardisolate").classList.add("cardselect");
    document.getElementById("cardisolate").classList.remove("card");
    document.getElementById("cardisolate").id = ("card9");
}



// target the parent of the cards and remove the card children. Then scramble the cards in an array and append the children back.

function shuffle(sourceArray) {
  for (var i = 0; i < sourceArray.length - 1; i++) {
      var j = i + Math.floor(Math.random() * (sourceArray.length - i));

      var temp = sourceArray[j];
      sourceArray[j] = sourceArray[i];
      sourceArray[i] = temp;
  }
  return sourceArray;
}


function shuffledeck() {
  deck = document.querySelectorAll(".card");
  deckparent = document.getElementById("cardgrid");
  for (i = 0; i < deck.length; i++) {
    deck[i].parentElement.removeChild(deck[i]);
  }
  var mutabledeck = []
  for (i= 0; i < deck.length; i++) {
    mutabledeck.push(deck[i]);
  }
  var randomdeck = shuffle(mutabledeck);
  
  
  for (i = 0; i < randomdeck.length; i++) {
    deckparent.appendChild(randomdeck[i]);}
    console.log("shuffled");
  } 

function loading() 
{
var timeleft = 10;
var downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
  }
  document.getElementById("progressBar").value = 10 - timeleft;
  timeleft -= 1;
}, 1000);
}

function loading2() 
{
var timeleft = 10;
var downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
  }
  document.getElementById("progressBar2").value = 10 - timeleft;
  timeleft -= 1;
}, 1000);
}

function loading3() 
{
var timeleft = 10;
var downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
  }
  document.getElementById("progressBar3").value = 10 - timeleft;
  timeleft -= 1;
}, 1000);
}
  
