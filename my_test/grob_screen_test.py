from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
import win32gui
import sys
import numpy as np
import cv2
import time


# QPixmap => CvMat
# method from google/baidu
def qtpixmap_to_cvmat(qtpixmap):
    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result


# CvMat => QPixmap
# method from google/baidu
def cvmat_to_qtimg(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

    return cvimg


game_title = r'Grand Theft Auto V'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find [{}]'.format(game_title))
    print('exit')
    # exit()
app = QApplication(sys.argv)
screen = app.primaryScreen()
while True:
    t0 = time.time()
    q_pix_map = screen.grabWindow(hwnd)
    t1 = time.time()
    cost = 1000 * (t1 - t0)
    text = 'hwnd : {} , cost : {:.6f} ms'.format(hwnd, cost)

    mat = qtpixmap_to_cvmat(q_pix_map)
    # FIXME 图片颜色怪异,但如果不写下面代码,则cv2.putText会报错
    mat = cv2.cvtColor(mat, cv2.COLOR_RGB2BGR)
    cv2.putText(mat, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('window', mat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
