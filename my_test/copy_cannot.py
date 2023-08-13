import pyautogui
from pywubi import wubi
import unicodedata
import time

# 暂停十秒，检查输入法是否是五笔，检查鼠标是否落在输入框中
time.sleep(5)

with open('my_text.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    # 将中文标点转换成英文标点
    line = unicodedata.normalize('NFKC', line)
    print(line)
    # 将中文汉字转换成五笔
    wubi_symbol = wubi(line)
    for word in wubi_symbol:
        # pyautogui.typewrite(word)
        # 如果全是字符说明不是标点符号，就补一个空格来打字
        isWord = word.isalpha()
        pyautogui.typewrite(word)
        if isWord:
            pyautogui.typewrite(" ")
    pyautogui.press("enter")
