from pytube import Playlist
import os

def download_videos(playlist_url, max_videos):
    playlist = Playlist(playlist_url)
    print(f'Downloading up to {max_videos} videos from playlist: {playlist.title}')

    for url, index in zip(playlist.video_urls, range(max_videos)):
        print(f'Downloading video {index + 1}...')
        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    max_videos = int(input("Enter the maximum number of videos to download: "))
    download_videos(playlist_url, max_videos)
