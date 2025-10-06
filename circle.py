import pyautogui
import time
import math
import os
import keyboard
from datetime import datetime

# 更順的滑動：移除每步自動暫停
pyautogui.PAUSE = 0

# === 參數 ===
interval = 0.1          # 每次往返後的等待秒數
round_trip_sec = 0.4  # 上半圓「右→左→右」往返時間（秒）
radius = 240
steps_half = 40       # 半圓分段；來回共 2*steps_half 次移動

# === 位置（螢幕中偏右、偏下）===
width, height = pyautogui.size()
center_x =1645
center_y = 680

# 每步延遲（確保整段約 round_trip_sec 秒）
per_step_sleep = (round_trip_sec / 2) / steps_half

# === 開始訊息 ===
print(f"開始於：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"每隔 {interval} 秒進行一次『上半圓』來回，按 Esc 可停止。")

times = 0
try:
    while True:
        if keyboard.is_pressed('esc'):
            raise KeyboardInterrupt

        # 起點（右端）
        pyautogui.moveTo(center_x + radius, center_y)

        # 右 → 左（上半圓，角度 0 → π）
        for i in range(steps_half + 1):
            if keyboard.is_pressed('esc'):
                raise KeyboardInterrupt
            angle = math.pi * i / steps_half
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)  # 螢幕座標向下為正，減號代表上半圓
            pyautogui.moveTo(x, y)
            time.sleep(per_step_sleep)

        # 左 → 右（上半圓回程，角度 π → 0）
        for i in range(steps_half, -1, -1):
            if keyboard.is_pressed('esc'):
                raise KeyboardInterrupt
            angle = math.pi * i / steps_half
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)
            pyautogui.moveTo(x, y)
            time.sleep(per_step_sleep)

        times += 1
        time.sleep(interval)

except KeyboardInterrupt:
    print(f"✅ 已停止，總共運行 {times} 次。")