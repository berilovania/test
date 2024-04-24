import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

aviso = "start"
print(aviso)

LIFE_STATUS = (218, 79, 79)
FULL_LIFE_STATUS = (218, 79, 79)
MANA_STATUS = (83, 80, 217)
# Range life em pixels -> 1856 (Cheio) - 1766 (Vazio)


def check_status(name):
    if name == 'life':
        print(f'checando {name}...')
        if event_th.is_set():
            return
        if pg.pixel(1856, 147) != FULL_LIFE_STATUS:
            if pg.pixel(1805, 147) != LIFE_STATUS:
                pg.press('1')
                pg.press('2')
            elif pg.pixel(1838, 147) != LIFE_STATUS:
                pg.press('1')
    elif name == 'mana':
        print(f'checando {name}...')
        if event_th.is_set():
            return
        if pg.pixel(1856, 160) != MANA_STATUS:
            if pg.pixel(1825, 160) != MANA_STATUS:
                pg.press('f')


def run():
    print('inicio')
    while True:
        if event_th.is_set():
            return
        check_status('life')
        pg.sleep(0.2)
        if event_th.is_set():
            return
        check_status('mana')
        pg.sleep(0.2)
        if event_th.is_set():
            return


def key_code(key):
    if key == keyboard.Key.home:
        event_th.set()
        return False
    elif key == keyboard.Key.insert:
        th_run.start()


global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listner:
    listner.join()
