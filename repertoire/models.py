from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from base.models import AdminCheck

"""receiver function"""
import os
import uuid
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _






class Disponibilites(AdminCheck):
	Dispo_Choices = [
		('irl', 'personne'),
		('tel', 'téléphone'),
		('mail', 'e-mail'),
		]

	dispo = MultiSelectField(choices=Dispo_Choices, blank=True, null=True)

	class Meta:
		abstract = True




class Contact(Disponibilites):
	prenom = models.CharField(max_length=42)
	nom = models.CharField(max_length=42)

	metier = models.ManyToManyField('Metier')
	secteur = models.ManyToManyField('Secteur')
	
	tel = models.CharField(max_length=10, blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)
	ville = models.CharField(max_length=84, blank=True, null=True)

	date_pub = models.DateTimeField(default=timezone.now, 
								verbose_name="Date de parution")

	ajoute_par = models.ForeignKey('utilisateurs.Volontaire', related_name="ajoute_par", on_delete=models.CASCADE, null = True)
	vol_visible = models.BooleanField(default=False)


	class Meta:
		verbose_name = "contact"
		ordering=['date_pub',]
	
	def __str__(self):

		return "{0} {1}".format(self.prenom, self.nom)




	def save(self, *args, **kwargs):

		if self.pk:


			c= self
			super(Contact, c).save(*args, **kwargs)

			for m in c.metier.all():


				check_list=[]


				"""je teste tel dans lun des contacts.dispo"""
				if m.contact_set.filter(dispo__contains ='tel'):
					check_list.append('tel')

				if m.contact_set.filter(dispo__contains ='mail'):
					check_list.append('mail')

				if m.contact_set.filter(dispo__contains ='irl'):
					check_list.append('irl')

				m.dispo = check_list
				m.save()

				for s in m.secteur.all():
					check_list=[]


					if s.metier_set.filter(dispo__contains='tel'):
						check_list.append('tel')

					if m.contact_set.filter(dispo__contains ='mail'):
						check_list.append('mail')

					if m.contact_set.filter(dispo__contains ='irl'):
						check_list.append('irl')


					s.dispo=check_list
					s.save()

		else:
			super(Contact, self).save(*args, **kwargs)





	def delete(self, *args, **kwargs):

		c= self

		for m in c.metier.all():

			check_list=[]



			if m.contact_set.filter(dispo__contains ='tel').exclude(pk=c.pk):
				check_list.append('tel')

			if m.contact_set.filter(dispo__contains ='mail').exclude(pk=c.pk):
				check_list.append('mail')

			if m.contact_set.filter(dispo__contains ='irl').exclude(pk=c.pk):
				check_list.append('irl')


			m.dispo = check_list
			m.save()


			for s in m.secteur.all():
				check_list=[]


				if s.metier_set.filter(dispo__contains='tel').exclude(pk=c.pk):

					check_list.append('tel')

				if m.contact_set.filter(dispo__contains ='mail').exclude(pk=c.pk):

					check_list.append('mail')

				if m.contact_set.filter(dispo__contains ='irl').exclude(pk=c.pk):

					check_list.append('irl')



				s.dispo=check_list
				s.save()



		super(Contact, self).delete(*args, **kwargs)






class Metier(Disponibilites):
	metier = models.CharField(max_length=30)
	secteur = models.ManyToManyField('Secteur')

	class Meta:
		ordering=['metier',]
		
	def __str__(self):
		return self.metier


class Secteur(Disponibilites):
	secteur = models.CharField(max_length=60)

	def __str__(self):
		return self.secteur



def maj_contact_dispo_on_creation(sender, instance, **kwargs):

			
	c=instance

	for m in c.metier.all():


		check_list=[]


		"""je teste tel dans lun des contacts.dispo"""
		if m.contact_set.filter(dispo__contains ='tel'):
			check_list.append('tel')

		if m.contact_set.filter(dispo__contains ='mail'):
			check_list.append('mail')

		if m.contact_set.filter(dispo__contains ='irl'):
			check_list.append('irl')

		m.dispo = check_list
		m.save()

		for s in m.secteur.all():
			check_list=[]


			if s.metier_set.filter(dispo__contains='tel'):
				check_list.append('tel')

			if m.contact_set.filter(dispo__contains ='mail'):
				check_list.append('mail')

			if m.contact_set.filter(dispo__contains ='irl'):
				check_list.append('irl')


			s.dispo=check_list
			s.save()


m2m_changed.connect(maj_contact_dispo_on_creation, sender=Contact.metier.through)


class Ressource(AdminCheck):
	titre = models.SlugField()
	fichier = models.FileField(upload_to="ressources/")

	metier= models.ManyToManyField('Metier', blank=True)
	secteur= models.ManyToManyField('Secteur', blank=True)

	date_pub = models.DateTimeField(default=timezone.now, 
								verbose_name="Date de parution")

	vol = models.ForeignKey('utilisateurs.Volontaire', related_name="ressource_ajoute_par", on_delete=models.CASCADE, null = True)

	def extension(self):
		titre, extension = os.path.splitext(self.fichier.titre)

		return extension


@receiver(models.signals.post_delete, sender=Ressource)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.fichier:
        if os.path.isfile(instance.fichier.path):
            os.remove(instance.fichier.path)

class Requete(models.Model):
	metier = models.ManyToManyField('Metier', blank=True)
	secteur = models.ManyToManyField('Secteur', blank=True)
	contact = models.ManyToManyField('Contact', blank=True)

	volontaire = models.ManyToManyField('utilisateurs.Volontaire', blank=False)
	date_pub = models.DateTimeField(default=timezone.now)

	commentaire_vol = models.TextField()

	commentaire_admin = models.TextField(blank=True, null=True)

	ETAPE_CHOICES= [('0', 'non traite'),
					('1', 'rdv pris'),
					('2', 'rdv effectue'),
					('3', 'clôturé'),
						]  

	etape = MultiSelectField(choices=ETAPE_CHOICES, default='0')

	Dispo_Choices = [
		('irl', 'personne'),
		('tel', 'téléphone'),
		('mail', 'e-mail'),
		]

	dispo_vol = MultiSelectField(choices=Dispo_Choices, blank=True, null=True)

