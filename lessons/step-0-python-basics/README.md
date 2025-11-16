# Step 0: Python の基本

## 🎯 このステップの目標

Telloドローンを動かす前に、Pythonプログラミングの基本を学びましょう。
ここで学ぶ内容は、このあとのすべてのレッスンで使います！

## 📝 学習内容

*   変数とデータ型
*   文字列とf文字列
*   関数の使い方
*   クラスとオブジェクト
*   モジュールとインポート

---

## 1. 変数 - 値を入れる「箱」

**変数** は、データを入れておく「箱」のようなものです。箱に名前（変数名）をつけて、後で使えるようにします。

### 変数の基本

```python
# 変数に値を代入する
name = "太郎"
age = 20
height = 175.5

# 変数を使う
print(name)    # 太郎
print(age)     # 20
print(height)  # 175.5
```

### ルール

*   **変数名は自由につけられる**（日本語も使えるけど、英語が推奨）
*   **=（イコール）** で値を代入する
*   **#（ハッシュ）** の後ろはコメント（メモ）で、プログラムとして実行されない

### データ型

変数には、いろんな種類の値を入れられます：

```python
# 文字列（str）: 文字の並び
name = "花子"

# 整数（int）: 小数点のない数字
age = 25

# 浮動小数点数（float）: 小数点のある数字
temperature = 36.5

# 真偽値（bool）: True（正しい）か False（間違い）
is_student = True
```

---

## 2. 文字列 - 文字の扱い方

### 文字列の基本

```python
# シングルクォート、ダブルクォート、どちらでもOK
message1 = 'こんにちは'
message2 = "さようなら"

# 文字列を連結する
greeting = "こんにちは、" + "世界！"
print(greeting)  # こんにちは、世界！
```

### f文字列 - 変数を埋め込む便利な方法 ⭐

**f文字列（フォーマット文字列）** は、文字列の中に変数の値を埋め込む、とても便利な方法です。

```python
name = "太郎"
age = 20

# 古い方法（読みにくい）
message = "私の名前は" + name + "です。年齢は" + str(age) + "歳です。"

# f文字列（読みやすい！）⭐
message = f"私の名前は{name}です。年齢は{age}歳です。"
print(message)  # 私の名前は太郎です。年齢は20歳です。
```

**ポイント**:
*   文字列の前に `f` をつける
*   変数を `{変数名}` で囲む
*   自動的に文字列に変換してくれる

### f文字列の応用

```python
battery = 85
# パーセント記号も一緒に表示
print(f"バッテリー残量: {battery}%")

# 計算もできる
width = 100
height = 50
print(f"面積は {width * height} です")

# 小数点以下の桁数を指定
pi = 3.14159
print(f"円周率は約 {pi:.2f} です")  # 3.14（小数点以下2桁）
```

---

## 3. リスト - 複数の値をまとめて管理

**リスト** は、複数の値を順番に並べて管理できる「箱」です。

```python
# リストの作成
fruits = ["りんご", "バナナ", "オレンジ"]

# 要素にアクセス（0から数える！）
print(fruits[0])  # りんご
print(fruits[1])  # バナナ

# 要素を追加
fruits.append("ぶどう")
print(fruits)  # ['りんご', 'バナナ', 'オレンジ', 'ぶどう']

# リストの長さ
print(len(fruits))  # 4
```

---

## 4. 関数 - 処理をまとめる

**関数** は、何度も使う処理をまとめて、名前をつけたものです。

### 関数の定義と呼び出し

```python
# 関数を定義する
def greet(name):
    """挨拶する関数"""
    print(f"こんにちは、{name}さん！")

# 関数を呼び出す
greet("太郎")  # こんにちは、太郎さん！
greet("花子")  # こんにちは、花子さん！
```

**ポイント**:
*   `def` で関数を定義する
*   `( )` の中に **パラメータ（引数）** を書く
*   `:` の後に、実行する処理を書く
*   **インデント（字下げ）** が重要！

### 戻り値のある関数

```python
def add(a, b):
    """2つの数を足す関数"""
    result = a + b
    return result  # 結果を返す

# 関数の戻り値を変数に代入
sum_value = add(10, 20)
print(sum_value)  # 30
```

### デフォルト引数

```python
def greet(name, greeting="こんにちは"):
    """挨拶する関数（デフォルトは「こんにちは」）"""
    print(f"{greeting}、{name}さん！")

greet("太郎")              # こんにちは、太郎さん！
greet("花子", "おはよう")   # おはよう、花子さん！
```

---

## 5. クラスとオブジェクト - 設計図と実体

**クラス** は、「もの」を作るための設計図です。
**オブジェクト** は、その設計図から作られた実際の「もの」です。

### なぜクラスが必要？

例えば、「犬」という概念を考えてみましょう：
*   すべての犬には **名前**、**年齢**、**種類** がある
*   すべての犬は **吠える**、**走る** ことができる

これを設計図（クラス）にしておけば、ポチ君もコロ君も同じ構造で作れます。

### クラスの基本

