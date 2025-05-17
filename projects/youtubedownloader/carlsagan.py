# pip install yt-dlp
import yt_dlp
import os

url = "https://www.youtube.com/watch?v=f9A_qFM9IAk"
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
ydl_opts = {
    'format': 'bv*+ba/best',
    'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s') 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

