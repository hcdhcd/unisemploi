alert('var.js');
var field_metier = document.querySelector('.field_metier');
var field_secteur = document.querySelector('.field_secteur');
var add_metierField = document.getElementById('+metier');
var add_secteurField = document.getElementById('+secteur');

var step1 = document.querySelectorAll('.step1');
var step2 = document.querySelectorAll('.step2');
var step3 = document.querySelectorAll('.step3');

var buttonsStep2 = document.querySelector('#buttonsStep2');
var buttonsStep3 = document.querySelector('#buttonsStep3');

var buttonStep1To2 = document.querySelector('#buttonStep1To2');
var buttonStep2To3 = document.querySelector('#buttonStep2To3');
var buttonStep2To1 = document.querySelector('#buttonStep2To1');
var buttonStep3To2 = document.querySelector('#buttonStep3To2');
var form = document.querySelector('form');
var comment = document.querySelector("#comment");
var currentStep = 1;

var titreStep1 = "Ajouter un contact (1/3)";
var commentStep1 = "Selectionnez les secteurs et les metiers de votre contact, si l\'un d\'eux n\'est pas dans la liste, vous pouvez le saisir directement.";
var titreStep2 = "Ajouter un contact (2/3)";
var commentStep2 = "Associez les secteurs aux metiers.";
var titreStep3 = "Ajouter un contact (3/3)";
var commentStep3 = "";
alert(comment.innerHTML)