```python
# クラスを定義（設計図を作る）
class Dog:
    """犬クラス"""
    
    def __init__(self, name, age):
        """初期化メソッド（コンストラクタ）"""
        self.name = name  # 属性（プロパティ）
        self.age = age
    
    def bark(self):
        """吠えるメソッド"""
        print(f"{self.name}がワンワン！と吠えました。")
    
    def run(self):
        """走るメソッド"""
        print(f"{self.name}が走っています！")

# オブジェクトを作る（設計図から実体を作る）
pochi = Dog("ポチ", 3)
coro = Dog("コロ", 5)

# メソッドを呼び出す
pochi.bark()  # ポチがワンワン！と吠えました。
coro.run()    # コロが走っています！

# 属性にアクセス
print(f"{pochi.name}は{pochi.age}歳です")  # ポチは3歳です
```

### 重要な用語

*   **クラス**: 設計図（`Dog`）
*   **オブジェクト（インスタンス）**: 設計図から作った実体（`pochi`, `coro`）
*   **属性（プロパティ）**: オブジェクトが持つデータ（`name`, `age`）
*   **メソッド**: オブジェクトができる動作（`bark()`, `run()`）
*   **`__init__`**: オブジェクトを作るときに最初に実行される特殊なメソッド
*   **`self`**: 「自分自身」を指す特別な変数

### Telloでの例

```python
from djitellopy import Tello

# Tello クラスからオブジェクトを作る
tello = Tello()

# メソッドを呼び出す
tello.connect()       # 接続する
tello.takeoff()       # 離陸する

# 属性にアクセス
battery = tello.get_battery()
```

これと同じ構造です！

---

## 6. クラスの継承 - 既存のクラスを拡張する

**継承** は、既存のクラスをベースに、新しい機能を追加したクラスを作ることです。

### 継承の基本

```python
# 親クラス（基底クラス）
class Animal:
    """動物クラス"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """鳴く（共通の動作）"""
        print(f"{self.name}が何か言いました。")

# 子クラス（派生クラス）- Animalを継承
class Dog(Animal):
    """犬クラス（Animalを継承）"""
    
    def speak(self):
        """鳴く（犬バージョン）"""
        print(f"{self.name}がワンワン！")

class Cat(Animal):
    """猫クラス（Animalを継承）"""
    
    def speak(self):
        """鳴く（猫バージョン）"""
        print(f"{self.name}がニャー！")

# 使ってみる
pochi = Dog("ポチ")
tama = Cat("タマ")

pochi.speak()  # ポチがワンワン！
tama.speak()   # タマがニャー！
```

**メリット**:
*   共通部分（`name`）を何度も書かなくて済む
*   親クラスの機能を引き継ぎつつ、独自の機能を追加できる

### 継承の例（Telloでのイメージ）

```python
# もし自分でカスタムTelloクラスを作るなら...
class MyTello(Tello):
    """Telloクラスを継承した自分専用クラス"""
    
    def safe_takeoff(self):
        """バッテリーをチェックしてから離陸"""
        battery = self.get_battery()
        if battery < 30:
            print("バッテリー残量が少ないため、離陸できません。")
        else:
            print("バッテリーOK！離陸します。")
            self.takeoff()

# 使う
my_tello = MyTello()
my_tello.connect()
my_tello.safe_takeoff()  # 自分で追加したメソッド
```

---

## 7. モジュールとインポート - 他の人のコードを使う

**モジュール** は、Pythonプログラムが書かれたファイルです。
**インポート** は、他のファイルの機能を自分のプログラムで使えるようにすることです。

### 標準ライブラリのインポート

```python
# timeモジュールをインポート
import time

print("3秒待ちます...")
time.sleep(3)  # 3秒間停止
print("待機完了！")
```

### 特定の関数だけインポート

```python
# timeモジュールからsleep関数だけをインポート
from time import sleep

print("2秒待ちます...")
sleep(2)  # time.sleep(2) と書かなくてOK
print("完了！")
```

### 外部ライブラリのインポート

```python
# djitellopyライブラリからTelloクラスをインポート
from djitellopy import Tello

tello = Tello()
tello.connect()
```

### asで別名をつける

```python
# 長い名前を短くする
import numpy as np

# np という短い名前で使える
array = np.array([1, 2, 3])
```

---

## 8. 制御構文 - プログラムの流れを制御する

### if文 - 条件分岐

```python
battery = 50

if battery > 80:
    print("バッテリー十分！")
elif battery > 30:
    print("バッテリーそこそこ。")
else:
    print("バッテリー少ない。充電してね。")
```

### for文 - 繰り返し

```python
# リストの各要素に対して処理
fruits = ["りんご", "バナナ", "オレンジ"]
for fruit in fruits:
    print(f"私は{fruit}が好きです")

# 範囲指定の繰り返し
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"{i}回目の繰り返し")
```

### while文 - 条件を満たす間ずっと繰り返し

```python
count = 0
while count < 3:
    print(f"カウント: {count}")
    count += 1  # count = count + 1 と同じ
```

