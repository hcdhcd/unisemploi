from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField


class Message(models.Model):
	titre = models.CharField(max_length=80)
	contenu = models.TextField()
	lu = models.BooleanField(default=False)
	traite = models.BooleanField(default=False)


class AddContact(models.Model):

	Dispo_Choices = [
		('irl', 'personne'),
		('tel', 'téléphone'),
		('mail', 'e-mail'),
		]

	dispo = MultiSelectField(choices=Dispo_Choices, blank=False, null=False)

	GROUPE_CHOICES = [
		
		('01', 'Connectés/Emploi'),
		('02', 'JCN/Chèque Energie'),
		('03', 'Colomiers'),
		('04', 'Cinéma et citoyenneté'),
		('na', 'N\'appartient pas à Unis-Cité'),
	]

	prenomV = models.CharField(max_length=30)
	nomV = models.CharField(max_length=30)
	groupeV = models.CharField(max_length=2, choices=GROUPE_CHOICES, default='01' )

	vol_visible = models.BooleanField(default=False)
	
	telV = models.CharField(max_length=10, blank=True, null=True)
	mailV = models.EmailField(blank=True, null=True)

	prenom = models.CharField(max_length=42)
	nom = models.CharField(max_length=42)

	metier0 = models.CharField(max_length=30)
	secteur0 = models.CharField(max_length=30)
	metier1 = models.CharField(max_length=30, blank=True, null=True)
	secteur1 = models.CharField(max_length=30, blank=True, null=True)
	metier2 = models.CharField(max_length=30, blank=True, null=True)
	secteur2 = models.CharField(max_length=30, blank=True, null=True)
	metier3 = models.CharField(max_length=30, blank=True, null=True)
	secteur3 = models.CharField(max_length=30, blank=True, null=True)
	metier4 = models.CharField(max_length=30, blank=True, null=True)
	secteur4 = models.CharField(max_length=30, blank=True, null=True)
	
	tel = models.CharField(max_length=10, blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)
	ville = models.CharField(max_length=84, blank=True, null=True)

	date = models.DateTimeField(default=timezone.now, 
								verbose_name="Date de parution")

	

	class Meta:
		verbose_name = "AddContact"
	
	def __str__(self):

		return "{0} {1}".format(self.prenom, self.nom)

