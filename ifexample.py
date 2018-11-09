listuname = ['anggi','admin']
print('Hallow, Masukkan Username .!')
username = input()
print('Hai,'+ username)
if username.strip() not in listuname:
    print('maaf ' + username + ' belum terdaftar,silahkan daftar terlebih dahulu')
    exit()
else: 
    print('masukkan password')
password = input()
if password != 'snake':
    print('Password Salah .!')
else:
    print('Hai ' + username + ', Selamat Datang Kembali')
