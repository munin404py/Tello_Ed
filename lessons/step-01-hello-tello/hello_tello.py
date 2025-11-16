from djitellopy import Tello

# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
print("Telloに接続中...")
tello.connect()

# バッテリー残量を取得
battery = tello.get_battery()
print(f"バッテリー残量: {battery}%")

# 接続終了
print("接続を終了しました。")
