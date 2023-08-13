import win32gui
import win32con
import win32api
import time

ret = win32api.ShellExecute(1, 'open', r'C:\Users\xiaox\Desktop\test.txt', '', '', 1)
print('正在打开软件...')
time.sleep(2)
handle = win32gui.FindWindow(None, r'D:\test.txt - Notepad++')
handleEdit = win32gui.FindWindowEx(handle, None, 'Scintilla', None)

menu = win32gui.GetMenu(handle)
subMenu = win32gui.GetSubMenu(menu, 0)

mystring = ['北国风光，千里冰封，万里雪飘。',
            '望长城内外，惟余莽莽；大河上下，顿失滔滔。',
            '山舞银蛇，原驰蜡象，欲与天公试比高。',
            '须晴日，看红装素裹，分外妖娆。',
            '江山如此多娇，引无数英雄竞折腰。',
            '惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。',
            '一代天骄，成吉思汗，只识弯弓射大雕。',
            '俱往矣，数风流人物，还看今朝。', '《沁园春·雪》']
for index, i in enumerate(mystring):
    for ch in i:
        print(ch)
        win32gui.SendMessage(handleEdit, win32con.WM_CHAR, ord(ch), 0)
        time.sleep(0.05)

    # 模拟按下回车键的操作
    win32api.keybd_event(13, 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

# 获取保存按钮
cmdId = win32gui.GetMenuItemID(subMenu, 6)
# 点击保存
win32gui.PostMessage(handle, win32con.WM_COMMAND, cmdId, 0)
# 关闭窗口
win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)



