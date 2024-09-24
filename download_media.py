
import os
import subprocess

def download_spotify_song(spotify_url):
    subprocess.run(['spotdl', spotify_url])

def download_youtube_video(youtube_url):
    from pytube import YouTube
    yt = YouTube(youtube_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()

if __name__ == '__main__':
    spotify_url = 'https://open.spotify.com/track/xyz'  # Replace with actual Spotify URL
    youtube_url = 'https://www.youtube.com/watch?v=xyz'  # Replace with actual YouTube URL

    download_spotify_song(spotify_url)
    download_youtube_video(youtube_url)
