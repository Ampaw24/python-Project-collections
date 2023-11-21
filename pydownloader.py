from pytube import YouTube

userLink = input("Paste Video Link here... \n ")
ytube = YouTube(userLink)
video_stream = ytube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#streams = ytube.streams.filter(only_audio=True, file_extension='mp4')
video_title = ytube.title
video_author = ytube.author

description = ytube.description

print("Video ",video_title," download started \n", video_author , "\n", description)


video_stream.download()
print("Video ", video_title, " completed.......")