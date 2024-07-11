from main_clavier import operation, coffre
from servo_moteur import lock, unlock
from main_led import clignotement_rouge, clignotement_vert

while True :
    print("Ok")
    if operation("159D"):
        clignotement_vert()
        unlock()
        print("GG")
    else :
        clignotement_rouge()
        #lock()
        print("Ho snap")
    
    if operation("CCCC"):
        #coffre()
        clignotement_vert()
        lock()
        print("locked")
    
        

