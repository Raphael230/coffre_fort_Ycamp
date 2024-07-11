# Objet du code : 
# Version MicroPyhton du programme "Blink".
# Fait clignoter une LED (éventuellement infrarouge) à une fréquence programmable.
# Nécessite une LED externe à la carte (module Grove par exemple).

from machine import Pin # Classe pour gérer les broches GPIO
from time import sleep_ms # Classe pour temporiser

# La LED est assignéeà la broche D4
vert = Pin(23,  mode=Pin.OUT)
rouge = Pin(21, mode=Pin.OUT)
jaune = Pin(19, mode=Pin.OUT)

# while True :
# 	sleep_ms(500) # Pose 0.5 seconde
# 	led.off()
# 	print("LED éteinte")
# 	sleep_ms(500) # Pause 0.5 seconde
# 	led.on() 
# 	print("LED allumée")


def clignotement_vert ():
	vert.on()
	sleep_ms(500) # Pose 0.5 seconde
	vert.off()
	sleep_ms(500)
	print("NICE")

def clignotement_rouge():
	rouge.on()
	sleep_ms(500) # Pose 0.5 seconde
	rouge.off()
	sleep_ms(500)
	print("ERROR")

def clignotement_jaune():
	jaune.on()
	sleep_ms(500) # Pose 0.5 seconde
	jaune.off()
	sleep_ms(500)


	