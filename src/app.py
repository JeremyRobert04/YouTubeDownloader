##
## PERSONAL PROJECT, 2022
## YouTubeDownloader
## File description:
## main
##

from tkinter import *
from tkinter import messagebox
import customtkinter
from tkinter.filedialog import askdirectory
from pathlib import Path
from pytube import YouTube
from PIL import Image, ImageTk
from io import BytesIO
import urllib.request

URL = "https://youtu.be/AvBv2goo7Ng"
WIDTH = 780
HEIGHT = 520

PATH_TO_DOWNLOAD = str(Path.home() / "Downloads")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Download():
    def __init__(self, url):
        self.yt = YouTube(url)

    def get_title(self):
        title = self.yt.title
        specialChars = "\\/"
        for specialChar in specialChars:
            title = title.replace(specialChar, ' ')
        return title

    def get_thumbnail(self):
        return self.yt.thumbnail_url

    def get_resolution(self):
        resolutions = [int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in self.yt.streams if i.resolution])))]
        resolutions.sort()
        del resolutions[1:-1]
        str_resolution = [str(x) for x in resolutions]
        return str_resolution

    def download_video(self, res="mp3"):
        if res == "Download MP4":
            return
        if res == "mp3":
            try:
                self.yt.streams.get_audio_only().download(PATH_TO_DOWNLOAD, self.get_title() + ".mp3")
            except:
                print("An Error occured when downloading the video to mp3... try again later or contact the owner")
                return
            self.video_download_done()
        else:
            try:
                if self.get_resolution().index(res) == 1:
                    self.yt.streams.get_highest_resolution().download(PATH_TO_DOWNLOAD)
                else:
                    self.yt.streams.get_lowest_resolution().download(PATH_TO_DOWNLOAD)
                self.video_download_done()
            except:
                print("An Error occured... try again later or contact the owner")
                return

    def video_download_done(self):
        messagebox.showinfo("Successfully", "Video correctly downloaded and saved in " + PATH_TO_DOWNLOAD)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Video Downloader")
        self.iconbitmap("Icon.ico")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # LEFT FRAME
        self.frame_left = customtkinter.CTkFrame(master=self, width=0.30 * WIDTH, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(6, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.video_label = customtkinter.CTkLabel(
            master=self.frame_left,
            text="Youtube Video URL:",
            text_font=("Roboto Medium", -16)
        )
        self.video_label.grid(row=2, column=0, pady=20, padx=20, sticky="we")

        self.url_entry = customtkinter.CTkEntry(
            master=self.frame_left,
            width=0.25 * WIDTH,
            placeholder_text="Enter Video URL"
        )
        self.url_entry.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.browse_download = customtkinter.CTkButton(
            master=self.frame_left,
            text="Load",
            width=100,
            command=self.load_youtube
        )
        self.browse_download.grid(row=3, column=1, pady=20, padx=10, sticky="e")

        self.download_label = customtkinter.CTkLabel(
            master=self.frame_left,
            text="Download Folder:",
            text_font=("Roboto Medium", -16)
        )
        self.download_label.grid(row=4, column=0, sticky="we")

        self.path_download = customtkinter.CTkLabel(
            master=self.frame_left,
            width=0.25 * WIDTH,
            text=PATH_TO_DOWNLOAD,
            corner_radius=6,
            anchor='w',
            fg_color=("white", "gray38"),
        )
        self.path_download.grid(row=5, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.browse_download = customtkinter.CTkButton(
            master=self.frame_left,
            text="Browse",
            width=100,
            command=self.open_files_browser
        )
        self.browse_download.grid(row=5, column=1, pady=20, padx=10, sticky="e")

        self.switch_theme = customtkinter.CTkSwitch(
            master=self.frame_left,
            text="Dark Mode",
            command=self.change_appearance_mode,
        )
        self.switch_theme.grid(row=10, column=0, pady=20)
        if customtkinter.get_appearance_mode() == 'Dark':
            self.switch_theme.select()

        # RIGHT FRAME
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

    def load_youtube(self):
        url = self.get_url()
        if not url:
            print("Error: Please give a youtube URL")
            return
        try:
            yt = Download(url)

            u = urllib.request.urlopen(yt.get_thumbnail())
            raw_data = u.read()
            u.close()

            pilImage = Image.open(BytesIO(raw_data))
            self.update()
            pilImage = pilImage.resize((384, 216), Image.Resampling.LANCZOS)

            image = ImageTk.PhotoImage(pilImage)

            self.frame_info.rowconfigure(0, weight=0)
            self.frame_info.columnconfigure(0, weight=1)
            self.label = customtkinter.CTkLabel(
                master=self.frame_info,
                image=image,
            )
            self.label.image = image
            self.label.grid(row=0, column=0, pady=10)
            self.label_title = customtkinter.CTkLabel(
                master=self.frame_info,
                text=yt.get_title(),
            )
            self.label_title.grid(row=1, column=0, padx=10)

            self.button_mp3 = customtkinter.CTkButton(
                master=self.frame_right,
                text="Download MP3",
                width=self.frame_right.winfo_width() / 2 - 10,
                command=yt.download_video
            )
            self.button_mp3.grid(row=8, column=0, pady=20, padx=20, sticky="w")

            self.option_mp4 = customtkinter.CTkOptionMenu(
                master=self.frame_right,
                values=yt.get_resolution(),
                width=self.frame_right.winfo_width() / 2 - 10,
                command=yt.download_video
            )
            self.option_mp4.grid(row=8, column=1, pady=10, padx=20, sticky="e")
            self.option_mp4.set("Download MP4")
        except:
            print("Error couldn't load the video with the given url")
            return

    def get_url(self):
        return self.url_entry.get()

    def open_files_browser(self):
        global PATH_TO_DOWNLOAD
        directory = askdirectory()
        if directory:
            PATH_TO_DOWNLOAD = directory
        self.path_download.configure(text=PATH_TO_DOWNLOAD)

    def change_appearance_mode(self):
        if (self.switch_theme.get() == 0):
            customtkinter.set_appearance_mode('Light')
        else:
            customtkinter.set_appearance_mode('Dark')

    def on_closing(self, event=0):
        self.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()