import getpass

#switch to larger database

users:dict[str,str] ={'yaramin': 'fatu456', 
        'jeyuso':'yeet562',
        'romanreigns': 'otc897'}

try:
    username: str=input('Enter username: ').lower()
    password : str= getpass.getpass('Enter password: ')

    if username in users.keys():
        if password != users[username]:
            print('Username/password is incorrect')
        else:
            print('Verified')

    else:
        print('Username/password is incorrect')
except KeyboardInterrupt :
    print('\n Interrupted by user')
except Exception as e :
    print(f'Error at {e}')

