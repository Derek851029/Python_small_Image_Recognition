import moviepy.editor as mp
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("D:/movie_resized.mp4", 0, 5, targetname="test.mp4") #cut video length

# clip = mp.VideoFileClip('C:/Users/Administrator/Desktop/20210706_151132.mp4')
# clip_resized = clip.resize(newsize=(2200,250)) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("D:/movie_resized.mp4")