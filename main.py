from main_clavier import operation, coffre
from servo_moteur import lock, unlock
from main_led import clignotement_rouge, clignotement_vert
from RFID import do_read
close = True 

while True :
    print("Ok")
    if close :
        if do_read() :
            print("badge accepter")
            clignotement_vert()
            if operation("159D"):
                clignotement_vert()
                unlock()
                print("GG")
                close = False
            else :
                clignotement_rouge()
                print("Ho snap")
        else :
            clignotement_rouge()
            print("Ho snap")
              
    else :
        print("unlock")
        coffre()
        clignotement_vert()
        print("locked")
        close = True
    
        

