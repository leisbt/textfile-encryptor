import scrypt

textfile_folder = input('Folder location: ')
choice = input('1 to encrypt\n'
               '2 to decrypt\n: ')

if choice == '1':
    username = input('username: ')
    try:
        secrets = open(textfile_folder + username)
        secrets.close()
        data = input('data: ')
        password = input('password: ')
        secrets = open(textfile_folder + username, 'rb')
        secretsread = secrets.read()
        datadecrpyted = scrypt.decrypt(secretsread, password, maxtime=0.1)[:]
        dataencrypted = scrypt.encrypt(data, password, maxtime=0.1)
        secrets.close()
        secrets = open(textfile_folder + username, 'wb')
        secrets.write(dataencrypted)
        secrets.close()
    except FileNotFoundError:
        secrets = open(textfile_folder + username, 'wb')
        data = input('data: ')
        password = input('password: ')
        dataencrypted = scrypt.encrypt(data, password, maxtime=0.1)
        secrets.write(dataencrypted)
        secrets.close()
    except scrypt.scrypt.error:
        print('passwword incorrect')
if choice == '2':
    try:
        username = input('username: ')
        secrets = open(textfile_folder + username, 'rb')
        password = input('password: ')
        secretsread = secrets.read()
        datadecrpyted = scrypt.decrypt(secretsread, password, maxtime=0.1)[:]
        for line in datadecrpyted[:].split('~'):
            print(line)
        secrets.close()
    except scrypt.scrypt.error:
        print('password incorrect')
