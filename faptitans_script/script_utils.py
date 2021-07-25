# 获取图片坐标是否与提供的颜色匹配
def img_position_match_color(img, xy, expect_color, tolerance=10):
    pixel = img.getpixel(xy)
    r, g, b = pixel[:3]
    ex_r, ex_g, ex_b = expect_color[:3]
    return (abs(r - ex_r) <= tolerance) and (abs(g - ex_g) <= tolerance) and (abs(b - ex_b) <= tolerance)
