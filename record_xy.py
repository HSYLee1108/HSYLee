import pyautogui
import time
import keyboard  # pip install keyboard

print("移動滑鼠到想抓的位置，座標會持續更新。按 [Esc] 停止。\n")

while True:
    if keyboard.is_pressed('esc'):
        print("\n已停止。")
        break

    x, y = pyautogui.position()
    print(f"\r目前座標：X={x}  Y={y}", end="")
    time.sleep(0.05)
