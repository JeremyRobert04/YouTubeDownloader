##
## PERSONAL PROJECT, 2022
## YouTubeDownloader
## File description:
## tkinter GUI
##

import tkinter as tk
import script
import darktheme.detect_theme as detect_theme
from PIL import Image, ImageTk

def run_app():
    root = tk.Tk()

    root.geometry("1024x768")
    root.update()

    root.wm_iconbitmap("templates/Icon.ico")
    root.wm_title("Youtube Video Downloader")
    root.resizable(False, False)
    detect_theme.check_dark_theme()

    root.mainloop()