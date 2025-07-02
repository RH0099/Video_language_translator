import os

def combine_audio_video(video_file, audio_file):
    output_file = "final_translated_video.mp4"
    os.system(f"ffmpeg -i {video_file} -i {audio_file} -c:v copy -map 0:v:0 -map 1:a:0 -shortest {output_file} -y")
    return output_file
