
from pytube import YouTube

# Downloading the highest resolution video
yt = YouTube('https://www.youtube.com/watch?v=00R4dOtzDIA')
video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
videoTitle = yt.title

print(videoTitle)
video_stream.download()
print("Video ", videoTitle," Completed....")
