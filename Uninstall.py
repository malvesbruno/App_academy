import os
import getpass
from tkinter import messagebox
import sys

res = messagebox.askyesno("Uninstall", "Are you sure you want to uninstall?")
if res:
    USER_NAME = getpass.getuser()
    loc_atual = sys.executable
    loc_atual = str(loc_atual).replace(r"\uninstall.exe", "")
    path = os.listdir(loc_atual)
    with open("loc_saved", "w") as arquivo:
        arquivo.write(f"{loc_atual}")
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    try:
        os.remove(bat_path + "\open_clock.bat")
    except:
        pass
    for c in path:
        pth = loc_atual + f"\{c}"
        print(pth)
        os.remove(pth)
        os.rmdir(loc_atual)
else:
    pass