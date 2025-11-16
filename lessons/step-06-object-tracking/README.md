# Step 6: 簡単な物体追跡

## 🎯 このステップの目標

OpenCVの画像処理で、特定の色を見つけてその座標を取得しましょう。
これは、自律飛行やターゲット追跡の基礎となる技術です！

> **💡 初心者の方へ**: このレッスンでは、OpenCVの高度な機能を使います。Step 4でカメラ映像の基本を学んでから挑戦してください！画像処理の概念は少し難しいですが、コメントを読みながら一つずつ理解していきましょう。

## 📝 学習内容

*   色空間（RGB、HSV）の概念
*   OpenCVでの色検出方法
*   輪郭検出とその応用
*   カメラ映像上での物体の位置特定

## 🔧 準備

### 必要なライブラリ

```bash
pip install opencv-python numpy djitellopy
```

### 追跡対象の準備

*   赤、青、緑などの単色の物体（ボール、紙、マーカーなど）
*   明るい場所で実験することをお勧めします

## 💻 サンプルコード

`color_tracking.py` というファイル名で、以下のコードを作成してみましょう。

```python
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
```

## 🚀 実行方法

1. Telloのスイッチを入れて、Wi-Fiに接続します
2. 赤い物体（ボール、紙など）を用意します
3. ターミナルで以下のコマンドを実行します：

```bash
python color_tracking.py
```

4. カメラ映像が表示されます
5. 赤い物体をカメラに近づけると、緑色の矩形と中心点が表示されます

## ✅ 期待される動作

*   **元の映像ウィンドウ**: 赤い物体の周りに緑の矩形が表示され、中心に赤い点が表示されます
*   **マスクウィンドウ**: 赤い部分だけが白く表示されます
*   **コンソール**: 検出された物体の座標が表示されます

## 🔍 コードの解説

### HSV色空間

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

*   RGB（赤・緑・青）よりも、HSV（色相・彩度・明度）の方が色の検出に適しています
*   照明条件の変化に強い

### 色の範囲指定

```python
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
```

*   `[H, S, V]` の形式で範囲を指定
*   赤色は色相（H）が 0〜10 の範囲

### マスクの作成

```python
mask = cv2.inRange(hsv, lower_red, upper_red)
```

指定した色の範囲に含まれるピクセルを白（255）、それ以外を黒（0）にしたマスク画像を作成します。

### 輪郭検出

```python
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

マスク画像から物体の輪郭を検出します。

### 外接矩形の取得

```python
x, y, w, h = cv2.boundingRect(largest_contour)
```

*   `(x, y)`: 矩形の左上の座標
*   `w, h`: 矩形の幅と高さ

## 🎨 他の色を検出する

### 青色を検出

```python
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([130, 255, 255])
```

### 緑色を検出

```python
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])
```

### 黄色を検出

```python
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
```

## 💡 応用例：ドローンが物体を追跡

物体の位置に応じてドローンを移動させるコードです：

```python
# ... 上記のコードに追加 ...

# フレームの中心座標
frame_center_x = frame.shape[1] // 2
frame_center_y = frame.shape[0] // 2

# 物体が検出された場合
if contours and cv2.contourArea(largest_contour) > 500:
    # 物体の位置を判定
    offset_x = center_x - frame_center_x
    offset_y = center_y - frame_center_y
    
    # しきい値を設定（±50ピクセル以内なら中央とみなす）
    threshold = 50
    
    if abs(offset_x) > threshold:
        if offset_x > 0:
            print("物体が右にあります → 右に移動")
            # tello.move_right(20)
        else:
            print("物体が左にあります → 左に移動")
            # tello.move_left(20)
    
    if abs(offset_y) > threshold:
        if offset_y > 0:
            print("物体が下にあります → 下に移動")
            # tello.move_down(20)
        else:
            print("物体が上にあります → 上に移動")
            # tello.move_up(20)
```

※ 実際にドローンを飛行させながら追跡する場合は、安全に十分注意してください！

## 🎓 やってみよう！

1. **複数の色を同時に検出してみよう**
   - 赤と青の物体を同時に検出してみる

2. **色の範囲を調整してみよう**
   - トラックバーを使って、リアルタイムでHSV範囲を調整できるようにする

3. **物体のサイズも検出してみよう**
   - 輪郭の面積から物体までの距離を推定する

## ⚠️ トラブルシューティング

### 物体が検出されない

*   照明が暗すぎる可能性があります → 明るい場所で試してください
*   HSV範囲が適切でない可能性があります → 範囲を調整してください
*   物体がカメラに近すぎる/遠すぎる可能性があります

### 誤検出が多い

*   背景に似た色がある可能性があります
*   HSV範囲を狭くしてみてください
*   面積の閾値（`500`）を大きくしてみてください

## 🎉 おめでとうございます！

画像処理を使った物体検出ができるようになりました！
次は [Step 7](../step-07-intro-to-slam) で、SLAMの概念を学びましょう。