---

## 9. エラーと例外処理

プログラムを書いていると、エラー（例外）が起きることがあります。
**try-except** を使うと、エラーが起きても プログラムが止まらないようにできます。

```python
try:
    # エラーが起きるかもしれない処理
    number = int(input("数字を入力してください: "))
    result = 100 / number
    print(f"結果: {result}")
except ValueError:
    # 数字以外が入力された場合
    print("エラー: 数字を入力してください")
except ZeroDivisionError:
    # 0で割ろうとした場合
    print("エラー: 0では割れません")
except Exception as e:
    # その他のエラー
    print(f"予期しないエラーが発生: {e}")
```

### Telloでの例

```python
try:
    tello = Tello()
    tello.connect()
    battery = tello.get_battery()
    print(f"バッテリー: {battery}%")
except Exception as e:
    print(f"接続エラー: {e}")
    print("Telloの電源とWi-Fi接続を確認してください")
```

---

## 10. 実践：これまでの知識を組み合わせる

それでは、これまで学んだことを全部使ってみましょう！

### 練習問題

`python_practice.py` というファイルを作って、以下のコードを試してみてください：

```python
# モジュールをインポート
import time

# クラスを定義
class Robot:
    """ロボットクラス"""
    
    def __init__(self, name, energy):
        """初期化"""
        self.name = name
        self.energy = energy
    
    def introduce(self):
        """自己紹介"""
        print(f"私の名前は{self.name}です。")
        print(f"エネルギー残量は{self.energy}%です。")
    
    def charge(self, amount):
        """充電する"""
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        print(f"{amount}%充電しました。現在{self.energy}%です。")
    
    def work(self, hours):
        """仕事をする"""
        energy_used = hours * 10
        if self.energy >= energy_used:
            self.energy -= energy_used
            print(f"{hours}時間働きました。エネルギー残量: {self.energy}%")
        else:
            print("エネルギー不足！充電してください。")

# メイン処理
print("=== ロボットシミュレーター ===\n")

# ロボットを作成
robot = Robot("ロボ太郎", 80)

# 自己紹介
robot.introduce()
print()

# 仕事をする
robot.work(3)
time.sleep(1)  # 1秒待機

robot.work(5)
time.sleep(1)

# 充電する
robot.charge(50)
time.sleep(1)

# また仕事をする
robot.work(7)

print("\n=== シミュレーション終了 ===")
```

### 実行してみよう

```bash
python python_practice.py
```

### 期待される出力

```
=== ロボットシミュレーター ===

私の名前はロボ太郎です。
エネルギー残量は80%です。

3時間働きました。エネルギー残量: 50%
5時間働きました。エネルギー残量: 0%
50%充電しました。現在50%です。
エネルギー不足！充電してください。

=== シミュレーション終了 ===
```

---

## 11. よく使う組み込み関数

Pythonには、最初から使える便利な関数がたくさんあります：

```python
# print() - 画面に表示
print("こんにちは")

# len() - 長さを取得
fruits = ["りんご", "バナナ", "オレンジ"]
print(len(fruits))  # 3

# type() - データ型を確認
print(type(10))      # <class 'int'>
print(type("hello")) # <class 'str'>

# input() - ユーザー入力を受け取る
name = input("名前を入力してください: ")
print(f"こんにちは、{name}さん！")

# range() - 連番を生成
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# str(), int(), float() - 型変換
num_str = "123"
num_int = int(num_str)  # 文字列を整数に
print(num_int + 10)     # 133
```

---

## 🎓 やってみよう！

1. **f文字列を使った自己紹介プログラムを作ろう**
   ```python
   name = "あなたの名前"
   age = 20
   hobby = "プログラミング"
   
   print(f"私の名前は{name}で、{age}歳です。")
   print(f"趣味は{hobby}です。")
   ```

2. **関数を使った計算機を作ろう**
   ```python
   def calculate(a, b, operation):
       if operation == "+":
           return a + b
       elif operation == "-":
           return a - b
       elif operation == "*":
           return a * b
       elif operation == "/":
           return a / b
   
   result = calculate(10, 5, "+")
   print(result)  # 15
   ```

3. **簡単なクラスを作ってみよう**
   - 好きなもの（車、ペット、スマホなど）をクラスにしてみる
   - 属性とメソッドを考えて実装してみる

---

## ✅ このステップで学んだことチェック

- [ ] 変数を使ってデータを保存できる
- [ ] f文字列を使って変数を文字列に埋め込める
- [ ] 関数を定義して呼び出せる
- [ ] クラスとオブジェクトの概念を理解している
- [ ] 継承が何かを理解している
- [ ] モジュールをインポートして使える
- [ ] if文、for文、while文を使える
- [ ] try-exceptでエラー処理ができる

---

## 🎉 おめでとうございます！

Pythonの基本を学びました！
これで、Telloドローンのプログラムを読んで理解できるようになりました。

次は [Step 1](../step-01-hello-tello) で、実際にTelloドローンに接続してみましょう！
