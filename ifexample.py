print('Hallow, Masukkan Username .!')
username = input()
print('Hai,'+ username)
if username != 'anggi' or username !='admin':
    print('maaf ' + username + ' belum terdaftar,silahkan daftar terlebih dahulu')
    exit()
else: 
    print('masukkan password')
password = input()
if password != 'snake':
    print('Password Salah .!')
else:
    print('Hai' + username + ', Selamat Datang Kembali')

