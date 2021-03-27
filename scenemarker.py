#!/usr/bin/env python
# coding: utf-8


#this script turns movies into shot-by-shot gifs
#run this script from the command line or just put your path and save_path directly into first two
#variables and run


path = input("Enter the file path:")
save_path = input("Enter folder path you want to save the gifs to--DO NOT PUT A SLASH AT THE END:")
#path = '/Users/juanhuml/Desktop/Tomjerry.mp4'
#save_path = '/Users/juanhuml/Desktop/tomjerryclips'
# Standard PySceneDetect imports:
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector

def find_scenes(video_path, threshold=30.0):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    # Each returned scene is a tuple of the (start, end) timecode.
    return scene_manager.get_scene_list()


scenes = find_scenes(path)


def to_seconds(string):
    h,m,s = string.split(':')
    return (float(h)*3600 + float(m)*60+ float(s))

#scenes doesn't start with 0 so we add this to our initial list
timestamp = [0]
for j in range(len(scenes)):
    timestamp.append(round(to_seconds(scenes[j][1].get_timecode()),3))


#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#ffmpeg_extract_subclip('/Users/juanhuml/Desktop/Tomjerry.mp4',3, 7, targetname="/Users/juanhuml/Desktop/test.mp4")


from moviepy.editor import *

for i in range(len(timestamp)):
    video = VideoFileClip(path).subclip(timestamp[i],timestamp[i+1])
    video.write_gif(save_path + '/scene' + str(i) + '.gif')

