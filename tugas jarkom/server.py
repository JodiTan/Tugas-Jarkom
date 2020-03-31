# Nama : Jodi Tanato - 2017730037
# Nama : Harry Senjaya Darmawan - 2017730067
import socket
import _thread
import time

players = []
message = ''
soal = ['1 + 1 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '2 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '1 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '1 + 4 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '1 + 3 = \nA. 2 \nB. 3 \nC. 4 \nD. 5']
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

def getAnswer(connectionTemp):
    while True:
        global tempUser
        global tempJawaban
        global tempWaktu
        namaUser = connectionTemp.recv(1024).decode()
        print(namaUser)
        temp =  namaUser.split()
        tempUser.append(temp[0])
        tempJawaban.append(temp[1])
        tempWaktu.append(temp[2])
        break
        

host = socket.gethostname()
port = 8888

socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketServer.bind((host, port))

socketServer.listen(10)

_thread.start_new_thread(threadPlayer, ())
while True:
    message = input("Ketikkan 'mulai' untuk memulai permainan! \n")
    if message.lower() == 'mulai':
        break
    
_thread.exit_thread
    
for nomor in range(0, soal.__len__()):
    for i in players:
        connection = i['connection']
        connection.send(soal[nomor].encode())
    playerBenar = ''
    tercepat = 1000
    tempUser = []
    tempJawaban = []
    tempWaktu = []
    for x in players:
        _thread.start_new_thread(getAnswer, (x['connection'],))
    print('masuk')    
    time.sleep(15)
    
    for h in range(0,players.__len__()):
        if(tempJawaban[h].lower() == jawaban[nomor]):
            if(float(tempWaktu[h]) < float(tercepat)):
                playerBenar = tempUser[h]
                tercepat = float(tempWaktu[h])

    for k in players:
        if(k['nama'] == playerBenar):
            print(k['nama'])
            k['score'] += 1
        k['connection'].send(('User yang mendapatkan poin adalah user ' + playerBenar).encode())

hasil = ''
for i in players:
    hasil += i['nama']+' '+str(i['score'])+'\n'
    
for i in players:
    connection = i['connection']
    connection.send(hasil.encode())