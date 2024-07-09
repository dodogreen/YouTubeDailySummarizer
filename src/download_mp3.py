import yt_dlp

URLS = ['https://youtu.be/6dWBoH2ervY\?si\=KjqSVjWh1cCIl53V']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
    
    
# download mp3
# yt-dlp --output "%(title)s.%(ext)s" --embed-thumbnail --add-metadata --extract-audio --audio-format mp3 --audio-quality 320K "https://youtu.be/6dWBoH2ervY\?si\=KjqSVjWh1cCIl53V"

# 下載自動生成字幕檔的指令
# yt-dlp --output "%(title)s.%(ext)s" --write-auto-subs --write-sub --convert-subs srt --embed-thumbnail --add-metadata --merge-output-format mp4 "https://www.youtube.com/watch?v=FfgT6zx4k3Q"


# 只下載字幕檔不下載影片的指令
# yt-dlp --output "%(title)s.%(ext)s" --sub-lang zh-TW --write-sub --convert-subs srt --skip-download "https://www.youtube.com/watch?v=FfgT6zx4k3Q"

# 刪除業配片段
# 使用--sponsorblock-remove all，將所有的影片業配片段從下載的影片中刪除。


# --date DATE                     Download only videos uploaded on this date.
                                # The date can be "YYYYMMDD" or in the format 
                                # [now|today|yesterday][-N[day|week|month|year]].
                                # E.g. "--date today-2weeks" downloads only
                                # videos uploaded on the same day two weeks ago