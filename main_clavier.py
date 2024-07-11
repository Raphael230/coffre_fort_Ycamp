# Objet du script : mise en œuvre d'un clavier matriciel 4x4.
# Matériel requis (en plus de la NUCLEO-WB55) : un clavier matriciel 4x4 et, 
# bien sûr, des câbles pour le connecter à la NUCLEO-WB55...

#-----------------------------------------------------------------

from keypad import Keypad4x4 # Bibliothèque pour gérer le clavier
from main_led import clignotement_jaune

keyboard = Keypad4x4() # Instanciation du clavier



def operation(mdp) :
    while True:
        OSS = ""
	    #print(key) # Affichage de la touche appuyée
        for x in range(len(mdp)):  # len(mdp) veut dire qu'il renverra autant de caractère qu'il y a dans mdp 
            key = keyboard.read_key() # Lecture de la touche appuyée
            clignotement_jaune()
            OSS += str(key)
            print(OSS)

        return mdp == OSS # boolean 

        



    
            