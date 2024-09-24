
import os
import subprocess
from download_media import download_spotify_song, download_youtube_video

def create_apk(media_file, app_name):
    # Create a simple main.py file for the APK
    with open('main.py', 'w') as f:
        f.write(f'''
from kivy.app import App
from kivy.uix.label import Label

class {app_name}(App):
    def build(self):
        return Label(text="This is a media app")

if __name__ == "__main__":
    {app_name}().run()
''')

    # Create a buildozer.spec file
    with open('buildozer.spec', 'w') as f:
        f.write(f'''
[app]
title = {app_name}
package.name = {app_name.lower()}
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
source.include_exts = mp3,mp4
source.include_patterns = {media_file}
fullscreen = 1
[buildozer]
log_level = 2
warn_on_root = 1
''')

    # Run buildozer to create the APK
    subprocess.run(['buildozer', 'android', 'debug'])

if __name__ == '__main__':
    media_file = 'example.mp3'  # Replace with actual media file
    app_name = 'MediaApp'
    create_apk(media_file, app_name)
