from keyboard import add_hotkey, remove_hotkey
from time import sleep
from keyboard import write as _write, is_pressed
from time import sleep
from playsound import playsound
from os.path import split
from random import choice, randint
from os import _exit
from os import name
from ctypes import windll
import tkinter as tk
from pynput import keyboard
from pyperclip import paste

CurseLevel = 2
IsInput = False


def NumberInput(Default: int = 0, Minimal: int = 1, Maximal: int = 10):
    global IsInput
    IsInput = True

    Window = tk.Tk()
    Window.title("Введите уровень шакализации текста")
    Window.geometry('245x25')

    Window.resizable(False, False)

    def CheckInput():
        global ReturnValue
        ReturnValue = TextInput.get(1.0, "end-1c")

        if not ReturnValue.isdigit():
            windll.user32.MessageBoxW(0,
                                      'Введёное значение не является числом',
                                      'Ошибка', 0x30)
            return

        ReturnValue = int(ReturnValue)

        if ReturnValue < Minimal:
            windll.user32.MessageBoxW(0,
                                      'Введёное значение меньше минимального',
                                      'Ошибка', 0x30)
            return

        if ReturnValue > Maximal:
            windll.user32.MessageBoxW(
                0, 'Введёное значение больше максимального', 'Ошибка', 0x30)
            return

        Window.destroy()

    TextInput = tk.Text(Window, height=1, width=20)
    TextInput.place(x=3, y=3)
    CheckButton = tk.Button(Window, text="Установить", command=CheckInput)
    CheckButton.place(x=170, y=2, height=20)

    Window.mainloop()

    IsInput = False

    try:
        return ReturnValue

    except:
        return Default


if name == 'nt':
    from threading import Thread
    Thread(target=lambda: windll.user32.MessageBoxW(0, 'Ctrl+Shift+S - Пауза/Продолжить\n' + \
                                'Ctrl+Shift+E - Закрыть\n' + \
                                'Ctrl+Shift+L - Изменить уровень искажения', 'ScaryType', 0x40 | 0x10000)).start()

Folder = split(__file__)[0].replace('\\', '/')

State = True


def Curse():
    CursedChars = (769, 771, 772, 773, 774, 775, 776, 777, 778, 782, 783, 785,
                   786, 789, 791, 793, 794, 796, 799, 800, 801, 802, 803, 804,
                   805, 807, 808, 810, 812, 816, 817, 818, 819, 820, 821, 822,
                   823, 824, 826, 829, 830, 832, 833, 835, 836, 837, 839, 841,
                   842, 844, 846, 850, 852, 853, 854, 855, 857, 859, 860, 861,
                   864)

    ToReturn = ''

    if randint(1, 2) == 1:
        for x in range(randint(CurseLevel - 1, CurseLevel + 1)):
            ToReturn += chr(choice(CursedChars))

        return ToReturn
    
    else:
        return ''


def WriteLetter(Letter):
    _write(Letter + Curse())


def PasteCursed():
    Content = paste().lower()

    Content = Content.replace('б', '6')
    Content = Content.replace('с', 's')
    Content = Content.replace('з', 'z')
    Content = Content.replace('ч', '4')
    Content = Content.replace('и', 'u')
    Content = Content.replace('п', 'n')
    Content = Content.replace('в', 'v')
    Content = Content.replace('т', 't')
    Content = Content.replace('д', 'd')
    Content = Content.replace('к', 'k')
    Content = Content.replace('о', '0')
    
    ToReturn = ''

    for Letter in Content:
        ToReturn += Curse() + Letter

    _write(ToReturn)


def AddHotkeys():
    add_hotkey(',', callback=lambda: WriteLetter('6'), suppress=True)
    add_hotkey('c', callback=lambda: WriteLetter('s'), suppress=True)
    add_hotkey('p', callback=lambda: WriteLetter('z'), suppress=True)
    add_hotkey('x', callback=lambda: WriteLetter('4'), suppress=True)
    add_hotkey('b', callback=lambda: WriteLetter('u'), suppress=True)
    add_hotkey('g', callback=lambda: WriteLetter('n'), suppress=True)
    add_hotkey('d', callback=lambda: WriteLetter('v'), suppress=True)
    add_hotkey('n', callback=lambda: WriteLetter('t'), suppress=True)
    add_hotkey('l', callback=lambda: WriteLetter('d'), suppress=True)
    add_hotkey('r', callback=lambda: WriteLetter('k'), suppress=True)
    add_hotkey('j', callback=lambda: WriteLetter('0'), suppress=True)
    add_hotkey('.', callback=lambda: _write('ю'), suppress=True)

    try:
        add_hotkey('ё', callback=lambda: WriteLetter('ё'), suppress=True)

    except:
        try:
            add_hotkey('~', callback=lambda: WriteLetter('ё'), suppress=True)

        except:
            pass


def RemoveHotkeys():
    remove_hotkey(',')
    remove_hotkey('c')
    remove_hotkey('p')
    remove_hotkey('x')
    remove_hotkey('b')
    remove_hotkey('g')
    remove_hotkey('d')
    remove_hotkey('n')
    remove_hotkey('l')
    remove_hotkey('r')
    remove_hotkey('j')
    remove_hotkey('.')

    try:
        remove_hotkey('ё')

    except:
        try:
            remove_hotkey('~')

        except:
            pass


def ChangeState():
    global State

    State = not State

    if not State:
        RemoveHotkeys()
        playsound(Folder + '/state_changed.mp3')

    else:
        AddHotkeys()
        playsound(Folder + '/state_changed.mp3')


AddHotkeys()

add_hotkey('Ctrl+Shift+S', ChangeState, suppress=True)

add_hotkey('Ctrl+Shift+E',
           lambda: playsound(Folder + '/state_changed.mp3') | _exit(0),
           suppress=True)

add_hotkey('Ctrl+V', PasteCursed, suppress=True)

playsound(Folder + '/state_changed.mp3')


def OnKeyPress(Key):
    if not IsInput:
        if is_pressed('Ctrl'):
            return

        if is_pressed('Shift'):
            return

        try:
            KeyButton = Key.char
        except:
            KeyButton = Key.name

        if KeyButton in [
                'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
                'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
                'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
                'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '0'
        ]:
            _write(Curse())


listener = keyboard.Listener(on_press=OnKeyPress)
listener.start()

while True:
    if is_pressed('Ctrl+Shift+L'):
        CurseLevel = NumberInput(CurseLevel)

    sleep(.1)