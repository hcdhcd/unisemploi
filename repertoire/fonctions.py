def dispoupdate (c) :

	print("dispo contact", c.dispo)
	

	print("metier contact ", c.metier.all())
	

	for m in c.metier.all() :

		print ("metier", m)
		

		print( "dispo metier", m.dispo)
		

		check_list=[]




		print("on ajoute a la checklist les dispos non impactées par le contact")

		for dispo_metier in m.dispo : 

			if dispo_metier not in c.dispo :
				print (dispo_metier , " not in " , c)
				check_list.append(dispo_metier)

				

				print("check_list :", check_list)

				


		print("on cherche a ajouter les dispos tjrs presentes dans les autres contacts")

		for dispo_contact in c.dispo :

			print("liste des contacts associés au metier", m.contact_set.all() )
			

			print("liste des contacts ayant la même dispo", m.contact_set.filter(dispo__contains=dispo_contact) )

			
			print("id du contact =" , c.id )

			print("liste des contacts ayant la meme dispo en excluant = " , c, ": ", m.contact_set.filter(dispo__contains=dispo_contact).exclude(id=c.id))
			


			if m.contact_set.filter(dispo__contains=dispo_contact).exclude(id=c.id) :
				print("liste des contacts ayant la meme dispo not null")
				check_list.append(dispo_contact)

				print("check_list actualisée", check_list)

		m.dispo=check_list
		m.save()


def add_dispo_metier(c,m):

	"""add dispo metier """
	check_list=c.dispo

	for dispo_contact in c.dispo:
			

		if dispo_contact not in m.dispo :
			print(dispo_contact)
			check_list.append(dispo_contact)

	m.dispo=check_list
	m.save()
	"""fin add dispo metier"""


def add_dispo_secteur(m,s):

	"""add dispo secteur"""
	check_list=m.dispo

	for dispo_metier in m.dispo:
		if dispo_metier not in s.dispo :
			check_list.append(dispo_metier)

	s.dispo=check_list
	s.save()

	"""fin add dispo secteur """



def remove_dispo_metier(c,m):
	"""remove dispo metier"""
	check_list=[]


	for dispo_metier in m.dispo : 

		if dispo_metier not in c.dispo :
			check_list.append(dispo_metier)


	for dispo_contact in c.dispo :


		if m.contact_set.filter(dispo__contains=dispo_contact).exclude(id=c.id) :
			check_list.append(dispo_contact)

	m.dispo=check_list
	m.save()
	"""fin remove dispo metier"""


def remove_dispo_secteur(m,s):



	check_list=[]

	for dispo_secteur in s.dispo :
		if dispo_secteur not in m.dispo :
			check_list.append(dispo_secteur)

	for dispo_metier in m.dispo :

		if s.metier_set.filter(dispo__contains=dispo_metier).exclude(id=m.id) :
			check_list.append(dispo_metier)

	s.dispo=check_list
	s.save()





def test(c):
	print("go")

	for m in c.metier.all():




		check_list=c.dispo

		for dispo_contact in c.dispo:
			

			if dispo_contact not in m.dispo :
				print(dispo_contact)
				check_list.append(dispo_contact)


				print(check_list)

		m.dispo=check_list
		m.save()




"""

	check_list=[]


	for dispo_metier in m.dispo : 

		if dispo_metier not in c.dispo :
			check_list.append(dispo_metier)


	for dispo_contact in c.dispo :


		if m.contact_set.filter(dispo__contains=dispo_contact).exclude(id=c.id) :
			check_list.append(dispo_contact)

	m.dispo=check_list
	m.save()




	for s in m.secteur.all() :





		check_list=m.dispo

		for dispo_metier in m.dispo:
			if dispo_metier not in s.dispo :
				check_list.append(dispo_metier)

		s.dispo=check_list
		s.save()





		check_list=[]

		for dispo_secteur in s.dispo :
			if dispo_secteur not in m.dispo :
				check_list.append(dispo_secteur)

		for dispo_metier in m.dispo :

			if s.metier_set.filter(dispo__contains=dispo_metier).exclude(id=m.id) :
				check_list.append(dispo_metier)

		s.dispo=check_list
		s.save()

"""