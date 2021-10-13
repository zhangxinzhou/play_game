import win32gui


def _MyCallback(hwnd, extra):
    windows = extra
    temp = []
    temp.append(hex(hwnd))
    temp.append(win32gui.GetClassName(hwnd))
    temp.append(win32gui.GetWindowText(hwnd))
    windows[hwnd] = temp


windows = {}
win32gui.EnumWindows(_MyCallback, windows)
hld = win32gui.FindWindow("TXGuiFoundation", '实时加速工具')

hldb = win32gui.FindWindow("TXGuiFoundation", '实时加速工具2')
