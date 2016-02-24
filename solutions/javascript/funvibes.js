var readlineSync = require('readline-sync');

function pickColour(){
  while (1) {
    var colour = readlineSync.question('pick a colour (red, blue, green, or orange): ');
    if (['red', 'blue', 'green', 'orange'].indexOf(colour) >=0 ) {
      console.log("you have selected: " + colour);
      return colour;
    } else {
      console.log("you have not selected a valid colour: " + colour);
    }
  }
}

function pickNumber(){
  while (1){
    var number = readlineSync.question('pick a number (between 1 and 8): ');
    if (['1', '2', '3', '4', '5', '6', '7', '8'].indexOf(number) >= 0) {
      console.log("you have selected: " + number);
      return number;
    } else {
      console.log("you have not selected a valid number: " + number);
    }
  }
}

colour = pickColour();
console.log(colour);
num1 = pickNumber();
console.log(num1);
console.log("And one more...");
num2 = pickNumber();
console.log(num2);

if (colour=="red" && num1 == 1 && num2 == 8) console.log("Be kind.\n");
else if (colour=="blue" && num1 == '2' && num2 == '7') console.log("Be encouraging.\n");
else if (colour=="green" && num1 == '3' && num2 == '6') console.log("Be thoughtful.\n");
else if (colour=="orange" && num1 == '4' && num2 == '5') console.log("Be gentle.\n");
else console.log("Be positive.\n");



