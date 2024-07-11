# Objet du code : 
# Version MicroPyhton du programme "Blink".
# Fait clignoter une LED (éventuellement infrarouge) à une fréquence programmable.
# Nécessite une LED externe à la carte (module Grove par exemple).

from machine import Pin # Classe pour gérer les broches GPIO
from time import sleep_ms # Classe pour temporiser

# La LED est assignéeà la broche D4
led = Pin(23,  mode=Pin.OUT)

while True :
	sleep_ms(500) # Pose 0.5 seconde
	led.off()
	print("LED éteinte")
	sleep_ms(1000) # Pause 1 seconde
	led.on() 
	print("LED allumée")
