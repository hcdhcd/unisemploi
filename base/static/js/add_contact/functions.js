alert('functions');
// permet de renseigner un attribut onclick a un element html
function setOnclick(node, onclickValue){
	if(typeof node === 'string'){node=document.querySelector(node);}
	node.setAttribute('onclick', onclickValue);
}

//permet de renseigner un attribut onclick a plusieurs el html. Peut permettre de leur definir un id incrémenté
function setManyOnclick(css, onclickValue, id=0){
	var n=0;
	var list=document.querySelectorAll(css);
	for (const element of list) {
		element.setAttribute("onclick", onclickValue);
		if (id===0){;}else {
			element.id=id + n.toString();
			n+=1;
		}
	}
}

//
function insertBeforeNCopies(n, original, node) {
for(var i = 0; i < n; i++) {
	var clone = original.cloneNode(true);
	var parent = node.parentElement;
	parent.insertBefore(clone, node);
	}
}

function deleteNode(node){
	node.parentNode.removeChild(node);
}


// step to step
function test(){
	alert("test as been called");
	var metiers_list = document.querySelectorAll("#metier_div ul input");
	alert(metiers_list);
	for (const element of metiers_list){
		if (element.value == 1){
			alert(element.value);
		} 
	}
}

function step1To2(){
	if (currentStep != 1){
		alert("Sois il y a triche sois il y a bug");
	}else{
		for(const element of step1){
			element.classList.add("hidden");
		}
		for(const element of step2){
			element.classList.remove("hidden");
		}
		form.classList.replace("double", "simple");
		buttonStep1To2.classList.add("none");
		buttonsStep2.classList.remove("none");

		titre.innerHTML=titreStep2;
		comment.innerHTML=commentStep2;

		currentStep=2;
	}
	/*	recuperer les valeurs


		verifier les valeurs
	*/
}

function step2To3(){
	if (currentStep != 2){
		alert("Sois il y a triche sois il y a bug");
	}else{
		for(const element of step2){
			element.classList.add("hidden");
		}
		for(const element of step3){
			element.classList.remove("hidden");
		}
		form.classList.replace("simple", "double");
		buttonsStep2.classList.add("none");
		buttonsStep3.classList.remove("none");


		titre.innerHTML=titreStep3;
		comment.innerHTML=commentStep3;

		currentStep=3;
		}
}

function step3To2(){
	if (currentStep != 3){
		alert("Sois il y a triche sois il y a bug");
	}else{
		for(const element of step3){
			element.classList.add("hidden");
		}
		for(const element of step2){
			element.classList.remove("hidden");
		}
		form.classList.replace("double", "simple");
		buttonsStep3.classList.add("none");
		buttonsStep2.classList.remove("none");

		titre.innerHTML=titreStep2;
		comment.innerHTML=commentStep2;

		currentStep=2;
	}
}

function step2To1(){
		if (currentStep != 2){
		alert("Soit il y a triche soit il y a bug");
	}else{
		for(const element of step2){
			element.classList.add("hidden");
		}
		for(const element of step1){
			element.classList.remove("hidden");
		}
		form.classList.replace("simple", "double");
		buttonsStep2.classList.add("none");
		buttonStep1To2.classList.remove("none");

		titre.innerHTML=titreStep1;
		comment.innerHTML=commentStep1;

		currentStep = 1;
	}
}