function DiceJS() {

	// setup Dice on click to roll
	var SetsOfDice = document.getElementsByClassName("dice"); 
	for (var i = 0;i < SetsOfDice.length;i++){
		SetsOfDice[i].onclick = function() { 
			var die = this.className;
			var dieClasses = die.split(' ');
			var diceType = dieClasses[1];
			var diceSides = diceType.substring(1);
			var rolled = Math.floor((Math.random() * diceSides) + 1);
            // alert('Roll ' + rolled); 
            this.innerHTML = rolled;
        };
	}

	// Sets of RollAll buttons
	var SetsOfRollAll = document.getElementsByClassName("RollAll");
	for (var i = 0;i < SetsOfRollAll.length;i++){
		SetsOfRollAll[i].onclick = function() { 
			var rollAllButtons = this.className;
			var dieClasses = rollAllButtons.split(' ');
			var diceType = dieClasses[1];
			var diceSides = diceType.substring(1);
			// console.log(".dice " + diceType + " col-sm-1");
			var die = document.getElementsByClassName("dice " + diceType);
			for (var j = 0;j < die.length;j++){
				die[j].click();
			}
        };
	}	

}

window.onload = function() {
  	window.DiceJS = new DiceJS();
};