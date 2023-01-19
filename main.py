import time
import keyboard

def input_tuple():
    string = input('Entrez des entiers tel que : hh mm ss : ')
    string_tuple = tuple(string.split())
    sec = int(string_tuple[2])
    minute = int(string_tuple[1])
    heure = int(string_tuple[0])
    new_tuple = (heure, minute, sec)

    return new_tuple

def input_tuple_us():
    string = input('Entrez des entiers tel que : hh mm ss XX ou XX représente am ou pm: ')
    string_tuple = tuple(string.split())
    sec = int(string_tuple[2])
    minute = int(string_tuple[1])
    heure = int(string_tuple[0])
    am_pm = string_tuple[3]
    new_tuple = (heure, minute, sec, am_pm)

    return new_tuple
def set_heure():
    modif = input('Voulez vous modifier l heure actuelle? Y/N : ')
    if modif.lower() == "y":
        horloge(input_tuple())
def check_alarm(random_tuple, temps):
    if random_tuple == temps:
        print('aaaaaaaaaaaa')

def pause():
    print('Pause, appuyer sur - a - pour repartir')
    while True:
        if keyboard.is_pressed('a'):
            break
        pass

def horloge(random_tuple):

    sec = int(random_tuple[2])
    minute = int(random_tuple[1])
    heure = int(random_tuple[0])


    mode = input('mode 24 ou 12: ')
    if mode == "24":
        alarme_yesno = input('Voulez vous set une arlame? Y/N: ')
        if alarme_yesno.lower() == 'y':
            print('Alarme:  ')
            alarm_tuple = input_tuple()
        else:
            alarm_tuple = 0
        print('maintenez - p - pour mettre pause')
        while True:
            if keyboard.is_pressed('p'):
                pause()
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
            print(heure, ':', minute, ':', sec)
            check_alarm(alarm_tuple, temps)
            if minute == 30 and sec == 0:
                set_heure()
    elif mode == "12":
        alarme_yesno = input('Voulez vous set une arlame? Y/N: ')
        if alarme_yesno.lower() == 'y':
            print('Alarme:  ')
            alarm_tuple = (input_tuple_us())
        else:
            alarm_tuple = 0
        if heure > 11:
            am_pm = "PM"
        else:
            am_pm = "AM"
        while True:
            if keyboard.is_pressed('p'):
                pause()
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

            print(heure, ':', minute, ':', sec, '-', am_pm)
            check_alarm(alarm_tuple, temps)
            if minute == 30 and sec == 0:
                set_heure()

horloge(input_tuple())
