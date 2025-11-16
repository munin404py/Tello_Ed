# Step 2: 基本的な飛行制御

## 🎯 このステップの目標

ドローンを離陸させ、少し動かして、着陸させることができるようになりましょう。
Telloを実際に空中で操作する、最初の一歩です！

> **💡 Python初心者の方へ**: このレッスンでは `import`, `if文`, `time.sleep()` などの基本的なPython構文を使います。これらがよくわからない場合は、[Step 0: Pythonの基本](../step-0-python-basics) を先に学習することをお勧めします！

## 📝 学習内容

*   ドローンの離陸（takeoff）と着陸（land）
*   基本的な移動コマンド（前後左右、上下、回転）
*   安全な飛行のための注意点

## ⚠️ 飛行前の安全確認

**必ず以下を確認してから飛行させてください：**

1. ✅ 周囲に十分な空間がある（最低でも2m四方の空間）
2. ✅ 天井の高さが2.5m以上ある
3. ✅ 周りに人やペット、壊れやすいものがない
4. ✅ バッテリー残量が50%以上ある
5. ✅ プロペラに異常がない
6. ✅ 屋内で飛行する（屋外は風の影響を受けやすい）

## 💻 サンプルコード

`basic_flight.py` というファイル名で、以下のコードを作成してみましょう。

```python
from djitellopy import Tello
import time

# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
print("Telloに接続中...")
tello.connect()

# バッテリー残量を確認
battery = tello.get_battery()
print(f"バッテリー残量: {battery}%")

if battery < 50:
    print("警告: バッテリー残量が少ないです。充電してください。")
    exit()

# 離陸
print("離陸します...")
tello.takeoff()
time.sleep(3)  # 3秒待機（安定するまで）

# 上に20cm移動
print("上昇します...")
tello.move_up(20)
time.sleep(2)

# 前に30cm移動
print("前進します...")
tello.move_forward(30)
time.sleep(2)

# 時計回りに90度回転
print("回転します...")
tello.rotate_clockwise(90)
time.sleep(2)

# 後ろに30cm移動（元の位置に戻る）
print("後退します...")
tello.move_back(30)
time.sleep(2)

# 反時計回りに90度回転（元の向きに戻る）
print("回転します...")
tello.rotate_counter_clockwise(90)
time.sleep(2)

# 着陸
print("着陸します...")
tello.land()

print("飛行完了！")
```

## 🚀 実行方法

1. **安全確認をもう一度行います**（周囲の安全確保！）
2. Telloのスイッチを入れて、Wi-Fiに接続します
3. ドローンを平らな場所に置きます
4. ターミナルで以下のコマンドを実行します：

```bash
python basic_flight.py
```

## ✅ 期待される動作

1. ドローンが自動的に離陸します
2. 少し上昇します
3. 前に進みます
4. 右を向きます
5. 後ろに進みます（元の位置付近に戻ります）
6. 元の向きに戻ります
7. 自動的に着陸します

## 🔍 コードの詳しい解説

### モジュールのインポート

```python
from djitellopy import Tello
import time
```

*   **`import time`**: `time` モジュールをインポート
*   `time.sleep()` を使うために必要

💡 **timeモジュールとは？**:
*   時間に関する機能を提供するPython標準ライブラリ
*   `sleep()` 関数で、指定した秒数だけプログラムを一時停止できる

### バッテリーチェックと条件分岐

```python
battery = tello.get_battery()
print(f"バッテリー残量: {battery}%")

if battery < 50:
    print("警告: バッテリー残量が少ないです。充電してください。")
    exit()
```

*   **`if battery < 50:`**: もしバッテリーが50%未満なら
*   **`exit()`**: プログラムを終了する

💡 **if文の仕組み**:
*   条件が真（True）のとき、インデントされた部分が実行される
*   `<` は「より小さい」という比較演算子
*   安全のため、バッテリーが少ないときは飛行させない

**比較演算子の例**:
```python
battery < 50   # 50より小さい
battery > 80   # 80より大きい
battery <= 50  # 50以下
battery >= 80  # 80以上
battery == 50  # 50と等しい
battery != 50  # 50と等しくない
```

### 離陸と着陸

```python
tello.takeoff()  # 離陸（自動的に約1mの高さまで上昇）
tello.land()     # 着陸（その場に降りる）
```

*   `takeoff()`: ドローンが自動的に安全な高さ（約1m）まで上昇
*   `land()`: その場に着陸する

### 移動コマンド（単位: cm）

```python
tello.move_up(x)       # 上に x cm 移動
tello.move_down(x)     # 下に x cm 移動
tello.move_forward(x)  # 前に x cm 移動
tello.move_back(x)     # 後ろに x cm 移動
tello.move_left(x)     # 左に x cm 移動
tello.move_right(x)    # 右に x cm 移動
```

*   **x**: 移動距離（センチメートル）
*   **範囲**: 20〜500 cmまで指定できます
*   20cm未満の移動は失敗することがあります

**使用例**:
```python
tello.move_forward(30)  # 前に30cm移動
tello.move_up(20)       # 上に20cm移動
```

### 回転コマンド（単位: 度）

```python
tello.rotate_clockwise(x)          # 時計回りに x 度回転
tello.rotate_counter_clockwise(x)  # 反時計回りに x 度回転
```

*   **x**: 回転角度（度数法）
*   **範囲**: 1〜360度まで指定できます
*   **clockwise**: 時計回りの意味
*   **counter_clockwise**: 反時計回りの意味

**使用例**:
```python
tello.rotate_clockwise(90)  # 時計回りに90度（右を向く）
tello.rotate_counter_clockwise(180)  # 反時計回りに180度（後ろを向く）
```

### 待機（sleep）

```python
time.sleep(2)  # 2秒待機
```

*   プログラムを指定した秒数だけ一時停止する
*   ドローンが移動を完了するまで待つために使う

💡 **なぜsleep()が必要？**:
*   ドローンに「前に進め」と命令しても、実際に移動するには時間がかかる
*   次の命令を出す前に、前の動作が完了するのを待つ必要がある
*   `sleep()` を入れないと、ドローンが命令についていけなくなる

**sleepの例**:
```python
tello.move_forward(30)
time.sleep(2)  # 移動が完了するまで2秒待つ
tello.move_up(20)
time.sleep(2)  # 次の移動が完了するまで2秒待つ
```

## 🎓 やってみよう！

コードが動いたら、以下のことを試してみましょう：

1. **正方形を描いて飛行してみよう**
   - 前進 → 右回転90度 → 前進 → 右回転90度 → ...を繰り返す

2. **移動距離を変えてみよう**
   - `move_forward` の数値を50や100に変更してみる

3. **緊急着陸を試してみよう**
   ```python
   tello.emergency()  # 即座にモーターを停止（緊急時のみ使用！）
   ```

## ⚠️ トラブルシューティング

### ドローンが応答しない場合

*   一度 `tello.land()` を実行してみてください
*   それでも反応しない場合は、Telloの電源を切って再起動してください

### 途中で止まってしまう場合

*   バッテリー残量を確認してください
*   `time.sleep()` の時間を長めに設定してみてください

### コマンドが失敗する場合

*   移動距離が小さすぎる（20cm未満）と失敗することがあります
*   移動距離を 20〜100cm の範囲で指定してみてください

## 🎉 おめでとうございます！

基本的な飛行制御ができるようになりました！
次は [Step 3](../step-03-web-api) で、Web APIを使ってブラウザからドローンを操作してみましょう。
