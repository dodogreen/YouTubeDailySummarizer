import subprocess
import json
import datetime
import os
import argparse

def get_channel_videos(channel_url):
    command = [
        'yt-dlp',
        '--flat-playlist',
        '--dump-json',
        '--default-search', 'ytsearch',
        channel_url
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return [json.loads(line) for line in result.stdout.splitlines()]
    except subprocess.CalledProcessError as e:
        print(f"Error fetching channel videos: {e}")
        return []

def get_video_info(video_url):
    command = [
        'yt-dlp',
        '--dump-json',
        video_url
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching video info: {e}")
        return None

def download_today_mp3(video_url, output_dir):
    command = [
        'yt-dlp',
        '--output', os.path.join(output_dir, '%(title)s.%(ext)s'),
        '--date', 'today',
        '--embed-thumbnail',
        '--add-metadata',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '320K',
        '--date', 'today',
        video_url
    ]
    subprocess.run(command)

def download_subs_only(video_url, output_dir):
    command = [
        'yt-dlp',
        '--output', os.path.join(output_dir, '%(title)s.%(ext)s'),
        '--sub-lang', 'zh-TW',
        '--write-sub',
        '--convert-subs', 'srt',
        '--skip-download',
        video_url
    ]
    subprocess.run(command)

def main(channel_url, base_dir):
    videos = get_channel_videos(channel_url)
    if not videos:
        print("No videos found for the channel.")
        return

    today = datetime.datetime.now().date()
    channel_id = channel_url.split('/')[-1]
    output_dir = os.path.join(base_dir, channel_id, today.strftime('%Y-%m-%d'))
    os.makedirs(output_dir, exist_ok=True)

    for video in videos:
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        info = get_video_info(video_url)
        if not info:
            continue

        upload_date = datetime.datetime.strptime(info['upload_date'], '%Y%m%d').date()
        if upload_date == today:
            subtitles = info.get('subtitles', {})
            if 'zh-TW' in subtitles:
                download_subs_only(video_url, output_dir)
            else:
                download_today_mp3(video_url, output_dir)
            break
    else:
        print("No videos uploaded today.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download today\'s videos from specified YouTube channels.')
    parser.add_argument('-c', '--channels', nargs='+', default=[
                        'https://www.youtube.com/@user-mk9eo5kx3d',
                        'https://www.youtube.com/@eason111',
                        'https://www.youtube.com/@user-zr8qq2te8l',
                        'https://www.youtube.com/@user-id3ui2pw7j'
                        ], help='List of YouTube channel URLs')
    parser.add_argument('-d', '--output', default='download_mp3_srt', help='Base output for downloads')

    args = parser.parse_args()
    
    for channel_url in args.channels:
        main(channel_url, args.output)
    

