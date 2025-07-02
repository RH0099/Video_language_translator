import yt_dlp

def download_video(url):
    output_path = "downloaded_video.mp4"
    ydl_opts = {'outtmpl': output_path, 'format': 'mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path
