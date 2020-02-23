from django.shortcuts import render
from repertoire.models import Metier




def annuaire(request):

	metiers = Metier.objects.all()


	for metier in metiers:
		if not metier.contact_set.all():
			metiers=metiers.exclude(pk=metier.pk)


	return render(request, 'repertoire.html', {'metiers' : metiers})


