import os
import sys
import pathlib
import youtube_dl


def write_list_to_file(lines, file):
    for line in lines:
        file.write(line + '\n')
    return

if __name__ == '__main__':

    savepath = 'download_videos_result'
    os.makedirs(savepath, exist_ok=True)
    ydl_opt = {'format': 'bestvideo/best',
               'outtmpl': os.path.join(savepath, '%(id)s.%(ext)s'),} 
    ydl = youtube_dl.YoutubeDL(ydl_opt)
    
    urls_filename = sys.argv[1]
    urls = []
    with open(urls_filename, 'r') as urls_file:
        urls = urls_file.read().splitlines()
    urls_update = []
    with open(urls_filename, 'r') as file:
        urls_update = file.read().splitlines()

    num_urls = len(urls)
    for url in urls:
        info_dict = ydl.extract_info(url, download=False)

        duration = info_dict['duration']
        if duration < 600:
            ydl.download((url,))
