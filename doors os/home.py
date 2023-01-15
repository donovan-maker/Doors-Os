import time
import os
import socket
import psutil as pu
import random

def start():
    while True:
        battery = pu.sensors_battery()
        login_pass = open('user/password.data')
        login_name = open('user/username.data')
        l_p = login_pass.read()
        l_n = login_name.read()
        running = True
        print('██████╗░░█████╗░░█████╗░██████╗░░██████╗░░░░░░░█████╗░░██████╗\n██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔════╝\n██║░░██║██║░░██║██║░░██║██████╔╝╚█████╗░█████╗██║░░██║╚█████╗░\n██║░░██║██║░░██║██║░░██║██╔══██╗░╚═══██╗╚════╝██║░░██║░╚═══██╗\n██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝░░░░░░╚█████╔╝██████╔╝\n╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░░╚════╝░╚═════╝░')
        print('WELCOME ' + l_n + '!')
        print('The Date Is ' + time.strftime('%m/%d/%y'))
        print('The Battery Level is: ')
        print(battery.percent)
        print("""
        [1] To Open Network Explorer
        [2] To Open Notepad
        [3] To Open File Explorer
        [4] To Configure and Open Bios
        [5] To Shut Down OS
        """)
        select = input('[?]: ')

        if select == '1':
            os.startfile('InternetExplorer.py')

        if select == '2':
            os.startfile('notepad.py')

        if select == '3':
            os.startfile('FileExplorer.py')

        if select == '4':
            while running:
                running = True
                b_login = input(str('Please Enter The Password To ' + l_n + ' To Open Bios: '))
                if b_login == l_p:
                    while running:
                        print('Opening Bios...')
                        host_name = socket.gethostname()
                        host_ip = socket.gethostbyname(host_name)
                        print('[1] USER NAME: ' + l_n)
                        print('[2] PASSWORD: ' + l_p)
                        print('HOST NAME: ',host_name)
                        print('LOCAL IP: ',host_ip)
                        print("""
                        [1] Change Username
                        [2] Change Password
                        [3] Close Bios
                        """)
                        edit_b = input('Enter [?] To Change Setting')
                        if edit_b == '1':
                            with open('user/username.data', 'w') as f:
                                edit_n = input('Enter New Username')
                                f.writelines(edit_n)
                            print('Username Changed To ' + edit_n)
                        if edit_b == '2':
                            with open('user/password.data', 'w') as f:
                                edit_p = input('Enter New Password')
                                f.writelines(edit_p)
                            print('Password Changed To ' + edit_p)
                        if edit_b == '3':
                            print('Closing The Bios')
                            running = False
                        input()
        if select == '5':
            print('Shutting Down...')
            time.sleep(random.randint(2,5))
            break