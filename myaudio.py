#
# pip install mutagen
# 讀取音訊的屬性

from mutagen.mp3 import MP3

audio = MP3("hello.mp3")
#print("Title:", audio["TIT2"])
#print("Artist:", audio["TPE1"])
#print("Album:", audio["TALB"])

for key, value in audio.tags.items():
    print(f"{key}: {value}")
    