"""module multipli contenant la fonction table"""
import os

def table(nb, max=10):
	"""Fonction affichant la table de multiplication par nb de
	1 * nb jusqu'à max * nb"""
	
	for i in range(max) :
		ch = i + 1
		mult = ch * nb
		print(ch , "*" , nb , "=" ,mult)
	# test de la fonction 

if __name__ == "__main__":
	table(int(input('Entrez un nombre a multiplier  : ')))
	os.system("pause")