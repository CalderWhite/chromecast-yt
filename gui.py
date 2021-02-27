import tkinter
import subprocess

CHROMECAST_IP = "192.168.1.148"

root = tkinter.Tk()

url_bar = tkinter.Entry(root)
url_bar.grid(row=0, column=0)

def play_video(event):
    youtube_url = url_bar.get()

    print("Finding CDN url...")
    proc = subprocess.run(["youtube-dl", "--get-url", "-f", "22", youtube_url],
                          capture_output=True)
    cdn_url = proc.stdout.decode('utf-8').strip()
    print(cdn_url)

    print("Launching CDN url in vlc...")
    subprocess.run([
        "vlc", cdn_url, "--sout", "#chromecast", "--sout-chromecast-ip", CHROMECAST_IP,
        "--demux-filter", "demux_chromecast"
    ])

def empty_bar(event):
    url_bar.delete(0, tkinter.END)


root.bind('<Return>', play_video)
root.bind('<Shift-Delete>', empty_bar)

root.mainloop()
