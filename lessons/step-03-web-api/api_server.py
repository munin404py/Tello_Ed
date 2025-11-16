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
