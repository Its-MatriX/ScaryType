from keyboard import add_hotkey, remove_hotkey
from time import sleep
from keyboard import write as _write
from time import sleep
from playsound import playsound
from os.path import split
from random import choice, randint
from os import _exit
from ctypes import windll
from threading import Thread

Thread(target=lambda:windll.user32.MessageBoxW(0, 'Ctrl+Shift+S - Пауза/Продолжить\n' + \
                             'Ctrl+Shift+E - Закрыть', 'ScaryType', 0x40 | 0x10000)).start()

Folder = split(__file__)[0].replace('\\', '/')

State = True


def CurseLetter(Letter):
    CursedChars = (769, 771, 772, 773, 774, 775, 776, 777, 778, 782, 783, 785,
                   786, 789, 791, 793, 794, 796, 799, 800, 801, 802, 803, 804,
                   805, 807, 808, 810, 812, 816, 817, 818, 819, 820, 821, 822,
                   823, 824, 826, 829, 830, 832, 833, 835, 836, 837, 839, 841,
                   842, 844, 846, 850, 852, 853, 854, 855, 857, 859, 860, 861,
                   864)

    ToReturn = ''

    for x in range(randint(0, 3)):
        ToReturn += chr(choice(CursedChars))

    ToReturn += Letter
    return ToReturn


def WriteLetter(Letter):
    _write(CurseLetter(Letter))


def AddHotkeys():
    add_hotkey(',', callback=lambda: WriteLetter('6'), suppress=True)
    add_hotkey('c', callback=lambda: WriteLetter('s'), suppress=True)
    add_hotkey('p', callback=lambda: WriteLetter('z'), suppress=True)
    add_hotkey('x', callback=lambda: WriteLetter('4'), suppress=True)
    add_hotkey('b', callback=lambda: WriteLetter('u'), suppress=True)
    add_hotkey('g', callback=lambda: WriteLetter('n'), suppress=True)
    add_hotkey('d', callback=lambda: WriteLetter('v'), suppress=True)
    add_hotkey('n', callback=lambda: WriteLetter('t'), suppress=True)
    add_hotkey('q', callback=lambda: WriteLetter('j'), suppress=True)
    add_hotkey('l', callback=lambda: WriteLetter('d'), suppress=True)
    add_hotkey('r', callback=lambda: WriteLetter('k'), suppress=True)
    add_hotkey('j', callback=lambda: WriteLetter('0'), suppress=True)

    try:
        add_hotkey('ё', callback=lambda: WriteLetter('ё'), suppress=True)

    except:
        add_hotkey('~', callback=lambda: WriteLetter('ё'), suppress=True)


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
        playsound(Folder + '/state_changed.mp3')

    else:
        playsound(Folder + '/state_changed.mp3')
        AddHotkeys()


AddHotkeys()

add_hotkey('Ctrl+Shift+S', ChangeState, suppress=True)
add_hotkey('Ctrl+Shift+E',
           lambda: playsound(Folder + '/state_changed.mp3') | _exit(0),
           suppress=True)

playsound(Folder + '/state_changed.mp3')

while True:
    sleep(1)
