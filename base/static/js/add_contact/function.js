alert('function');

// permet de renseigner un attribut onclick a un element html//
function setOnclick(node, onclickValue){
	if(typeof node === 'string'){node=document.querySelector(node);}
	node.setAttribute('onclick', onclickValue);
}

//permet de renseigner un attribut onclick a plusieurs el html. Peut permettre de leur definir un id incrémenté//
function setManyOnclick(css, onclickValue, id=0){
	var n = 0;
	var liste=querySelectorAll(css);
	for (var i = 0; i<liste.length; i++) {
		liste[i].setAttribute("onclick", onclickValue);

	}
}

//plop//
function insertBeforeNCopies(n, original, node) {
	for(var i = 0; i < n; i++) {
		var clone = original.cloneNode(true);
		var parent = node.parentElement;
		parent.insertBefore(clone, node);
	}
}