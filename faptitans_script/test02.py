import pyautogui


def has_mask_layer():
    mask_layer = "detection_img/mask_layer2.png"
    # 开箱子
    location = pyautogui.locateOnScreen(image=mask_layer)
    print(location)
    return location is not None


if __name__ == '__main__':
    hml = has_mask_layer()
    print(hml)
