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
			var die = document.getElementsByClassName("dice " + diceType);
			for (var j = 0;j < die.length;j++){
				die[j].click();
			}
        };
	}

	// Sets of Add buttons
	var SetsOfAdd = document.getElementsByClassName("Add");
	for (var i = 0;i < SetsOfAdd.length;i++){
		SetsOfAdd[i].onclick = function() { 
			var AddButtons = this.className;
			var dieClasses = AddButtons.split(' ');
			var diceType = dieClasses[1];
			var diceSides = diceType.substring(1);
			var diceBox = document.getElementById(diceType + "Box");
			var dices = diceBox.getElementsByClassName("dice");
			if (dices.length == 6){
				alert("You cannot have more than 6 of " + diceType + " dice.");
			} else {
				var btn = document.createElement("BUTTON");
				btn.className = "dice " + diceType + " col-sm-1";
				btn.innerHTML = diceType;
				btn.onclick = function() { 
					var die = this.className;
					var dieClasses = die.split(' ');
					var diceType = dieClasses[1];
					var diceSides = diceType.substring(1);
					var rolled = Math.floor((Math.random() * diceSides) + 1);
		            // alert('Roll ' + rolled); 
		            this.innerHTML = rolled;
		        };
				diceBox.appendChild(btn);
			}
        };
	}

	// Sets of Remove buttons
	var SetsOfRemove = document.getElementsByClassName("Remove");
	for (var i = 0;i < SetsOfRemove.length;i++){
		SetsOfRemove[i].onclick = function() { 
			var RemoveButtons = this.className;
			var dieClasses = RemoveButtons.split(' ');
			var diceType = dieClasses[1];
			var diceSides = diceType.substring(1);
			var diceBox = document.getElementById(diceType + "Box");
			var dices = diceBox.getElementsByClassName("dice");
			if (dices.length == 0){
				alert("You do not have any " + diceType + " dice to remove.");
			} else {
				// dices.lastChild.remove();
				$('#' + diceType + "Box" + ' .dice:last').remove();
			}
        };
	}		

}

window.onload = function() {
  	window.DiceJS = new DiceJS();
};