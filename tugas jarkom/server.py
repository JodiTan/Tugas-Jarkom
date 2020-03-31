import socket
import _thread
import threading

players = []
message = ''
soal = ['1 + 1 = \nA. 2 \nB. 3 \nC. 4 \nD. 5', '2 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 2 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 4 = \nA. 2 \nB. 3 \nC. 4 \nD.5', '1 + 3 = \nA. 2 \nB. 3 \nC. 4 \nD. 5']
jawaban = ['a', 'c', 'b', 'd', 'c']
jawabanBenarCepat = 'Jawaban Anda benar!'
jawabanBenarTidakCepat = 'Jawaban Anda benar namun Anda kurang cepat!'
jawabanSalah = 'Jawaban Anda Salah!'
tambahScore = 'Skor Anda bertambah 1!'

def threadPlayer():
    while True:
        global players
        global message
        connection, address = socketServer.accept()
        namaPlayer = connection.recv(1024).decode()
        connection.send(('Selamat datang ' + namaPlayer + '\nWaktu anda menjawab adalah 10 detik. \nAnda hanya perlu menilai A atau B dan seterusnya').encode())
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
    timer = threading.Timer(10,()) 
    timer.start()
    for j in players:
        jawaban = connection.recv(1024).decode()
        waktu = connection.recv(1024).decode()
        if(jawaban.lower() == jawaban[nomor]):
            if(float(waktu) < float(tercepat)):
                playerBenar = j['nama']
                tercepat = float(waktu)
                connection.send(jawabanBenarCepat.encode())
            else:
                connection.send(jawabanBenarTidakCepat.encode())
        else:
            connection.send(jawabanSalah.encode())
    for k in players:
        if(k['nama'] == playerBenar):
            k['score'] += 1
        

