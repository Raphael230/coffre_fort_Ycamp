from main_clavier import operation
from servo_moteur import lock, unlock


while True :
    print("Ok")
    if operation("159D"):
        unlock()
    else :
        lock()
    

