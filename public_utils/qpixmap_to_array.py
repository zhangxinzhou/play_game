import numpy as np


def qpixmap_to_array(qtpixmap):
    img = qtpixmap.toImage()
    temp_shape = (img.height(), img.bytesPerLine() * 8 // img.depth())
    temp_shape += (4,)
    ptr = img.bits()
    ptr.setsize(img.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result
