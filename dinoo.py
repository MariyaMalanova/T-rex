import numpy as np
from mss import mss 
import cv2
import pyautogui


cod = {'top': 385, 'left':155, 'width':70, 'height':60}
val = 17290
while True:
    cam = mss().grab(cod)
    cam = np.array(cam)
    cv2.imshow('Image',cam)
    cactus = cam[28,:,0]
    bird = cam[1,:,0]
    cactus_sum = np.sum(cactus)
    bird_sum = np.sum(bird)

    if cactus_sum < val:
        pyautogui.press('up')
    if bird_sum < val:
        pyautogui.press('down')

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break