# from pytube import YouTube

# def download_youtube_video():
#     # Ask the user for the link
#     link = input("Please enter the YouTube short link: ")

#     # Create a YouTube object
#     yt = YouTube(link)

#     # Download the highest resolution version of the video
#     yt.streams.get_highest_resolution().download()

#     print("Download completed!")

# # Call the function
# download_youtube_video()
from pytube import YouTube
YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()