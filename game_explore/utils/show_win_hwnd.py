import win32gui


def print_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title = win32gui.GetWindowText(hwnd)
        if hwnd_title != '':
            print(hwnd, hwnd_title)


win32gui.EnumWindows(print_all_hwnd, 0)
