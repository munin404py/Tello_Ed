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
