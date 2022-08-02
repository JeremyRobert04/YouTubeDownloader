##
## PERSONAL PROJECT, 2022
## YouTubeDownloader
## File description:
## tkinter GUI
##

import tkinter
import customtkinter
import darkdetect

screen_width = 900
screen_height = 600

def widgets_light(root):
    root['background']='#F2F2F2'
    canvas = tk.Canvas(
        root,
        height=600,
        width=150,
        bg='yellow'
    )
    canvas.pack()

def rounded_corner_canvas(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def widgets_dark(root):
    root['background']='#1A1A1A'
    left_canvas = tk.Canvas(
        root,
        height=screen_height,
        width=0.25 * screen_width,
        bg='#2A2A2A',
        highlightthickness=0
    )
    left_canvas.pack(side='left', fill='x')
    entry_url_canvas = tk.Canvas(
        left_canvas,
        height=30,
        width=int(left_canvas['width']) - 0.15 * int(left_canvas['width']),
        bg='#2A2A2A',
        highlightthickness=0
    )
    left_canvas.create_window(int(left_canvas['width']) - 110, 100, window=entry_url_canvas)
    rectangle = rounded_corner_canvas(
        entry_url_canvas,
        0, 0, int(entry_url_canvas['width']), int(entry_url_canvas['height']),
        radius=10,
        fill="#4D4D4D"
    )
    entry_url = tk.Entry(
        root,
        # height=30,
        width=30,
        bg='#4D4D4D',
        fg='#A4A9A7',
    )
    def clear_text(text_box):
        text_box.configure(state='normal')
        text_box.delete(0, 'end')
        text_box.unbind('<Button-1>', clicked)
    entry_url.insert(0, "Enter Video URL")
    entry_url.config(borderwidth=0)
    entry_url.pack()
    clicked = entry_url.bind('<Button-1>', clear_text(entry_url))

    # rectangle = rounded_corner_canvas(
    #     entry_url,
    #     0, 0, 100, 100,
    #     radius=20,
    #     fill="red"
    # )

    right_canvas = tk.Canvas(
        root,
        height=screen_height - 0.1 * screen_height,
        width=screen_width - 0.1 * screen_height,
        bg='#1A1A1A',
        highlightthickness=0
    )
    right_canvas.pack(side='right', fill='x', padx=0.05 * screen_height)
    my_rectangle = rounded_corner_canvas(
        right_canvas,
        0, 0, int(right_canvas['width']) - 0.25 * screen_width, int(right_canvas['height']),
        radius=40,
        fill="#2A2A2A"
    )


def load_widgets(root):
    print("Load Widgets")
    if (darkdetect.isDark):
        widgets_dark(root)
    else:
        widgets_light(root)


def run_app():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()

    # TitleBar
    root.title("Youtube Video Downloader")
    root.iconbitmap("templates/Icon.ico")
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(False, False)

    # load_widgets(root)
    # def motion(event):
    #     x, y = event.x, event.y
    #     print('{}, {}'.format(x, y))

    # root.bind('<Motion>', motion)
    left_canvas = customtkinter.CTkCanvas(
        master=root,
        height=screen_height,
        width=0.25 * screen_width,
        bg='#2A2A2A',
        highlightthickness=0
    )
    left_canvas.pack(side='left', fill='x')
    def button_function():
        print("button pressed")
    button = customtkinter.CTkButton(master=root, text="CTkButton", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    root.mainloop()