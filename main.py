from keyboard import add_hotkey, remove_hotkey, write
from time import sleep
from playsound import playsound
from os.path import split
from colorama import Fore

Folder = split(__file__)[0].replace('\\', '/')

State = True

def AddHotkeys():
    add_hotkey(',', callback=lambda: write('6'), suppress=True)
    add_hotkey('c', callback=lambda: write('s'), suppress=True)
    add_hotkey('p', callback=lambda: write('z'), suppress=True)
    add_hotkey('x', callback=lambda: write('4'), suppress=True)
    add_hotkey('b', callback=lambda: write('u'), suppress=True)
    add_hotkey('g', callback=lambda: write('n'), suppress=True)
    add_hotkey('d', callback=lambda: write('v'), suppress=True)
    add_hotkey('n', callback=lambda: write('t'), suppress=True)
    add_hotkey('q', callback=lambda: write('j'), suppress=True)
    add_hotkey('l', callback=lambda: write('d'), suppress=True)
    add_hotkey('r', callback=lambda: write('k'), suppress=True)
    add_hotkey('j', callback=lambda: write('0'), suppress=True)

    try:
        add_hotkey('ё', callback=lambda: write('ё'), suppress=True)

    except:
        add_hotkey('~', callback=lambda: write('ё'), suppress=True)

def RemoveHotkeys():
    remove_hotkey(',')
    remove_hotkey('c')
    remove_hotkey('p')
    remove_hotkey('x')
    remove_hotkey('b')
    remove_hotkey('g')
    remove_hotkey('d')
    remove_hotkey('n')
    remove_hotkey('q')
    remove_hotkey('l')
    remove_hotkey('r')
    remove_hotkey('j')

    try:
        remove_hotkey('ё')

    except:
        remove_hotkey('~')

def ChangeState():
    global State

    State = not State

    if not State:
        RemoveHotkeys()
        print(Fore.RED + 'Поставлено на паузу')
        playsound(Folder + '/state_changed.mp3')

    else:
        print(Fore.CYAN + 'Продолжение работы')
        playsound(Folder + '/state_changed.mp3')
        AddHotkeys()

AddHotkeys()

add_hotkey('Ctrl+Shift+S', ChangeState)
print(Fore.GREEN + 'Программа запущена!')

playsound(Folder + '/state_changed.mp3')

while True:
    sleep(1)
