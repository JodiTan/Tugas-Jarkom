import socket
import _thread
import threading
import time

players = []
message = ''
soal = ['1 + 1 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '2 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 4 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 3 = \nA. 2 \nB. 3 \nC. 4 \nD. 5']
jawaban = ['a', 'c', 'b', 'd', 'c']
jawabanBenarCepat = 'Jawaban Anda benar!'
jawabanBenarTidakCepat = 'Jawaban Anda benar namun Anda kurang cepat!'
jawabanSalah = 'Jawaban Anda Salah!'

def threadPlayer():
    while True:
        global players
        global message
        connection, address = socketServer.accept()
        namaPlayer = connection.recv(1024).decode()
        connection.send(('Selamat datang ' + namaPlayer + '\nWaktu anda menjawab adalah 10 detik! \nAnda hanya perlu menjawab A atau B atau C atau D.').encode())
        if(message == 'mulai'):
            break
        print('User ' + namaPlayer + ' telah bergabung')
        player = {
             'nama': namaPlayer,
             'score': 0,
             'connection': connection,
             'address': address
        }
        players.append(player)



host = socket.gethostname()
port = 8888

socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketServer.bind((host, port))

socketServer.listen(10)

_thread.start_new_thread(threadPlayer, ())
message = input("Ketikkan 'mulai' untuk memulai permainan! \n")
for nomor in range(0, soal.__len__()):
    for i in players:
        connection = i['connection']
        connection.send(soal[nomor].encode())
    playerBenar = ''
    tercepat = 1000
    tempUser = []
    tempJawaban = []
    tempWaktu = []
    for j in players:
        namaUser = connection.recv(1024).decode()
        print(namaUser)
        temp =  namaUser.split()
      #  jawabanUser = connection.recv(1024).decode()
     #   print(jawabanUser)
     #   selisihWaktu = connection.recv(1024).decode()
      #  print(selisihWaktu)
        tempUser.append(temp[0])
        tempJawaban.append(temp[1])
        tempWaktu.append(temp[2])
    for h in range(0,jawaban):
        if(tempJawaban[h].lower() == jawaban[nomor]):
            if(float(tempWaktu[h]) < float(tercepat)):
                playerBenar = tempUser[h]
                tercepat = float(tempWaktu[h])
    connection.send(('User yang mendapatkan poin adalah user' + playerBenar).encode())

    for k in players:
        if(k['nama'] == playerBenar):
            print(k['nama'])
            k['score'] += 1
        

