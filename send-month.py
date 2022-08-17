import os
import re
import shutil
import pandas as pd
import random as rd
from socket import error as SocketError
disco=input("Disco: ")
reception = f'/media/sistemas/{disco}/A/REVISADO/SEND-MONTH'
destiny = f'/media/sistemas/{disco}/A/REVISADO/ENVIAR'
soon = f'/media/sistemas/{disco}/A/REVISADO/PROXIMOS-ENVIOS'

for root, dirs, files in os.walk(reception):

    folder = root
    april = 0
    may = 0
    june = 0
    july = 0
    august = 0
    september = 0
    config = 'config.cfg'
    camara = root.split("/")[-1]
  
    for video in files:
        if video.endswith('.mp4'):
            if video[6:10] == '2022':
                print(video)

                if video[6:12] == '202204':
                    april += 1
                    print(f"{camara},{video}")
                    os.makedirs(f'{destiny}/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}', f'{destiny}/{camara}/{video}')
                    except:
                        print(f"Duplicated,{camara},{video}")
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info... {camara}, ABRIL: {may} videos')
                        pass
                
                elif video[6:12] == '202205':
                    may += 1
                    print(f"{camara},{video}")
                    os.makedirs(f'{soon}/MAYO/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}', f'{soon}/MAYO/{camara}/{video}')
                    except:
                        print(f"Duplicated,{camara},{video}")
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info... {camara}, MAYO: {may} videos')
                        pass
                    
                elif video[6:12] == '202206':
                    june += 1
                    print(f"{camara},{video}")
                    os.makedirs(f'{soon}/JUNIO/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}', f'{soon}/JUNIO/{camara}/{video}')
                    except:
                        print(f"Duplicated,{camara},{video}")
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info... {camara}, JUNIO: {june} videos')
                        pass
                    
                elif video[6:12] == '202207':
                    july += 1
                    print(f"{camara},{video}")
                    os.makedirs(f'{soon}/JULIO/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}', f'{soon}/JULIO/{camara}/{video}')
                    except:
                        print(f'Duplicated,{camara}{video}')
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info... {camara}, JULIO: {july} videos')
                        pass
                    
                elif video[6:12] == '202208':
                    august += 1
                    print(f'{camara},{video}')
                    os.makedirs(f'{soon}/AGOSTO/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}', f'{soon}/AGOSTO/{camara}/{video}')
                    except:
                        print(f"Duplicated,{camara}{video}")
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info ... {camara}, AGOSTO: {august} videos')
                        pass
                    
                elif video[6:12] == '202209':
                    september += 1
                    print(f'{camara},{video}')
                    os.makedirs(f'{soon}/SEPTIEMBRE/{camara}', exist_ok=True)
                    try:
                        shutil.move(f'{reception}/{camara}/{video}',f'{soon}/SEPTIEMBRE/{camara}/{video}')
                    except:
                        print(f"Duplicated,{camara}/{video}")
                        os.remove(f'{reception}/{camara}/{video}')
                        print(f'Sending info... {camara}, SEPTIEMBRE: {september} videos')
                        pass              

