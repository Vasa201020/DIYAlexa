import time
import random
import mouse
import keyboard


def pauza():
    while keyboard.is_pressed('q') == False :
        wait = random.randint(3, 14)

        time.sleep(int(wait))

        mouse.move(1257, 347, absolute=True, duration=0.3)

        mouse.click('left')

        time.sleep(2)

        mouse.click('left')