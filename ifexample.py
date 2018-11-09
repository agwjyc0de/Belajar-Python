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
    print('Masukkan Password.!')
    password = input()
    
print('Hai ' + username + ', Selamat Datang Kembali')

