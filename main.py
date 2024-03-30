from pytube import YouTube

def download_youtube_video():
    # Ask the user for the link
    link = input("Please enter the YouTube short link: ")

    # Create a YouTube object
    yt = YouTube(link)

    # Download the highest resolution version of the video
    yt.streams.get_highest_resolution().download()

    print("Download completed!")

# Call the function
download_youtube_video()
