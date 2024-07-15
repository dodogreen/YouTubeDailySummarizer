import subprocess
import datetime
import os
import argparse

def download_today_videos(channel_url, output_dir):
    today = datetime.datetime.now().strftime('%Y%m%d')
    command = [
        'yt-dlp',
        '--date', today,
        '--break-on-reject',
        '--output', os.path.join(output_dir, '%(title)s.%(ext)s'),
        channel_url
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading today's videos: {e}")
        print(f"Command output: {e.output}")
        print(f"Error message: {e.stderr}")

def main(channel_url, output_dir):
    today = datetime.datetime.now().date()
    channel_id = channel_url.split('/')[-1]
    output_dir = os.path.join(output_dir, channel_id, today.strftime('%Y-%m-%d'))
    os.makedirs(output_dir, exist_ok=True)

    download_today_videos(channel_url, output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download today\'s videos from specified YouTube channels.')
    parser.add_argument('-c', '--channels', nargs='+', default=[], help='List of YouTube channel URLs')
    parser.add_argument('-d', '--output_dir', default='download_mp3_srt', help='Base output for downloads')

    args = parser.parse_args()

    for channel_url in args.channels:
        main(channel_url, args.output_dir)