import os
import pyautogui

MASK_LAYER_PATH = "detection_img/mask_layer.png"
HERO_SCROLL = "detection_img/hero_scroll.png"
HERO_SCROLL_START = "detection_img/hero_scroll_start.png"
HERO_SCROLL_END = "detection_img/hero_scroll_end.png"
HERO_SCROLL_IS_TOP = False
PROMPT_PATH = "detection_img"


# 点击图片
def click_img(img_path, confidence=0.95, offset=(0, 0)):
    is_click = False
    location = pyautogui.locateOnScreen(image=img_path, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        x_offset = offset[0]
        y_offset = offset[1]
        x = x + x_offset
        y = y + y_offset
        pyautogui.leftClick(x, y)
        is_click = True
    # 移动到某个位置,防止阻挡图层
    return is_click


# 返回某个位置，不影响图片判断
def back_position(last_location_x=100, last_location_y=100):
    x, y = pyautogui.position()
    if x != last_location_x or y != last_location_y:
        pyautogui.moveTo(x=last_location_x, y=last_location_y)


# 判断是否有遮罩层
def click_able():
    location = pyautogui.locateOnScreen(image=MASK_LAYER_PATH, confidence=0.95)
    if location is not None:
        x, y = pyautogui.center(location)
        print(pyautogui.pixel(int(x), int(y)))
        return pyautogui.pixelMatchesColor(int(x), int(y), (255, 84, 84))
    return False


# 获取弹窗图片路径列表
def get_prompt_img_path_list(prefix):
    dir_path = PROMPT_PATH
    img_list = os.listdir(dir_path)
    prompt_img_path_list = []
    for img in img_list:
        if img.startswith(prefix):
            prompt_img_path_list.append(os.path.join(dir_path, img))
    return prompt_img_path_list


# 关闭弹窗
def close_prompt():
    prompt_img_path_list = get_prompt_img_path_list("prompt")
    for img_path in prompt_img_path_list:
        click_result = click_img(img_path)
        if click_result:
            return click_result
    return False


#
def hero_scroll(val):
    global HERO_SCROLL_IS_TOP
    hero_scroll_start_location = pyautogui.locateOnScreen(image=HERO_SCROLL_START)
    hero_scroll_end_location = pyautogui.locateOnScreen(image=HERO_SCROLL_END)
    if hero_scroll_start_location is not None:
        HERO_SCROLL_IS_TOP = True
    elif hero_scroll_end_location is not None:
        HERO_SCROLL_IS_TOP = False
    hero_scroll_location = pyautogui.locateOnScreen(image=HERO_SCROLL)
    if hero_scroll_location is None:
        return
    x, y = pyautogui.center(hero_scroll_location)
    pyautogui.moveTo(x=x, y=y)
    if HERO_SCROLL_IS_TOP:
        val = -1 * val
    pyautogui.scroll(val)


if __name__ == '__main__':
    location = pyautogui.locateOnScreen(image=MASK_LAYER_PATH, confidence=0.95)
    if location is not None:
        x, y = pyautogui.center(location)
        tmp = pyautogui.pixel(int(x), int(y))
        print(tmp)
        # return pyautogui.pixelMatchesColor(int(x), int(y), (255, 255, 255))
