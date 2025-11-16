from djitellopy import Tello
import cv2

# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
print("Telloに接続中...")
tello.connect()

# バッテリー残量を確認
battery = tello.get_battery()
print(f"バッテリー残量: {battery}%")

# カメラストリームをオン
print("カメラストリームを開始...")
tello.streamon()

print("映像を表示します。'q'キーで終了できます。")

# メインループ
while True:
    # フレーム（1枚の画像）を取得
    frame = tello.get_frame_read().frame
    
    # フレームをウィンドウに表示
    cv2.imshow("Tello Camera", frame)
    
    # キー入力を待つ（1ms）
    # 'q'キーが押されたらループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラストリームを停止
tello.streamoff()

# ウィンドウを閉じる
cv2.destroyAllWindows()

print("映像表示を終了しました。")
