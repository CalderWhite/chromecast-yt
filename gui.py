import subprocess

CHROMECAST_IP = "192.168.1.148"


def play_video(youtube_url):
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


while True:
    youtube_url = input("Enter a youtube url:")
    play_video(youtube_url)
