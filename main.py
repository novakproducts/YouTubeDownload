from pytube import YouTube

# URL видео на YouTube
video_url = 'https://www.youtube.com/shorts/XtJ3Yn_zpRs'

# Создаем объект YouTube
yt = YouTube(video_url)

# Получаем доступные потоки видео
video_streams = yt.streams.filter(file_extension='mp4', progressive=True)

# Выбираем желаемое качество (в данном случае - максимальное)
video = video_streams.get_highest_resolution()

# Скачиваем видео в текущую директорию
video.download()
