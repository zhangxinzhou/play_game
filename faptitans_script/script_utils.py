import os
import pyautogui

MASK_LAYER_PATH = "detection_img/mask_layer.png"
PROMPT_PATH = "detection_img"


# 点击图片
def click_img(img_path, confidence=0.95, last_location_x=100, last_location_y=100):
    is_click = False
    location = pyautogui.locateOnScreen(image=img_path, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        pyautogui.moveTo(x=last_location_x, y=last_location_y)
        is_click = True
    # 移动到某个位置,防止阻挡图层
    return is_click


# 判断是否有遮罩层
def click_able():
    location = pyautogui.locateOnScreen(image=MASK_LAYER_PATH, confidence=0.95)
    if location is not None:
        x, y = pyautogui.center(location)
        return pyautogui.pixelMatchesColor(int(x), int(y), (255, 87, 87))
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


if __name__ == '__main__':
    location = pyautogui.locateOnScreen(image=MASK_LAYER_PATH, confidence=0.95)
    if location is not None:
        x, y = pyautogui.center(location)
        tmp = pyautogui.pixel(int(x), int(y))
        print(tmp)
        # return pyautogui.pixelMatchesColor(int(x), int(y), (255, 255, 255))
