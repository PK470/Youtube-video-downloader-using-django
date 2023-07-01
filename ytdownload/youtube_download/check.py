from pytube import YouTube
import os
url ="https://www.youtube.com/watch?v=2ZNTQCeBQ1Y"
yt =  YouTube(url)
strem = yt.streams.first()
filename = yt.streams.first().default_filename
filename = os.path.splitext(filename)[0]
print(filename)
strem.download("C:/Users/91844/OneDrive/Desktop/myapp/ytdownload/video/")
