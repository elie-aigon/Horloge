import time


def horloge(heure_actu):
    sec = heure_actu[2]
    minute = heure_actu[1]
    heure = heure_actu[0]

    mode = input('mode 24 ou 12: ')
    if mode == "24":
        while True:
            if sec < 59:
                sec += 1

            elif minute < 59:
                sec = 00
                minute += 1
            elif heure < 23:
                sec = 00
                minute = 00
                heure += 1
            else:
                sec = 00
                minute = 00
                heure = 00
            time.sleep(1)
            temps = (heure, minute, sec)
            print(temps)
            if minute == 30 and sec == 0:
                set_alarm(temps)
                set_heure()

    elif mode == "12":
        if heure > 11:
            am_pm = "PM"
        else:
            am_pm = "AM"
        while True:
            if heure > 11:
                heure = heure - 12
            if sec < 59:
                sec += 1

            elif minute < 59:
                sec = 00
                minute += 1

            elif heure < 11:
                sec = 00
                minute = 00
                heure += 1
            else:
                sec = 00
                minute = 00
                heure = 00

            if heure % 12 == 0:
                if am_pm == "PM":
                    am_pm = "AM"
                else:
                    am_pm = "PM"

            time.sleep(1)
            temps = (heure, minute, sec, am_pm)
            print(temps)
            if minute == 30 and sec == 0:
                set_alarm(temps)
                set_heure()

def input_tuple():
    new_tuple = input('Entrez des entiers séparés par des virgules qui seront de la forme : hh, mm, ss : ')
    return new_tuple
def set_heure():
    modif = input('Voulez vous modifier l heure actuelle? Y/N : ')
    if modif.lower() == "y":
        new_temps_input = input('Entrez des entiers séparés par des virgules qui seront de la forme : hh, mm, ss : ')
        new_temps = tuple(map(int, new_temps_input.split(',')))
        horloge(new_temps)
def set_alarm(temps):
    modif = input('Voulez vous ajouter une alarme? Y/N : ')
    if modif.lower() == "y":

        alarm = input_tuple()
    return alarm
def check_alarm(alarm, temps):
    if alarm == temps:
        print("Réveille toi bouffon!")


heure_actu = (10, 29, 55)


horloge(heure_actu)