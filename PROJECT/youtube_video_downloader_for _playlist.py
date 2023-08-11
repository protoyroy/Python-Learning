from pytube import Playlist
playlist_url = input("Enter the url: ")
py= Playlist(playlist_url)
print(f'Downloading:{py.title}')
for video in py.videos:
    video.streams.first().download()
    