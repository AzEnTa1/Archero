import yt_dlp
import os

def download_youtube_video(url):
    # Configuration pour la meilleure qualité
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Combine les meilleurs flux
        'merge_output_format': 'mp4',          # Format de fusion
        'outtmpl': '%(title)s.%(ext)s',        # Template du nom de fichier
        'noplaylist': True,                    # Ne pas télécharger les playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Téléchargement terminé avec succès!")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    url = input("Collez l'URL de la vidéo YouTube: ")
    download_youtube_video(url)