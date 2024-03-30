from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import re

def download_videos(channel_url, max_videos):
    html = requests.get(channel_url).text
    video_links = re.findall(r'watch\?v=\S+index', html)
    
    print(f'Downloading up to {max_videos} videos from channel: {channel_url}')

    for video, index in zip(video_links, range(max_videos)):
        print(f'Downloading video {index + 1}...')
        video_url = f'https://www.youtube.com/{video[:-5]}'
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        stream.download()

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    max_videos = int(input("Enter the maximum number of videos to download: "))
    download_videos(channel_url, max_videos)
