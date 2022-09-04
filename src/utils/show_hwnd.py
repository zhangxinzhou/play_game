# 显示所有窗口的句柄和标题
import win32gui
import win32process

hwnd_set = set()


def get_all_hwnd(hwnd, params):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_set.add(hwnd)


win32gui.EnumWindows(get_all_hwnd, 0)
sss = "[{:>10}] [{:>10}] [{:>10}] [{:>10}] [{}]".format('hwnd_item', 'hwnd_ord', 'thread_id', 'process_id',
                                                        'hwnd_title')
print(sss)
for hwnd_item in hwnd_set:
    hwnd_ord = '%#x' % hwnd_item
    hwnd_title = win32gui.GetWindowText(hwnd_item)
    thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd_item)  # 获取窗口ID
    sss = "[{:>10}] [{:>10}] [{:>10}] [{:>10}] [{}]".format(hwnd_item, hwnd_ord, thread_id, process_id, hwnd_title)
    print(sss)
