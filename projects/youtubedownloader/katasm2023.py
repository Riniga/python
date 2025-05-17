# pip install yt-dlp
import yt_dlp
import os

url = "https://www.youtube.com/watch?v=zcBXU06quqE"
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

ydl_opts = {
    'format': 'bv*+ba/best',
    'download_sections': ['*02:15:15-02:25:25'],  # Start - Stop , however, this downloads the whole video and then cuts it
    'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s') 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

