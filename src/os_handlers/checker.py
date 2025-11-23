import platform

def osChecker():
    return f"{platform.system()}, {platform.release()}"