from djitellopy import Tello
import time

# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
print("Telloに接続中...")
tello.connect()

# バッテリー残量を確認
battery = tello.get_battery()
print(f"バッテリー残量: {battery}%")

if battery < 50:
    print("警告: バッテリー残量が少ないです。充電してください。")
    exit()

# 離陸
print("離陸します...")
tello.takeoff()
time.sleep(3)  # 3秒待機（安定するまで）

# 上に20cm移動
print("上昇します...")
tello.move_up(20)
time.sleep(2)

# 前に30cm移動
print("前進します...")
tello.move_forward(30)
time.sleep(2)

# 時計回りに90度回転
print("回転します...")
tello.rotate_clockwise(90)
time.sleep(2)

# 後ろに30cm移動（元の位置に戻る）
print("後退します...")
tello.move_back(30)
time.sleep(2)

# 反時計回りに90度回転（元の向きに戻る）
print("回転します...")
tello.rotate_counter_clockwise(90)
time.sleep(2)

# 着陸
print("着陸します...")
tello.land()

print("飛行完了！")
