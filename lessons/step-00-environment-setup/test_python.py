"""
Pythonの動作確認用スクリプト

このファイルを実行して、Pythonが正しくインストールされているか確認しましょう。
"""

print("=" * 50)
print("Pythonの動作確認")
print("=" * 50)
print()

# 1. Pythonのバージョンを表示
import sys
print(f"✅ Pythonバージョン: {sys.version}")
print()

# 2. 変数とf文字列のテスト
name = "太郎"
age = 20
print(f"✅ 変数とf文字列が動作しています: {name}さんは{age}歳です")
print()

# 3. 計算のテスト
result = 10 + 20
print(f"✅ 計算ができます: 10 + 20 = {result}")
print()

# 4. リストのテスト
fruits = ["りんご", "バナナ", "オレンジ"]
print(f"✅ リストが動作しています: {fruits}")
print()

# 5. 関数のテスト
def greet(name):
    return f"こんにちは、{name}さん！"

greeting = greet("花子")
print(f"✅ 関数が動作しています: {greeting}")
print()

# 6. モジュールのインポートテスト
import time
import random

print("✅ 標準ライブラリ（time, random）がインポートできました")
print()

# 7. 簡単な動作テスト
print("🎲 サイコロを振ります...")
time.sleep(1)
dice = random.randint(1, 6)
print(f"   出た目: {dice}")
print()

print("=" * 50)
print("すべてのテストが成功しました！ 🎉")
print("Pythonの環境は正しくセットアップされています。")
print("=" * 50)
