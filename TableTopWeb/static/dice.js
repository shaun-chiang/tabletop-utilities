function DiceJS() {
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
}

window.onload = function() {
  	window.DiceJS = new DiceJS();
};