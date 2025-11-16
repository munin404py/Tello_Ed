# Step 4: Telloの目を見る（映像取得）

## 🎯 このステップの目標

OpenCVを使い、Telloのカメラ映像をPCの画面に表示できるようにしましょう。
ドローンが見ている世界を、あなたのPCで見ることができます！

> **💡 Python初心者の方へ**: このレッスンでは `while文`、`break文`、`ビット演算` などの概念を使います。これらがよくわからない場合は、[Step 0: Pythonの基本](../step-0-python-basics) を先に学習することをお勧めします！

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

## 🔍 コードの詳しい解説

### カメラストリームの開始

```python
tello.streamon()
```

*   Telloのカメラからの映像配信（ストリーミング）を開始する
*   これを実行すると、Telloから映像データが継続的に送られてくるようになります

💡 **ストリームとは？**:
*   データを「流れ」のように連続して送ること
*   動画は、1秒間に何枚もの画像（フレーム）を連続で送ることで実現される

### メインループ - while文

```python
while True:
    # フレームを取得
    frame = tello.get_frame_read().frame
    
    # 表示
    cv2.imshow("Tello Camera", frame)
    
    # キー入力をチェック
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

*   **`while True:`**: 永久ループ（無限ループ）
*   **`break`**: ループから抜け出す

💡 **while文の仕組み**:
```python
while 条件:
    # 条件が真（True）の間、繰り返し実行される処理
```

*   `while True:` は「ずっと繰り返す」という意味
*   `break` で強制的にループを抜けることができる

**なぜ無限ループ？**:
*   映像は、終わりがない「連続したフレーム」の流れ
*   ユーザーが「q」キーを押すまで、ずっと映像を表示し続ける必要がある

### フレームの取得

```python
frame = tello.get_frame_read().frame
```

*   **`get_frame_read()`**: フレームリーダーオブジェクトを取得
*   **`.frame`**: 現在のフレーム（1枚の画像）を取得

💡 **フレームとは？**:
*   動画は、たくさんの静止画（フレーム）を高速で切り替えて表示したもの
*   1秒間に30フレーム表示すると、滑らかな動画に見える
*   フレームは、NumPy配列という形式の画像データ

### 映像の表示

```python
cv2.imshow("Tello Camera", frame)
```

*   **`cv2.imshow()`**: OpenCVの画像表示関数
*   **第1引数**: ウィンドウの名前（タイトルバーに表示される）
*   **第2引数**: 表示する画像データ（フレーム）

### キー入力の待機とチェック

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

*   **`cv2.waitKey(1)`**: 1ミリ秒だけキー入力を待つ
*   **`& 0xFF`**: ビット演算（最後の8ビットだけを取り出す）
*   **`ord('q')`**: 文字 'q' の文字コード（ASCIIコード）を取得
*   **`== ord('q')`**: 'q'キーが押されたかチェック

💡 **cv2.waitKey()の重要性**:
1.  **画面更新**: この関数を呼ばないと、ウィンドウが正しく表示されない
2.  **キー入力取得**: ユーザーがキーを押したかどうかを検知する
3.  **待機時間**: 1ミリ秒待つことで、CPUに余裕を持たせる

💡 **初心者向け補足**:
```python
# `& 0xFF` と `ord('q')` について
key = cv2.waitKey(1)  # 押されたキーのコードを取得
if key & 0xFF == ord('q'):  # 'q'が押されたかチェック
    break  # ループを抜ける
```

*   `ord('q')` は 113 という数値
*   'q'キーを押すと、その文字コード（113）が返される
*   それをチェックして、一致したらループを抜ける

### リソースの解放

```python
tello.streamoff()
cv2.destroyAllWindows()
```

*   **`streamoff()`**: カメラストリームを停止
*   **`destroyAllWindows()`**: 開いているすべてのウィンドウを閉じる

💡 **なぜ必要？**:
*   使い終わったリソース（カメラ、ウィンドウ）は、きちんと解放する
*   メモリリークを防ぎ、次回もスムーズに起動できるようにする

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
