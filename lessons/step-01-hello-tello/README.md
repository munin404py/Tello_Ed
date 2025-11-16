# Step 1: こんにちは、Tello！

## 🎯 このステップの目標

Telloドローンに初めて接続し、バッテリー残量を取得してみましょう。
これが、あなたとTelloの最初のコミュニケーションです！

## 📝 学習内容

*   Telloドローンとの接続方法
*   `djitellopy` ライブラリの基本的な使い方
*   ドローンの状態情報（バッテリー残量など）の取得方法

## 🔧 準備

### 必要なライブラリのインストール

まず、Pythonで Tello を制御するためのライブラリをインストールします。

```bash
pip install djitellopy
```

### Telloとの接続

1. Telloドローンの電源を入れます（本体側面のボタンを押します）
2. ドローンのLEDが点滅を始めたら、PCのWi-Fi設定画面を開きます
3. `TELLO-XXXXXX` という名前のWi-Fiネットワークを探して接続します
   - パスワードは不要です

## 💻 サンプルコード

`hello_tello.py` というファイル名で、以下のコードを作成してみましょう。

```python
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
```

## 🚀 実行方法

1. Telloのスイッチを入れて、Wi-Fiに接続します
2. ターミナル（コマンドプロンプト）で以下のコマンドを実行します：

```bash
python hello_tello.py
```

## ✅ 期待される結果

正常に動作すると、以下のような出力が表示されます：

```
Telloに接続中...
バッテリー残量: 85%
接続を終了しました。
```

※ バッテリー残量の数値は、ドローンの実際の残量によって変わります。

## 🔍 コードの解説

```python
from djitellopy import Tello
```
`djitellopy` ライブラリから `Tello` クラスをインポートします。
これがドローンを制御するためのメインクラスです。

```python
tello = Tello()
```
Telloオブジェクトを作成します。これがドローンとやり取りするための入口です。

```python
tello.connect()
```
ドローンとの接続を確立します。この命令が実行されると、Telloとの通信が開始されます。

```python
battery = tello.get_battery()
```
ドローンのバッテリー残量を取得します。返り値は整数で、パーセンテージを表します。

## 🎓 やってみよう！

コードが動いたら、以下のことを試してみましょう：

1. **温度も取得してみよう**
   ```python
   temp = tello.get_temperature()
   print(f"温度: {temp}°C")
   ```

2. **高度を取得してみよう（地上にいるので0が返るはず）**
   ```python
   height = tello.get_height()
   print(f"現在の高度: {height}cm")
   ```

3. **飛行時間を取得してみよう**
   ```python
   flight_time = tello.get_flight_time()
   print(f"飛行時間: {flight_time}秒")
   ```

## ⚠️ トラブルシューティング

### 「接続できない」というエラーが出る場合

*   PCがTelloのWi-Fiに正しく接続されているか確認してください
*   ファイアウォールがブロックしている可能性があります
*   ドローンの電源を一度切って、再度入れ直してみてください

### バッテリー残量が20%以下の場合

*   安全のため、バッテリーを充電してから実験を続けましょう

## 🎉 おめでとうございます！

Telloとの最初の接続に成功しました！
次は [Step 2](../step-02-basic-movement) で、実際にドローンを飛ばしてみましょう。
