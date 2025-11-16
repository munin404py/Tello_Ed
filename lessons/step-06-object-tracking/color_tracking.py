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

# 赤色のHSV範囲を定義
# HSV色空間: Hue（色相）, Saturation（彩度）, Value（明度）
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

print("赤い物体を追跡します。'q'キーで終了できます。")

while True:
    # フレームを取得
    frame = tello.get_frame_read().frame
    
    # BGRからHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 赤色の範囲でマスクを作成
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # 輪郭を検出
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 最大の輪郭を見つける
    if contours:
        # 面積が最大の輪郭を取得
        largest_contour = max(contours, key=cv2.contourArea)
        
        # 輪郭の面積が一定以上の場合のみ処理
        if cv2.contourArea(largest_contour) > 500:
            # 輪郭の外接矩形を取得
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            # 中心座標を計算
            center_x = x + w // 2
            center_y = y + h // 2
            
            # 矩形を描画
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # 中心点を描画
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            
            # 座標をテキストで表示
            cv2.putText(
                frame,
                f"({center_x}, {center_y})",
                (center_x + 10, center_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )
            
            # コンソールに出力
            print(f"赤い物体の中心座標: ({center_x}, {center_y})")
    
    # 元のフレームとマスクを表示
    cv2.imshow("Tello Camera - Color Tracking", frame)
    cv2.imshow("Mask", mask)
    
    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラストリームを停止
tello.streamoff()

# ウィンドウを閉じる
cv2.destroyAllWindows()

print("追跡を終了しました。")
