# services/youtube_service.py
from pytube import Playlist

def get_videos_from_playlist(playlist_url: str):
    try:
        playlist = Playlist(playlist_url)
        videos_info = [
            {
                'title': video.title,
                'video_url': video.watch_url,
                'thumbnail_url': video.thumbnail_url
            }
            for video in playlist.videos
        ]
        return videos_info
    except Exception as e:
        raise ValueError(f"Error al obtener videos de la lista de reproducción: {str(e)}")
