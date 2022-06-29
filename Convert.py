from moviepy import editor

video = editor.VideoFileClip("eftekhari.mp4")
audio = video.audio
audio.write_audiofile("eftekhari.mp3")