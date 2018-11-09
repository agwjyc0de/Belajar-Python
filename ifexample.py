listuname = ['anggi','admin']
print('Hallow, Masukkan Username .!')
username = input()
print('Hai,'+ username)
if username.strip() not in listuname:
    print('maaf ' + username + ' belum terdaftar,silahkan daftar terlebih dahulu')
    exit()
else: 
    print('Masukkan Password.!')
    password = input()
while password != 'snake':
    print('Password Salah .!')
<<<<<<< HEAD
    print('Masukkan Password.!')
    password = input()
    
print('Hai ' + username + ', Selamat Datang Kembali')

=======
else:
    print('Hai ' + username + ', Selamat Datang Kembali')
>>>>>>> d191d9a2e33bfd4cc0afa5cd006e091d15beb9e7
