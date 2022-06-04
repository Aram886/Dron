from threading import Thread
import cv2, time
from djitellopy import Tello

t = Tello()
t.connect()
t.streamon()

def get_udp_video_address(self):
    return 'udp://@' + self.VS_UDP_IP + ':' + str(self.VS_UDP_PORT)  # + '?overrun_nonfatal=1&fifo_size=5000'

def get_video_capture(self):
    if self.cap is None:
        self.cap = cv2.VideoCapture(self.get_udp_video_address())

    if not self.cap.isOpened():
        self.cap.open(self.get_udp_video_address())

    return self.cap


# frame_reader = t.get_frame_read()
# keepRecording = True
# def videoRecorder():
#     video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*'XVID'), 60)
#
#     while keepRecording:
#         video.write(frame_reader.frame)
#         time.sleep(1 / 60)
#
#     video.release()
#
# recorder = Thread(target=videoRecorder)
# recorder.start()

t.takeoff()

get_video_capture()
get_video_capture()

t.move_up(500)
t.move_up(500)

frame_read = t.get_frame_read()

t.move_forward(400)
t.rotate_counter_clockwise(45)
cv2.imwrite("picture1.jpg", frame_read.frame)

t.move_forward(100)
t.rotate_counter_clockwise(45)
cv2.imwrite("picture1.jpg", frame_read.frame)

t.move_forward(100)
t.rotate_counter_clockwise(45)
cv2.imwrite("picture1.jpg", frame_read.frame)

t.streamoff()

t.rotate_counter_clockwise(180)
t.move_forward(400)
t.move_forward(300)

t.land()

# keepRecording = False
# recorder.join()

