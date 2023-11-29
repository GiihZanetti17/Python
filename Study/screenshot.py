import cv2
import keyboard
import pyautogui
import numpy as np

fps = 30
tamanho_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"mp4h")
video = cv2.VideoWriter("video", codec, fps, tamanho_tela)

while True:
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    frame = cv2.cvtColor(frame, cv2.RGB)

    video.write(frame)

    if keyboard.is_pressed("esc"):
        break

video.release()
cv2.destroyALllWindows()
