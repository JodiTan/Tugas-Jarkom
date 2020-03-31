import socket
import time
import _thread

host = socket.gethostname()
port = 8888

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((host,port))

nama =  input('Masukkan Nama : ')
clientSocket.send(nama.encode())
print(clientSocket.recv(1024).decode())

def myTimer():
    time.sleep(10)
    global flag
    if (flag):
        clientSocket.send((nama+' '+'-'+' '+str(100)).encode())
        print('Timeout myTimer')
        hasil = clientSocket.recv(1024).decode()
        print(hasil+'\n')

flag = bool(1)

while True:
    flag = bool(1)
    pertanyaan = ''
    pertanyaan = clientSocket.recv(1024).decode()
    print(pertanyaan)
    waktuAwal = time.time()
    while True:
        if pertanyaan != '':
            myThread = _thread.start_new_thread(myTimer, ())
            break
    if(pertanyaan != '')
        jawaban = input('Masukkan Jawaban : ')
        waktuAkhir = time.time()
        waktuMenjawab = waktuAkhir - waktuAwal
        if(waktuMenjawab<=10):
            clientSocket.send((nama+' '+jawaban+' '+str(waktuMenjawab)).encode())
            flag = bool(0)
            hasil = clientSocket.recv(1024).decode()
            print(hasil+'\n')
        else:
            print('Timeout')
    else:
        break
    
