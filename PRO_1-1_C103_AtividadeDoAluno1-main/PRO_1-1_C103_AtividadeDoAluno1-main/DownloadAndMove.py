import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/Suporte/Downloads"
to_dir = "C:/Users/Suporte/Documents/Python"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if extension in value:
                fileName = os.path.basename(event.src.path)
                print("Baixado " + fileName)
                path1 = from_dir + "/" + fileName
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + fileName
                if os.path.exists(path2):
                    print("Este diretorio existe")
                    print("Movendo " + fileName + "..." )
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Criando diretorio ")
                    os.makedirs(path2)
                    print("Movendo " + fileName + "..." )
                    shutil.move(path1,path3)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("Foi interrompido")
    observer.stop()
