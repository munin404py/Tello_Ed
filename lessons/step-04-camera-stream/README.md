# Step 4: Telloの目を見る（映像取得）

## 🎯 このステップの目標

OpenCVを使い、Telloのカメラ映像をPCの画面に表示できるようにしましょう。
ドローンが見ている世界を、あなたのPCで見ることができます！

## 📝 学習内容

*   OpenCVライブラリの基本的な使い方
*   Telloのカメラストリームの取得方法
*   リアルタイム映像の表示方法
*   フレームレート（FPS）の概念

## 🔧 準備

### 必要なライブラリのインストール

```bash
pip install opencv-python djitellopy
```

*   `opencv-python`: 画像・映像処理ライブラリ
*   `djitellopy`: Tello制御ライブラリ

## 💻 サンプルコード

`camera_stream.py` というファイル名で、以下のコードを作成してみましょう。

```python
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
```

## 🚀 実行方法

1. Telloのスイッチを入れて、Wi-Fiに接続します
2. ターミナルで以下のコマンドを実行します：

```bash
python camera_stream.py
```

3. Telloのカメラ映像がウィンドウに表示されます
4. 終了するには、ウィンドウをアクティブにして `q` キーを押します

## ✅ 期待される動作

*   新しいウィンドウが開き、Telloのカメラが捉えている映像がリアルタイムで表示されます
*   `q` キーを押すと、映像表示が終了します

## 🔍 コードの解説

### カメラストリームの開始

```python
tello.streamon()
```

Telloのカメラからの映像配信を開始します。これを実行すると、Telloから映像データが送られてくるようになります。

### フレームの取得

```python
frame = tello.get_frame_read().frame
```

*   `get_frame_read()`: フレームリーダーオブジェクトを取得
*   `.frame`: 現在のフレーム（1枚の画像）を取得

フレームは、NumPy配列として表現された画像データです。

### 映像の表示

```python
cv2.imshow("Tello Camera", frame)
```

*   第1引数: ウィンドウの名前
*   第2引数: 表示する画像（フレーム）

### キー入力の待機

```python
cv2.waitKey(1)
```

*   1ミリ秒だけキー入力を待つ
*   この関数を呼ばないと、ウィンドウが正しく表示されません
*   `& 0xFF == ord('q')`: 'q'キーが押されたかチェック

### リソースの解放

```python
tello.streamoff()
cv2.destroyAllWindows()
```

カメラストリームを停止し、開いたウィンドウを閉じます。

## 💡 応用例：フレームを保存する

カメラ映像から1枚の写真を保存するコードです。

`take_photo.py`:

```python
from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
tello.streamon()

# 数秒待ってカメラを安定させる
import time
time.sleep(2)

# フレームを取得
frame = tello.get_frame_read().frame

# 画像として保存
cv2.imwrite("tello_photo.jpg", frame)
print("写真を保存しました: tello_photo.jpg")

tello.streamoff()
```

## 💡 応用例：映像にテキストを表示する

```python
from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
battery = tello.get_battery()
tello.streamon()

while True:
    frame = tello.get_frame_read().frame
    
    # フレームにテキストを描画
    cv2.putText(
        frame, 
        f"Battery: {battery}%", 
        (10, 30),  # 位置（x, y）
        cv2.FONT_HERSHEY_SIMPLEX,  # フォント
        1,  # サイズ
        (0, 255, 0),  # 色（BGR形式で緑）
        2  # 太さ
    )
    
    cv2.imshow("Tello Camera", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
cv2.destroyAllWindows()
```

## 🎓 やってみよう！

1. **フレームのサイズを確認してみよう**
   ```python
   print(f"フレームサイズ: {frame.shape}")
   # 結果例: (720, 960, 3) → 高さ720px、幅960px、3チャンネル（BGR）
   ```

2. **映像を録画してみよう**
   - OpenCVの `VideoWriter` を使って、映像をファイルに保存できます

3. **飛行しながら映像を見てみよう**
   - 離陸してから映像を表示すると、空中からの視点が見られます

## ⚠️ トラブルシューティング

### 映像が表示されない

*   Telloとの接続が正しく確立されているか確認してください
*   `tello.streamon()` が実行されているか確認してください
*   数秒待ってから再度実行してみてください

### 映像がカクカクする

*   Wi-Fiの電波が弱い可能性があります
*   Telloに近づいてみてください
*   他のWi-Fi機器の電源を切ってみてください

### ウィンドウが閉じられない

*   ウィンドウをアクティブ（クリック）してから `q` キーを押してください
*   それでも閉じない場合は、ターミナルで `Ctrl+C` を押してください

## 🎉 おめでとうございます！

Telloのカメラ映像を取得して表示できるようになりました！
次は [Step 5](../step-05-simple-frontend) で、ブラウザに操作パネルを作ってみましょう。
