# Step 3: Web APIでドローンを操る

## 🎯 このステップの目標

FastAPIを使ってWeb APIを作り、ブラウザからドローンを操作できるようにしましょう。
これで、Web技術とドローン制御を組み合わせることができます！

> **💡 初心者の方へ**: このレッスンでは「ポート」「サーバー」「API」といった用語が出てきます。これらの基本概念については [Step 00: 環境構築](../step-00-environment-setup) の「ポートとネットワークの基本」セクションで詳しく解説していますので、先に読むことをお勧めします！

## 📝 学習内容

*   Web APIとは何か（初心者向け解説）
*   FastAPIの基本的な使い方
*   HTTPリクエスト（GET/POST）の仕組み
*   ポートの開き方とサーバーの起動
*   APIエンドポイントの作成方法

## 📚 Web APIって何？（初心者向け）

### レストランで例えると...

**Web API** は、プログラム同士が会話するための「窓口」のようなものです。

レストランで考えてみましょう：
*   **あなた（クライアント）**: 料理を注文したい人
*   **ウェイター（API）**: 注文を聞いて、厨房に伝える人
*   **厨房（サーバー）**: 実際に料理を作る場所

1.  あなた → ウェイターに「ハンバーグください」と注文（**リクエスト**）
2.  ウェイター → 厨房に「ハンバーグ1つ！」と伝える
3.  厨房 → ハンバーグを作る
4.  ウェイター → あなたにハンバーグを提供（**レスポンス**）

Web APIも同じ！
*   **ブラウザ**: 「ドローンを離陸させて」とリクエスト
*   **API**: リクエストを受け取って、ドローンに命令を伝える
*   **サーバー**: ドローンを実際に操作する
*   **API**: 「離陸しました！」とレスポンスを返す

### HTTPリクエストとは？

**HTTP** は、ブラウザとサーバーが会話するときの「言語」です。

主なリクエストの種類：
*   **GET**: データを取得する（「見せて」）
    *   例: バッテリー残量を確認する
*   **POST**: データを送信する、状態を変更する（「やって」）
    *   例: ドローンを離陸させる

### エンドポイントとは？

**エンドポイント** は、APIの「アドレス」です。

例:
*   `http://localhost:8000/battery` → バッテリー情報が欲しい
*   `http://localhost:8000/takeoff` → 離陸してほしい
*   `http://localhost:8000/land` → 着陸してほしい

URLの最後の部分（`/battery`, `/takeoff` など）で、何をしたいかを指定します。

## 🔧 準備

### 必要なライブラリのインストール

```bash
pip install fastapi uvicorn djitellopy
```

*   `fastapi`: Web APIフレームワーク（APIを簡単に作れる道具）
*   `uvicorn`: FastAPIを動かすためのサーバー（アプリを起動する道具）
*   `djitellopy`: Telloを制御するライブラリ

💡 **ポートについて**: このレッスンでは、ポート8000番を使います。
ポートは、コンピュータの「出入り口」のようなもので、1つのコンピュータで複数のプログラムが同時にネットワーク通信をするときに、どのプログラムへのデータかを区別するために使います。詳しくは [Step 00](../step-00-environment-setup) を参照してください。

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

### FastAPIアプリの作成

```python
from fastapi import FastAPI
app = FastAPI()
```

*   **`from fastapi import FastAPI`**: FastAPIライブラリからFastAPIクラスをインポート
*   **`app = FastAPI()`**: FastAPIアプリケーションのインスタンス（実体）を作成

これが、Web APIの「土台」になります。

💡 **初心者向け補足**:
*   `app` という変数に、APIアプリ全体を管理するオブジェクトが入っています
*   この `app` に、いろんなエンドポイント（URLとその処理）を追加していきます

### グローバル変数

```python
tello = None
```

*   **`tello = None`**: 最初は何も入っていない状態
*   **グローバル変数**: プログラム全体で共有できる変数

💡 **なぜグローバル変数？**:
*   複数のエンドポイント（`/connect`, `/takeoff`, `/land` など）で、同じTelloオブジェクトを使いたい
*   一度接続したら、その接続をずっと使い回す

### デコレータとエンドポイント

```python
@app.get("/")
def read_root():
    return {"message": "Tello API Server is running!"}
```

*   **`@app.get("/")`**: デコレータ（装飾子）
    *   「この関数は、`/` というURLへのGETリクエストを処理します」という宣言
*   **`def read_root():`**: 実際に実行される関数
*   **`return {...}`**: JSON形式のデータを返す

💡 **デコレータって何？**:
*   関数に「印」をつけて、特別な意味を持たせるもの
*   `@app.get("/")` は、「この関数をルート（`/`）のGETリクエストと紐づける」という印

**アクセス方法**:
```
http://localhost:8000/
```
ブラウザでこのURLを開くと、`{"message": "Tello API Server is running!"}` と表示されます。

### POSTエンドポイント

```python
@app.post("/connect")
def connect():
    global tello
    try:
        tello = Tello()
        tello.connect()
        battery = tello.get_battery()
        return {"status": "connected", "battery": battery}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```

*   **`@app.post("/connect")`**: `/connect` へのPOSTリクエストを処理
*   **`global tello`**: グローバル変数 `tello` を使うことを宣言
*   **`try-except`**: エラーが起きても落ちないように

💡 **GETとPOSTの使い分け**:
*   **GET**: データを取得するだけ（状態は変えない）
    *   例: バッテリー残量を確認する
*   **POST**: 何かを実行する、状態を変える
    *   例: ドローンを離陸させる、接続する

### パスパラメータ

```python
@app.post("/move/{direction}/{distance}")
def move(direction: str, distance: int):
    # ...
    if direction == "up":
        tello.move_up(distance)
    elif direction == "down":
        tello.move_down(distance)
    # ...
```

*   **`{direction}`**: URLの一部を変数として受け取る
*   **`{distance}`**: もう一つの変数
*   **`direction: str`**: directionは文字列型
*   **`distance: int`**: distanceは整数型

**使用例**:
```
POST http://localhost:8000/move/forward/50
```
→ `direction="forward"`, `distance=50` として関数が呼ばれる

💡 **初心者向け補足**:
*   URLの一部を変数のように使える便利な機能
*   `{変数名}` で指定し、関数の引数として受け取れる

### サーバーの起動

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

*   **`if __name__ == "__main__":`**: このファイルが直接実行されたときだけ実行される
*   **`uvicorn.run()`**: uvicornサーバーを起動する
*   **`host="0.0.0.0"`**: すべてのネットワークインターフェースで待ち受ける
*   **`port=8000`**: ポート8000番で待ち受ける

💡 **ポートとホスト**:
*   **ポート8000**: この「出入り口」でリクエストを待つ
*   **host="0.0.0.0"**: すべてのIPアドレスから接続を受け付ける
    *   `localhost` (127.0.0.1) からも、同じネットワーク内の他のPCからもアクセス可能
*   `http://localhost:8000` でアクセスできます

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
