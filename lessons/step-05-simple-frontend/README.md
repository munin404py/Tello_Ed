# Step 5: 操作パネルを作る（フロントエンド）

## 🎯 このステップの目標

簡単なHTMLとJavaScriptで、ブラウザにドローン操作用のボタンを作りましょう。
これで、コードを書かずにボタンをクリックするだけでドローンを操作できるようになります！

> **💡 初心者の方へ**: このレッスンでは主にHTML/JavaScriptを使いますが、Pythonの知識も必要です。また、Step 3で作ったWeb APIを使うので、先に [Step 3](../step-03-web-api) を完了してください！

## 📝 学習内容

*   HTML/CSS/JavaScriptの基礎
*   ブラウザからのAPI呼び出し（Fetch API）
*   フロントエンドとバックエンドの連携
*   CORS（Cross-Origin Resource Sharing）の概念

## 🔧 準備

このステップでは、Step 3で作成したAPIサーバーを使用します。
まだ作成していない場合は、[Step 3](../step-03-web-api) を先に完了してください。

### 必要なライブラリの更新

FastAPIでCORSを有効にするため、`api_server.py` を少し修正します。

## 💻 サンプルコード

### 1. APIサーバーの修正

`api_server.py` にCORS設定を追加します：

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from djitellopy import Tello
import uvicorn

app = FastAPI()

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では具体的なドメインを指定すること
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Telloオブジェクト（グローバル変数）
tello = None

# ... 以下、Step 3と同じエンドポイント定義 ...
```

### 2. HTMLファイルの作成

`controller.html` というファイル名で、以下のコードを作成してみましょう。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tello ドローンコントローラー</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        
        h1 {
            color: #333;
            text-align: center;
        }
        
        .section {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .button-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 15px;
        }
        
        button {
            padding: 15px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        button:hover {
            transform: scale(1.05);
        }
        
        button:active {
            transform: scale(0.95);
        }
        
        .connect-btn {
            background-color: #4CAF50;
            color: white;
        }
        
        .takeoff-btn {
            background-color: #2196F3;
            color: white;
        }
        
        .land-btn {
            background-color: #f44336;
            color: white;
        }
        
        .move-btn {
            background-color: #FF9800;
            color: white;
        }
        
        .info {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            background-color: #e3f2fd;
        }
        
        #status {
            font-weight: bold;
            color: #1976D2;
        }
    </style>
</head>
<body>
    <h1>🚁 Tello ドローンコントローラー</h1>
    
    <div class="section">
        <h2>接続</h2>
        <button class="connect-btn" onclick="connect()">Telloに接続</button>
        <button class="connect-btn" onclick="getBattery()">バッテリー確認</button>
        <div class="info">
            <div id="status">未接続</div>
        </div>
    </div>
    
    <div class="section">
        <h2>基本操作</h2>
        <button class="takeoff-btn" onclick="takeoff()">離陸 ✈️</button>
        <button class="land-btn" onclick="land()">着陸 🛬</button>
    </div>
    
    <div class="section">
        <h2>移動操作</h2>
        <div class="button-grid">
            <div></div>
            <button class="move-btn" onclick="move('forward', 30)">前進 ⬆️</button>
            <div></div>
            
            <button class="move-btn" onclick="move('left', 30)">左 ⬅️</button>
            <button class="move-btn" onclick="move('up', 20)">上昇 🔼</button>
            <button class="move-btn" onclick="move('right', 30)">右 ➡️</button>
            
            <div></div>
            <button class="move-btn" onclick="move('back', 30)">後退 ⬇️</button>
            <button class="move-btn" onclick="move('down', 20)">下降 🔽</button>
        </div>
    </div>

    <script>
        const API_URL = 'http://localhost:8000';

        async function connect() {
            try {
                const response = await fetch(`${API_URL}/connect`, {
                    method: 'POST'
                });
                const data = await response.json();
                
                if (data.status === 'connected') {
                    document.getElementById('status').textContent = 
                        `接続成功！ バッテリー: ${data.battery}%`;
                } else {
                    document.getElementById('status').textContent = 
                        `エラー: ${data.message}`;
                }
            } catch (error) {
                document.getElementById('status').textContent = 
                    `接続エラー: ${error.message}`;
            }
        }

        async function getBattery() {
            try {
                const response = await fetch(`${API_URL}/battery`);
                const data = await response.json();
                
                if (data.status === 'success') {
                    document.getElementById('status').textContent = 
                        `バッテリー残量: ${data.battery}%`;
                } else {
                    document.getElementById('status').textContent = 
                        `エラー: ${data.message}`;
                }
            } catch (error) {
                document.getElementById('status').textContent = 
                    `エラー: ${error.message}`;
            }
        }

        async function takeoff() {
            try {
                const response = await fetch(`${API_URL}/takeoff`, {
                    method: 'POST'
                });
                const data = await response.json();
                alert(data.message || data.status);
            } catch (error) {
                alert(`エラー: ${error.message}`);
            }
        }

        async function land() {
            try {
                const response = await fetch(`${API_URL}/land`, {
                    method: 'POST'
                });
                const data = await response.json();
                alert(data.message || data.status);
            } catch (error) {
                alert(`エラー: ${error.message}`);
            }
        }

        async function move(direction, distance) {
            try {
                const response = await fetch(`${API_URL}/move/${direction}/${distance}`, {
                    method: 'POST'
                });
                const data = await response.json();
                
                if (data.status === 'success') {
                    console.log(data.message);
                } else {
                    alert(`エラー: ${data.message}`);
                }
            } catch (error) {
                alert(`エラー: ${error.message}`);
            }
        }
    </script>
</body>
</html>
```

