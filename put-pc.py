import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None 
file = input('Archivo a enviar: ')
Ale = 250
Ale2 = 229
Ern = 236
An = 237
Gu = 238

while True:
    try:
        HOST1 = f'192.168.50.{Ale}'
        HOST2 = f'192.168.50.{Ern}'
        HOST3 = f'192.168.50.{An}'
        HOST4 = f'192.168.50.{Gu}'
        HOST5 = f'192.168.50.{Ale2}'
        print('Elija PC: ')
        print('1)',HOST1)
        print('2)',HOST2)
        print('3)',HOST3)
        print('4)',HOST4)
        print('5)',HOST5)
        opcion = int(input('Ingrese la pc: '))
        if opcion == 1:
            HOST = HOST1
            with pysftp.Connection(HOST1, username='sistemas', password=f'TSystem#{Ale}', cnopts=cnopts) as sftp:
                print(f'{HOST1} - Conectado')
                print(sftp.listdir('/media/sistemas/'))
                disk = input('En que discos de la 250?: ')
                sftp.put(f'{file}', f'/media/sistemas/{disk}/A/REVISADO/scripts/{file}')
                print(f'{file} - Enviado')  
                while True:
                    add = input('Desea agregar otro disco? (S/N): ')
                    if add == 'S':
                        disk = input('En que discos de la 250?: ')
                        sftp.put(f'{file}', f'/media/sistemas/{disk}/A/REVISADO/scripts/{file}')
                        print(f'{file} - Enviado')                                        
                    elif add == 'N':
                        break
                    else:
                        print('Opcion no valida')
                        continue
        elif opcion == 2:
            HOST = HOST2
            with pysftp.Connection(HOST2, username = 'sistemas', password = f'TSystem#{Ern}', cnopts = cnopts) as sftp:
                print(f'{HOST2} - Conectado')
                print(sftp.listdir('/media/sistemas/'))
                disk2 = input('En que discos de la 236?: ')
                sftp.put(f'{file}', f'/media/sistemas/{disk2}/A/REVISADO/scripts/{file}')
                print(f'{file} - Enviado')
                while True:
                    add = input('Desea agregar otro disco? (S/N): ')
                    if add == 'S':
                        disk2 = input('En que discos de la 236?: ')
                        sftp.put(f'{file}', f'/media/sistemas/{disk2}/A/REVISADO/scripts/{file}')
                        print(f'{file} - Enviado')
                    elif add == 'N':
                        break
                    else:
                        print('Opcion no valida')
                        continue
        elif opcion == 3:
            HOST = HOST3
            with pysftp.Connection(HOST3, username = 'sistemas', password = f'TSystem#{An}', cnopts = cnopts) as sftp:
                print(f'{HOST3} - Conectado')
                print(sftp.listdir('/media/sistemas/'))
                disk3 = input('En que discos de la 237?: ')
                sftp.put(f'{file}', f'/media/sistemas/{disk3}/A/REVISADO/scripts/{file}')
                print(f'{file} - Enviado')
                while True:
                    add = input('Desea agregar otro disco? (S/N): ')
                    if add == 'S':
                        disk3 = input('En que discos de la 237?: ')
                        sftp.put(f'{file}', f'/media/sistemas/{disk3}/A/REVISADO/scripts/{file}')
                        print(f'{file} - Enviado')
                    elif add == 'N':
                        break
                    else:
                        print('Opcion no valida')
                        continue
        elif opcion == 4:
            HOST = HOST4
            with pysftp.Connection(HOST4, username = 'sistemas', password = f'TSystem#{Gu}', cnopts = cnopts) as sftp:
                print(f'{HOST4} - Conectado')
                print(sftp.listdir('/media/sistemas/'))
                disk4 = input('En que discos de la 238?: ')
                sftp.put(f'{file}', f'/media/sistemas/{disk4}/A/REVISADO/scripts/{file}')
                print(f'{file} - Enviado')
                while True:
                    add = input('Desea agregar otro disco? (S/N): ')
                    if add == 'S':
                        disk4 = input('En que discos de la 238?: ')
                        sftp.put(f'{file}', f'/media/sistemas/{disk4}/A/REVISADO/scripts/{file}')
                        print(f'{file} - Enviado')
                    elif add == 'N':
                        break
                    else:
                        print('Opcion no valida')
                        continue
        elif opcion == 5:
            HOST = HOST5
            with pysftp.Connection(HOST5, username = 'sistemas', password = f'TSystem#{Ale2}', cnopts = cnopts) as sftp:
                print(f'{HOST5} - Conectado')
                print(sftp.listdir('/media/sistemas/'))
                disk5 = input('En que discos de la 229?: ')
                sftp.put(f'{file}', f'/media/sistemas/{disk5}/A/REVISADO/scripts/{file}')
                print(f'{file} - Enviado')
                while True:
                    add = input('Desea agregar otro disco? (S/N): ')
                    if add == 'S':
                        disk5 = input('En que discos de la 229?: ')
                        sftp.put(f'{file}', f'/media/sistemas/{disk5}/A/REVISADO/scripts/{file}')
                        print(f'{file} - Enviado')
                    elif add == 'N':
                        break
                    else:
                        print('Opcion no valida')
                        continue
        else:
            print('Opcion no valida')
            exit()
                                        
    except Exception as e:
        print(e)
        print(f'{HOST1} - Offline')
        print(f'{HOST2} - Offline')
        print(f'{HOST3} - Offline')
        print(f'{HOST4} - Offline')
        print(f'{HOST5} - Offline')
        pass