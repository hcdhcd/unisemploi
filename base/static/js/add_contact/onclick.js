alert('start set onclick');
setOnclick(buttonStep1To2, "test();");
setOnclick(buttonStep2To3, "step2To3();");
setOnclick(buttonStep2To1, "step2To1();");
setOnclick(buttonStep3To2, "step3To2();");
setOnclick(add_metierField, 'insertBeforeNCopies(1, field_metier, add_metierField);');/*button add metier et add metier field*/
setOnclick(add_secteurField, 'insertBeforeNCopies(1, field_secteur, add_secteurField);');/*nom changes*/
setManyOnclick(".delete", "deleteNode(this.parentNode);");

function setOnclick2(){
	;
}

alert('end setoclick');


/*		
		var button_add_metier = document.getElementById('+metier');
		button_add_metier.setAttribute('onclick', 'insertBeforeNCopies(1, field_metier, button_add_metier);');*/

/*		var button_add_secteur = document.getElementById('+secteur');
		button_add_secteur.setAttribute('onclick', 'insertBeforeNCopies(1, field_secteur, button_add_secteur);');
*/
/*		var button_delete = document.querySelectorAll('.delete');
		var n=0;
		for (const element of button_delete) {
			element.setAttribute("onclick", "deleteNode(this.parentNode);");
			element.id=n.toString();
			n+=1;
		}
*/
