import pyautogui
import os
import time
import math
from datetime import datetime

# 讓 pyautogui 不要在每次動作後自動暫停，避免變慢
pyautogui.PAUSE = 0

terminal_width = os.get_terminal_size().columns
width, height = pyautogui.size()

# === 執行參數 ===
interval = 10        # 每隔幾秒執行一次
times = 0            # 計數
round_trip_sec = 0.4 # 上半圓來回一次的總時間（右→左→右）

# === 幾何參數 ===
radius = 150
steps_half = 40      # 半圓的分段數（來回就是 2*steps_half 次 move）
# 放在螢幕中間偏下
center_x = width // 2
center_y = int(height * 0.75)

# 每一步的延遲（往返 0.4 秒 → 半程 0.2 秒）
per_step_sleep = (round_trip_sec / 2) / steps_half

# 開始訊息
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"開始於：{start_time}")
print(f"每隔 {interval} 秒進行一次『上半圓』來回，單次 {round_trip_sec} 秒。\n按 Ctrl+C 停止")

try:
    while True:
        # 先到起點（右端）
        pyautogui.moveTo(center_x + radius, center_y)

        # 右 → 左（上半圓）：角度 0 → π
        # 注意：螢幕座標 y 向下為正，要畫上半圓需使用「減號」
        for i in range(steps_half + 1):
            angle = math.pi * i / steps_half
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)  # ← 這裡用減號，畫「上半圓」
            pyautogui.moveTo(x, y)
            time.sleep(per_step_sleep)

        # 左 → 右（上半圓回程）：角度 π → 0
        for i in range(steps_half, -1, -1):
            angle = math.pi * i / steps_half
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)
            pyautogui.moveTo(x, y)
            time.sleep(per_step_sleep)

        times += 1
        time.sleep(interval)

except KeyboardInterrupt:
    print("-" * terminal_width)
    print(f"已手動停止，共運行 {times} 次")
