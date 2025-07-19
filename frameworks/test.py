import requests
import time
import subprocess

def esta_online(username):
    url = f"https://chaturbate.com/api/chatvideocontext/{username}/"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data.get("broadcaster_username") is not None
    except:
        pass
    return False

def grabar_stream(username):
    print(f"Iniciando grabación de {username}...")
    nombre_archivo = f"{username}_{int(time.time())}.ts"
    comando = [
        "streamlink",
        f"https://chaturbate.com/{username}/",
        "best",
        "-o", nombre_archivo
    ]
    subprocess.run(comando)

def monitor_usuario(username, intervalo=60):
    print(f"Monitoreando a {username} cada {intervalo} segundos...")
    while True:
        if esta_online(username):
            print(f"{username} está en vivo. Iniciando descarga...")
            grabar_stream(username)
            print("Esperando a que termine el stream para reintentar...")
        else:
            print(f"{username} no está en vivo. Reintentando en {intervalo} segundos.")
            time.sleep(intervalo)

if __name__ == "__main__":
    monitor_usuario("bunnyy09", intervalo=60)  # reemplaza por el nombre real
