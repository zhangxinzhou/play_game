# -*- coding: utf-8 -*-
import win32process  # 进程模块
from win32con import PROCESS_ALL_ACCESS  # Opencress 权限
import win32api  # 调用系统模块
import ctypes  # C语言类型
from win32gui import FindWindow  # 界面


def read_memory_val_by_hwnd(hwnd, address, byte_length):
    if hwnd is None or hwnd == 0:
        raise ValueError("hwnd can not be None or 0")
    thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)  # 获取窗口ID
    process_hwnd = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)  # 获取进程句柄
    addr = ctypes.c_ulong()
    ctypes.windll.kernel32.ReadProcessMemory(int(process_hwnd), address, ctypes.byref(addr), byte_length, None)  # 读内存
    win32api.CloseHandle(process_hwnd)  # 关闭句柄
    return addr.value


def read_memory_val_by_win_name(win_name, address, byte_length):
    # 获取窗口句柄
    hwnd = FindWindow(None, win_name)
    return read_memory_val_by_hwnd(hwnd, address, byte_length)


if __name__ == '__main__':
    game_name = "MAME: 打击者 1945 [s1945]"
    xxx = 0x0F4E1194
    val = read_memory_val_by_win_name(game_name, xxx, 4);
    print(val)
