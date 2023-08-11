from pytube import YouTube

link = input("Enter the YouTube URL: ")
yt = YouTube(link)
videos = yt.streams.all() 
print(yt.title) #to show the youtube title
# print(yt.thumbnail_url) #to show youtube thumbnail
#videos = yt.streams.filter(only_audio= True)   ##to show only audio

# Enumerate starting from index 1 for user-friendly numbering
video = list(enumerate(videos, start=1))

print("Available video formats:")
for i, v in video:
    print(f"{i}. {v}")

print('Enter the desired option to download the video')
dn_option = int(input("Enter the option: ")) - 1  # Adjusting index for list access

# Validate user input
if 0 <= dn_option < len(video):
    dn_video = videos[dn_option]
    dn_video.download()  # Download the video
    print("Downloaded successfully")
else:
    print("Invalid option selected.")


