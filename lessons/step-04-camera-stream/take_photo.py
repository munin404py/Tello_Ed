from djitellopy import Tello
import cv2
import time

tello = Tello()
tello.connect()
tello.streamon()

# 数秒待ってカメラを安定させる
time.sleep(2)

# フレームを取得
frame = tello.get_frame_read().frame

# 画像として保存
cv2.imwrite("tello_photo.jpg", frame)
print("写真を保存しました: tello_photo.jpg")

tello.streamoff()
