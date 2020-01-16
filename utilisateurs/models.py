from django.db import models


class Volontaire(models.Model):
	est_unis = models.BooleanField(default=False)

	prenom = models.CharField(max_length=30)
	nom = models.CharField(max_length=30)
	
	tel = models.CharField(max_length=10, blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)



	class Meta:
		verbose_name = "Volontaire"
	
	def __str__(self):

		return "{0} {1}".format(self.prenom, self.nom)