import cv2
import keyboard
import pyautogui
import numpy as np

fps = 30
tamanho_tela = tuple(pyautogui.size())
print(tamanho_tela)

codec = cv2.VideoWriter_fourcc(*"mp4h")
video = cv2.VideoWriter("video", codec, fps, tamanho_tela)
