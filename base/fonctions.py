
def ListRepeatRemover(x):
  return list(dict.fromkeys(x))

def ListEmptyRemover(liste):
	liste = list(filter(None, liste)) 

