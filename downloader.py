import os
import yt_dlp

def descargar_video(url, carpeta_destino='videos_descargados'):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    opciones = {
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Introduce la URL del video (Twitter/X, YouTube, etc): ")
    descargar_video(url)
    print("Descarga completada.")