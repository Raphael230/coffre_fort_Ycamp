# Objet du code : 
# Version MicroPyhton du programme "Blink".
# Fait clignoter une LED (éventuellement infrarouge) à une fréquence programmable.
# Nécessite une LED externe à la carte (module Grove par exemple).

from machine import Pin # Classe pour gérer les broches GPIO
from time import sleep_ms # Classe pour temporiser

vert = Pin(23,  mode=Pin.OUT)
rouge = Pin(19, mode=Pin.OUT)
jaune = Pin(21, mode=Pin.OUT)

def clignotement_vert ():
	vert.on()
	sleep_ms(500) # Pose 0.5 seconde
	vert.off()
	sleep_ms(1500)

def clignotement_rouge():
	rouge.on()
	sleep_ms(500) # Pose 0.5 seconde
	rouge.off()
	sleep_ms(1500)

def clignotement_jaune():
	jaune.on()
	sleep_ms(500) # Pose 0.5 seconde
	jaune.off()
	sleep_ms(500)


	