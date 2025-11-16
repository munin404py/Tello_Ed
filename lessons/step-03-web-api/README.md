# Step 3: Web APIでドローンを操る

## 🎯 このステップの目標

FastAPIを使ってWeb APIを作り、ブラウザからドローンを操作できるようにしましょう。
これで、Web技術とドローン制御を組み合わせることができます！

## 📝 学習内容

*   FastAPIの基本的な使い方
*   Web APIとは何か
*   HTTPリクエスト（GET/POST）の仕組み
*   APIエンドポイントの作成方法

## 🔧 準備

### 必要なライブラリのインストール

```bash
pip install fastapi uvicorn djitellopy
```

*   `fastapi`: Web APIフレームワーク
*   `uvicorn`: FastAPIを動かすためのサーバー
*   `djitellopy`: Telloを制御するライブラリ

## 💻 サンプルコード

`api_server.py` というファイル名で、以下のコードを作成してみましょう。

```python
from fastapi import FastAPI
from djitellopy import Tello
import uvicorn

# FastAPIアプリを作成
app = FastAPI()

# Telloオブジェクト（グローバル変数）
tello = None

@app.get("/")
def read_root():
    """ルートエンドポイント - APIが動いているか確認"""
    return {"message": "Tello API Server is running!"}

@app.post("/connect")
def connect():
    """Telloに接続"""
    global tello
    try:
        tello = Tello()
        tello.connect()
        battery = tello.get_battery()
        return {"status": "connected", "battery": battery}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/takeoff")
def takeoff():
    """離陸"""
    global tello
    if tello is None:
        return {"status": "error", "message": "Not connected"}
    try:
        tello.takeoff()
        return {"status": "success", "message": "Takeoff complete"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/land")
def land():
    """着陸"""
    global tello
    if tello is None:
        return {"status": "error", "message": "Not connected"}
    try:
        tello.land()
        return {"status": "success", "message": "Landing complete"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/move/{direction}/{distance}")
def move(direction: str, distance: int):
    """移動（direction: up/down/left/right/forward/back, distance: cm）"""
    global tello
    if tello is None:
        return {"status": "error", "message": "Not connected"}
    
    try:
        if direction == "up":
            tello.move_up(distance)
        elif direction == "down":
            tello.move_down(distance)
        elif direction == "left":
            tello.move_left(distance)
        elif direction == "right":
            tello.move_right(distance)
        elif direction == "forward":
            tello.move_forward(distance)
        elif direction == "back":
            tello.move_back(distance)
        else:
            return {"status": "error", "message": "Invalid direction"}
        
        return {"status": "success", "message": f"Moved {direction} {distance}cm"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/battery")
def get_battery():
    """バッテリー残量を取得"""
    global tello
    if tello is None:
        return {"status": "error", "message": "Not connected"}
    try:
        battery = tello.get_battery()
        return {"status": "success", "battery": battery}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # サーバーを起動（ポート8000で待ち受け）
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 🚀 実行方法

1. Telloのスイッチを入れて、Wi-Fiに接続します
2. ターミナルで以下のコマンドを実行してAPIサーバーを起動します：

```bash
python api_server.py
```

3. サーバーが起動すると、以下のようなメッセージが表示されます：

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

4. ブラウザを開いて `http://localhost:8000` にアクセスしてみましょう

## 🌐 APIの使い方

### 1. APIの動作確認

ブラウザで `http://localhost:8000` にアクセスすると、以下のような応答が返ってきます：

```json
{"message": "Tello API Server is running!"}
```

### 2. Telloに接続

以下のURLにアクセスします（POSTリクエスト）：

```
http://localhost:8000/connect
```

※ ブラウザから直接POSTリクエストを送ることはできないので、次のいずれかの方法を使います：

**方法1: curlコマンドを使う（別のターミナルで）**

```bash
curl -X POST http://localhost:8000/connect
```

**方法2: Pythonスクリプトで試す**

`test_api.py` というファイルを作成：

```python
import requests

# 接続
response = requests.post("http://localhost:8000/connect")
print(response.json())

# バッテリー確認
response = requests.get("http://localhost:8000/battery")
print(response.json())

# 離陸
response = requests.post("http://localhost:8000/takeoff")
print(response.json())

# 2秒待機
import time
time.sleep(2)

# 着陸
response = requests.post("http://localhost:8000/land")
print(response.json())
```

実行：
```bash
pip install requests
python test_api.py
```

### 3. その他のAPI

*   `POST /takeoff` - 離陸
*   `POST /land` - 着陸
*   `POST /move/forward/30` - 前に30cm移動
*   `POST /move/up/20` - 上に20cm移動
*   `GET /battery` - バッテリー残量取得

## 🔍 コードの解説

### FastAPIの基本

```python
from fastapi import FastAPI
app = FastAPI()
```

FastAPIアプリケーションを作成します。これがWeb APIの土台です。

### エンドポイントの定義

```python
@app.get("/")
def read_root():
    return {"message": "Hello"}
```

*   `@app.get("/")`: GETリクエストを受け付けるエンドポイント
*   `/`: URLのパス
*   `return {...}`: JSON形式で返す内容

```python
@app.post("/takeoff")
def takeoff():
    tello.takeoff()
    return {"status": "success"}
```

*   `@app.post(...)`: POSTリクエストを受け付ける
*   状態を変更する操作（離陸、着陸など）にはPOSTを使用

### パスパラメータ

```python
@app.post("/move/{direction}/{distance}")
def move(direction: str, distance: int):
    # direction と distance を関数の引数として受け取れる
```

URLの一部を変数として受け取ることができます。

## 🎓 やってみよう！

1. **新しいエンドポイントを追加してみよう**
   - 回転のためのエンドポイント `/rotate/clockwise/90` など

2. **エラーハンドリングを改善してみよう**
   - バッテリー残量が少ない時は離陸を拒否する

3. **ドキュメントを見てみよう**
   - `http://localhost:8000/docs` にアクセスすると、FastAPIが自動生成したAPIドキュメントが見られます！

## 🎉 おめでとうございます！

Web APIを使ってドローンを操作できるようになりました！
次は [Step 4](../step-04-camera-stream) で、Telloのカメラ映像を取得してみましょう。
