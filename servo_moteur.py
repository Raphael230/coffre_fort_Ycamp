# premier exemple d'utilisation 

# from machine import Pin,PWM
# import time

# sg90 = PWM(Pin(22, mode=Pin.OUT))
# sg90.freq(50)

# # 0.5ms/20ms = 0.025 = 2.5% duty cycle
# # 2.4ms/20ms = 0.12 = 12% duty cycle

# # 0.025*1024=25.6
# # 0.12*1024=122.88

# while True:
#     sg90.duty(26)
#     time.sleep(1)
#     sg90.duty(123)
#     time.sleep(1)

#-------------------------------------------------

# Objet du script :
# Piloter un servomoteur
# Exemple de valeurs de PWM pour le servomoteur Grove livré avec les kits 
# de base pour Arduino.

# from time import sleep # Pour temporiser
# import pyb # Pour accéder  aux broches et aux compteurs (timers)

# servo = pyb.Pin('G22')

# Timer_Num = 1 # Numéro du timer
# Timer_Cha = 1 # Canal du timer
# Timer_Freq = 50 # Fréquence du timer (en Hz)

# while True:

# 	print("Servomoteur à 0 degrés")
# 	tim_servo = pyb.Timer(Timer_Num, freq=Timer_Freq) # Démarrage du timer
# 	tim_servo.channel(Timer_Cha, pyb.Timer.PWM, pin=servo, pulse_width_percent=5)	# Servomoteur à 0 degrés
# 	sleep(5) # temporisation de 5 secondes

# 	print("Servomoteur à 90 degrés")
# 	tim_servo = pyb.Timer(Timer_Num, freq=Timer_Freq) # Démarrage du timer
# 	tim_servo.channel(Timer_Cha, pyb.Timer.PWM, pin=servo, pulse_width_percent=2)	# Servomoteur à 90 degrés
# 	sleep(5) # temporisation de 5 secondes
	
# 	print("Servomoteur à -90 degrés")
# 	tim_servo = pyb.Timer(Timer_Num, freq=Timer_Freq) # Démarrage du timer
# 	tim_servo.channel(Timer_Cha, pyb.Timer.PWM, pin=servo, pulse_width_percent=9.5)	# Servomoteur à -90 degrés
# 	sleep(5) # temporisation de 5 secondes

# tim_servo.deinit() # Arrêt du timer

#-------------------------------------------------

from machine import Pin,PWM
import time

def rota () :
    sg90 = PWM(Pin(22, mode=Pin.OUT))
    sg90.freq(50)

    while True:
        sg90.duty(100)
        time.sleep(1)
        sg90.duty(60)
        time.sleep(1)

print(rota())