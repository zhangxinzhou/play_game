import win32gui
import win32con

game_title = 'Grand Theft Auto V'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find [{}]'.format(game_title))
    print('exiting game')
    exit()

# 窗口置顶
win32gui.SetActiveWindow(hwnd)
# 窗口移动到屏幕左上角
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 800, 600, win32con.SWP_SHOWWINDOW)
