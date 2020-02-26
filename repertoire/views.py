from django.shortcuts import render
from repertoire.models import Metier




def annuaire(request):

	metiers = Metier.objects.all()


	for metier in metiers:
		if not metier.contact_set.all():
			metiers=metiers.exclude(pk=metier.pk)


	return render(request, 'repertoire.html', {'metiers' : metiers})


def detailContact(request, pk):
	contacts=Metier.objects.get(pk=pk).contact_set.all()

	return render(request, 'detailContact.html', {'contacts' : contacts})


