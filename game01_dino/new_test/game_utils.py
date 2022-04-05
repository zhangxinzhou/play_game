import numpy as np
import cv2


def qpixmap_to_array(qtpixmap):
    img = qtpixmap.toImage()
    temp_shape = (img.height(), img.bytesPerLine() * 8 // img.depth())
    temp_shape += (4,)
    ptr = img.bits()
    ptr.setsize(img.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result


def img_to_candy(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_candy = cv2.Canny(img_gray, 100, 200)
    return img_candy
