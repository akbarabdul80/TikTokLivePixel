import os
import platform


def get_dir():
    file_name = "emulator.png"
    dir_file = os.getcwd()
    if platform.system() == "linux" or platform.system() == "linux2" or platform.system() == "win64" or platform.system() == "win32":
        return dir_file + "\\ss\\" + file_name
    elif platform.system() == "Darwin":
        return dir_file + "/ss/" + file_name
