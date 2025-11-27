from checker import detect_os
from linux_handler import LinuxHandler
from macos_handler import MacOSHandler
from windows_handler import WindowsHandler
from base import OSHandler

def get_handler() -> OSHandler:
    info = detect_os()

    if info.system == "windows":
        return WindowsHandler()
    elif info.system == "linux":
        return LinuxHandler()
    elif info.system == "macos":
        return MacOSHandler()
    
    raise RuntimeError(f"Unsupported or unknown OS: {info.system} ({info.release}). Contact Developer(Jigit)")