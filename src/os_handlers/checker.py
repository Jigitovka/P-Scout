import platform
from dataclasses import dataclass

@dataclass(frozen=True)
class OSInfo:
    system: str
    release: str
    version: str

# Function for detection OS
def detect_os() -> OSInfo:
    sys_raw = platform.system().lower()
    rel = platform.release()
    ver = platform.version()

    # Normalize
    if sys_raw.startswith("darwin"):
        sys_norm = "macos"
    elif sys_raw.startswith("windows"):
        sys_norm = "windows"
    elif sys_raw.startswith("linux"):
        sys_norm = "linux"
    else:
        sys_norm = "unknown"
    
    return OSInfo(system=sys_norm, release=rel, version=ver)


    