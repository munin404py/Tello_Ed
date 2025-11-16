import requests
import time

# 接続
print("Telloに接続中...")
response = requests.post("http://localhost:8000/connect")
print(response.json())

# バッテリー確認
print("\nバッテリー残量を確認中...")
response = requests.get("http://localhost:8000/battery")
print(response.json())

# 離陸
print("\n離陸します...")
response = requests.post("http://localhost:8000/takeoff")
print(response.json())

# 2秒待機
time.sleep(2)

# 着陸
print("\n着陸します...")
response = requests.post("http://localhost:8000/land")
print(response.json())