## 🚀 実行方法

### 1. APIサーバーを起動

まず、ターミナルで以下のコマンドを実行してAPIサーバーを起動します：

```bash
python api_server.py
```

### 2. Telloに接続

Telloのスイッチを入れて、Wi-Fiに接続します。

### 3. HTMLファイルを開く

`controller.html` をブラウザで開きます。

*   ファイルをダブルクリック、または
*   ブラウザにドラッグ&ドロップ

### 4. ドローンを操作

1. 「Telloに接続」ボタンをクリック
2. 接続成功のメッセージとバッテリー残量が表示されます
3. 「離陸」ボタンでドローンが離陸します
4. 移動ボタンでドローンを操作できます
5. 「着陸」ボタンで着陸します

## 🔍 コードの解説

### Fetch APIの使用

```javascript
const response = await fetch(`${API_URL}/connect`, {
    method: 'POST'
});
const data = await response.json();
```

*   `fetch()`: HTTPリクエストを送信する関数
*   `await`: 非同期処理の完了を待つ
*   `.json()`: レスポンスをJSON形式で取得

### CORSとは

CORS（Cross-Origin Resource Sharing）は、異なるオリジン（ドメイン）間での通信を制御する仕組みです。

*   ブラウザで開いたHTMLファイル: `file://` オリジン
*   APIサーバー: `http://localhost:8000` オリジン

この2つは異なるオリジンなので、CORSの設定が必要です。

### CSSグリッドレイアウト

```css
.button-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}
```

ボタンを3列のグリッドで配置しています。これにより、十字キー風のレイアウトが実現できます。

## 🎓 やってみよう！

1. **ボタンの色を変えてみよう**
   - CSS部分の `background-color` を変更してみる

2. **新しい操作ボタンを追加してみよう**
   - 回転ボタンを追加する
   - 移動距離を変更できるスライダーを追加する

3. **カメラ映像も表示してみよう**
   - Step 4のカメラストリームをWebSocketで配信
   - HTMLに `<img>` タグで表示

## ⚠️ トラブルシューティング

### ボタンを押しても反応しない

*   APIサーバーが起動しているか確認してください
*   ブラウザの開発者ツール（F12キー）でエラーを確認してください

### CORSエラーが出る

*   `api_server.py` にCORS設定が追加されているか確認してください
*   サーバーを再起動してみてください

## 🎉 おめでとうございます！

ブラウザから操作できるドローンコントローラーを作成できました！
次は [Step 6](../step-06-object-tracking) で、画像処理を使った物体追跡に挑戦しましょう。
