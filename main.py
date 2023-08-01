from pytube import YouTube

# URL видео на YouTube
video_url = 'link_to_video'

# Создаем объект YouTube
yt = YouTube(video_url)

# Получаем доступные потоки видео
video_streams = yt.streams.filter(file_extension='mp4', progressive=True)

# Выбираем желаемое качество (в данном случае - максимальное)
video = video_streams.get_highest_resolution()

# Скачиваем видео в текущую директорию
video.download()
