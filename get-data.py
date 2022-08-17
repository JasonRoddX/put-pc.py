from http import client
import pysftp
import os, re 
from socket import error as SocketError
import pandas as pd
import random as rd
import socket
import errno
import paramiko 
import shutil
import sys

for i in range (1, 17):
    if i not in [2, 3,4,5,6,7,8, 9, 10,13, 14, 17, 34, 36]:        
        try:
            class My_connection(pysftp.Connection):
                def __init__(self, *args, **kwargs):
                    self._sftp_live = False
                    self._transport = None
                    super().__init__(*args, **kwargs)
                                
            HOST = f'multas{i}.servidor.lan'
            host = f'MULTAS{i}'
            with My_connection(HOST, username='administrador', password='MultasPro2018') as sftp:
                print(f'{host} ¡Online!')
                path = "/procesos/ENVIAR-DARIO/PRUEBA"
                for camara in sftp.listdir(path):
                    if re.search(r'SECU\d\d\d\d', camara.split('/')[-1]):
                        print(f"Absorbiendo archivos de", HOST, camara)                            
                        videos = []
                        for video in sftp.listdir(f"{path}/{camara}"):
                            if video.endswith('.mp4'):
                                videos.append(video)
                                try:
                                    sftp.get(f"{path}/{camara}/{video}", f"Z:\\Recepcion\\{camara}\\{video}",)
                                    if camara and video in os.listdir(f"Z:\\Recepcion\\{camara}"):
                                        print(f'{camara}\\{video} ¡Descargado!')
                                except Exception as e:
                                    print(f'Error: {e}')

                                    #for files in sftp.listdir_attr('/procesos/ENVIAR-DARIO'):
                                        # print(files)
                                        #print(files)
                        
                                        #  if files.filename.endswith('1111'):
                                        #      sftp.get(f'/procesos/ENVIAR-DARIO/{files.filename}', f'C:\Users\EQUIPO 5\Desktop\R')
                                        #   if os.path.exists(f'C:\Users\EQUIPO 5\Desktop\R\'{files.filename}'):
                                        #      print(f'{files.filename} ¡Descargado!')                                                                                                 
        except Exception as e:
            print(e)
            #print(f'{HOST} ¡Offline!')
            continue        