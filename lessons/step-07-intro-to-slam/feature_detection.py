from djitellopy import Tello
import cv2
import numpy as np

# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
print("Telloに接続中...")
tello.connect()

# カメラストリームをオン
print("カメラストリームを開始...")
tello.streamon()

print("特徴点を表示します。'q'キーで終了できます。")

while True:
    # フレームを取得
    frame = tello.get_frame_read().frame
    
    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 特徴点を検出
    corners = cv2.goodFeaturesToTrack(
        gray,
        maxCorners=100,
        qualityLevel=0.3,
        minDistance=7
    )
    
    # 特徴点を描画
    if corners is not None:
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 0), -1)
        
        # 検出した特徴点の数を表示
        cv2.putText(
            frame,
            f"Feature Points: {len(corners)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
    
    # フレームを表示
    cv2.imshow("Tello Camera - Feature Points", frame)
    
    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラストリームを停止
tello.streamoff()

# ウィンドウを閉じる
cv2.destroyAllWindows()

print("特徴点検出を終了しました。")
