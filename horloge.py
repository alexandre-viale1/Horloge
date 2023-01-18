#Si on veut l'heure manuelle on appele la fonction horloge_manuelle 
#Si on veut l'heure automatique on appele pas la fonction horloge_manuelle
import time
horloge_active= True
#Fonction qui définie l'horloge manuellement
def horloge_manuelle(heure, minute, seconde):
#Condition pour savoir quelle fonction choisir en manuelle et automatique
    if horloge_active:
        print(" ")
    while True:
        if seconde > 59:
            seconde = 0
            minute += 1
        if minute > 59:
            minute = 0
            heure += 1
        if heure > 23:
            heure = 0
            minute = 0
            seconde = 0
        #définir l'heure de l'alarme de l'heure manuelle
        if heure == 0 and minute == 0 and seconde == 5:
            print("Alarme!")
            time.sleep(1)
        print("{:02d}:{:02d}:{:02d}".format(heure, minute, seconde))
        seconde += 1
        time.sleep(1) 

heure_actuelle = (0, 0, 0)
alarme = ()

def afficher_heure():
#Suite pour savoir quelle fonction choisir entre manuelle et automatique
    global horloge_active
    horloge_active = False
    print(" ")
#Affiche l'heure actuelle sous la forme hh:mm:ss
    heures, minutes, secondes = heure_actuelle
    print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

def regler_alarme(nouvelle_alarme):
    global alarme
    alarme = nouvelle_alarme

while True:
    afficher_heure()
    if heure_actuelle == alarme:
        print("Alarme!")
    time.sleep(1)
    heure_actuelle = time.localtime()[3:6]
    #définir l'heure de l'alarme automatique
    alarme = (0, 0, 0)
    #Appeler la fonction horloge_manuelle ici # 
    horloge_manuelle(15, 30, 30)              #
###############################################