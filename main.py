from main_clavier import operation, coffre
from servo_moteur import lock, unlock
from main_led import clignotement_rouge, clignotement_vert

close = True 

while True :
    print("Ok")

    if close :
        if operation("159D"):
            print(close)
            clignotement_vert()
            unlock()
            print("GG")
            close = False
        else :
            clignotement_rouge()
            #lock()
            print("Ho snap")
          
    else :
        print("unlock")
        coffre()
        clignotement_vert()
        # lock()
        print("locked")
        close = True
    
        

