import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube


def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH ", title="Save Video")
    if download_directory:
        download_Path.set(download_directory)


def Download():
    try:
        youtube_link = video_Link.get()
        download_Folder = download_Path.get()
        if youtube_link.strip() == "":
            raise ValueError("Please enter a YouTube link")

        getVideo = YouTube(youtube_link)
        video_streams = getVideo.streams.filter(progressive=True, file_extension='mp4')
        if not video_streams:
            raise ValueError("No downloadable video found")

        # Let's download the highest resolution video available
        video_stream = video_streams.order_by('resolution').desc().first()
        video_stream.download(download_Folder)
        messagebox.showinfo("Success", "Downloaded Video Saved IN\n" + download_Folder)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def Widgets():
    head_label = Label(root, text="YouTube Video Downloader Using Tkinter ",
                       padx=15, pady=15, font="SegoeUI 14",
                       bg="palegreen1", fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root, text="YouTube link :", bg="salmon", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Destination", bg="salmon", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse, width=10, bg="bisque", relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_B = Button(root, text="Download Video", command=Download, width=20, bg="thistle", pady=10, padx=15)
    Download_B.grid(row=4, column=1, pady=20, padx=20)


root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
