		//ajouter tous les onclick depuis le javascript permet de mettre le js a part et certainement de simplifier les problemes de sécurite//

		//definition des liens onclick//
		var button_valider = document.querySelector('#button_valider');
		button_valider.setAttribute("onclick", "window.location.href='{% url 'step1' %}';");

			
		var button_add_metier = document.getElementById('+metier');
		button_add_metier.setAttribute('onclick', 'insertBeforeNCopies(1, field_metier, button_add_metier);');

		var button_add_secteur = document.getElementById('+secteur');
		button_add_secteur.setAttribute('onclick', 'insertBeforeNCopies(1, field_secteur, button_add_secteur);');

		var button_delete = document.querySelectorAll('.delete');
		var n=0;
		for (const element of button_delete) {
			element.setAttribute("onclick", "deleteNode(this.parentNode);;");
			element.id=n.toString();
			n+=1;
		}

		//permet d'animer les boutons ajouter //
		var field_metier = document.querySelector('.field_metier');
		var field_secteur = document.querySelector('.field_secteur');

		function insertBeforeNCopies(n, original, node) {
			for(var i = 0; i < n; i++) {
				var clone = original.cloneNode(true);
				var parent = node.parentElement;
				parent.insertBefore(clone, node);
			}
			//Permet d'animer les bouttons supprimer nouvellement crées//
			//Mais ya pas besoin car déja defini avant ??//
			button_delete = document.querySelectorAll('.delete');
			n=0;
			for (const element of button_delete) {
				element.setAttribute("onclick", "deleteNode(this.parentNode);");
				element.id=n.toString();
				n+=1;

			}
		}

		//animer les boutons supprimer//
		function deleteNode(node){
			node.parentNode.removeChild(node);
		}


		//permet de stocker les valeurs de champ dans un input hidden a envoyer a la vue par post)
		
		function multipleValuesToListInput(data_class, output_id){
			inputs = document.querySelectorAll('.field_metier input');
			var values_list=[];
			for(let i=0; i<inputs.length; i++){
				values_list.push(input_newMetier[i].value);
				alert(values_list[i]);
			}
			var output = document.createElement('input');
			output.value=values_list.join();
			output.setAttribute("id", "output_id");
			alert(output.value);
			var form = document.querySelector('form');
		}

		 alert(values_NewMetier.value);