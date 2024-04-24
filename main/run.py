import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

aviso = "start"
print(aviso)

LIFE_STATUS = (218, 79, 79)
FULL_LIFE_STATUS = (218, 79, 79)
MANA_STATUS = (83, 80, 217)
REGION_RING = (1753, 257, 32, 32)
# Range life em pixels -> 1856 (Cheio) - 1766 (Vazio)


def check_equip():
    print('checando equips!')
    if pg.locateOnScreen('imgs/ring_slot.png', confidence=0.90, region=REGION_RING) != None:
        if event_th.is_set():
            return
        print('colocando ring')
        pg.press('7')
        pg.sleep(0.2)


def check_status(name):
    if name == 'mana':
        print(f'checando {name}...')
        if event_th.is_set():
            return
        if pg.pixel(1833, 160) == MANA_STATUS:
            pg.press('F12')
            pg.sleep(0.2)
            pg.press('F11')
            pg.sleep(0.2)
            pg.press('F11')


def run():
    print('inicio')
    while True:
        if event_th.is_set():
            return
        check_equip()
        pg.sleep(1)
        if event_th.is_set():
            return
        check_status('mana')
        pg.sleep(1)
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
