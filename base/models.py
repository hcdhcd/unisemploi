from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

class AdminCheck(models.Model):
	check = models.BooleanField(default=False)
	date_check = models.DateTimeField(blank=True, null=True)
	checked_by = models.ForeignKey('utilisateurs.Volontaire', on_delete=models.CASCADE, blank=True, null=True)


	class Meta:
		abstract = True


class Message(AdminCheck):
	titre = models.CharField(max_length=80)
	contenu = models.TextField()
	lu = models.BooleanField(default=False)



