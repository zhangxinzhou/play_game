from tqdm import tqdm
from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import time
import cv2


def face_detect(img, cascade_name):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    face_cascade = cv2.CascadeClassifier(cascade_name)
    faces = face_cascade.detectMultiScale(img)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 5)
    return img


def video_detect(file_name, cascade_name):
    video = cv2.VideoCapture(file_name)  # 视频对象
    fps = video.get(cv2.CAP_PROP_FPS)  # 帧
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')  # 指定视频的编码方式
    video_writer = cv2.VideoWriter('result.mp4', 0x7634706D, fps, (w, h))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in tqdm(range(frame_count)):  # 帧率遍历
        success, img = video.read()  # 读取视频帧
        img = face_detect(img, cascade_name)  # 帧检测
        video_writer.write(img)  # 视频对象写入


def game_detect(game_title, cascade_name, img_show=True):
    hwnd = win32gui.FindWindow(None, game_title)
    if hwnd == 0:
        print('can not find [{}]'.format(game_title))
        # print('exit')
        # exit()
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    while True:
        t0 = time.time()
        q_pix_map = screen.grabWindow(hwnd)
        img_name = 'buff.jpg'
        q_pix_map.save(img_name)
        img_mat0 = cv2.imread(img_name)
        img_mat1 = face_detect(img_mat0, cascade_name)
        t1 = time.time()
        cost = 1000 * (t1 - t0)
        if img_show:
            text = 'hwnd : {} ,cost : {:.6f} ms'.format(hwnd, cost)
            cv2.putText(img_mat1, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('window', img_mat1)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    # video_detect('video/test.mp4', 'cascade/haarcascade_frontalcatface.xml')

    # 总而言之,效果不理想,每帧识别大概需要0.1~1s不能满足需求
    game_title = r'1.mkv - VLC media player000'
    cascade_name = 'cascade/haarcascade_frontalface_default.xml'
    game_detect(game_title, cascade_name)
