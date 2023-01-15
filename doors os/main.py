import time
import os
import home

print('██████╗░░█████╗░░█████╗░██████╗░░██████╗░░░░░░░█████╗░░██████╗\n██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔════╝\n██║░░██║██║░░██║██║░░██║██████╔╝╚█████╗░█████╗██║░░██║╚█████╗░\n██║░░██║██║░░██║██║░░██║██╔══██╗░╚═══██╗╚════╝██║░░██║░╚═══██╗\n██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝░░░░░░╚█████╔╝██████╔╝\n╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░░╚════╝░╚═════╝░')
print('[1] Continue With Setup\n[2] Already Done Setup')
setup = input('[?]: ')
if setup == '1':
    name = input(str('Please Enter Your Username To Be Displayed'))
    pas = input(str('Please Enter Your Password To Login'))
    
    with open('user/username.data', 'w') as f:
        f.writelines(name)
    
    with open('user/password.data', 'w') as f:
        f.writelines(pas)
    print('Setup Complete!')
    print('Press Enter To Close Window')
    keyWait = input()
if setup == '2':
    login_pass = open('user/password.data')
    login_name = open('user/username.data')
    l_p = login_pass.read()
    l_n = login_name.read()
    while True:
        login = input(str('Please Enter The Password To ' + l_n + ': '))
        if login == l_p:
            home.start()
            break
        else:
            print(login + ' Is Not The Right Password To Login To ' + l_n)