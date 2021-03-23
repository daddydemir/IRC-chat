import socket 
import threading
from colorama import init
from colorama import Fore, Back, Style

init()
Style.RESET_ALL

def kullaniciAdi():
	nick = ""
	while True:
		nick = input("Lütfen bir nickname giriniz : ")
		if(nick == ""):
			print("geçersiz !")
			continue
		if(len(nick) > 10):
			print("çok uzun oldu !")
		else:
			break
	return nick

def checkMsg(gelen):
	isim = ""
	mesaj = ""
	sayac = 0
	isUser = False
	Style.RESET_ALL
	
	for i in gelen:
		sayac += 1
		if(i == "#"):
			# kullanıcılardan gelen mesajda # vardır 
			isUser = True
			mesaj = gelen[sayac:len(gelen)]
			break
		isim += i
			
			
	if(isUser == False):
		print(Fore.RED + gelen +Fore.WHITE)
	else:
		Style.RESET_ALL
		print(Fore.YELLOW + isim + Style.RESET_ALL + " >>> " + Fore.BLUE  + mesaj + Fore.WHITE)
	
	Style.RESET_ALL
		
def getMessage():
	while True:
		try:
			response = clientSocket.recv(1024) # sunucudan mesaj geliyor .:.
		except:
			a =""
		msg = response.decode('utf-8')
		#print(msg+"\n")
		checkMsg(msg)


isim = kullaniciAdi()

clientSocket = socket.socket() # default olarak IPv4 ü kullanıyor .:. 
host = "localhost" # sununun ip adresini girmelisiniz
port = 4545        # isteğe bağlı

print("Waiting for Connection")
try:
	clientSocket.connect((host,port)) # belirtilen porta bağlanma isteği gönderiliyor .:.
	clientSocket.send(str.encode(isim))
except socket.error as e:
	print(str(e))

t1 = threading.Thread(target=getMessage)
t1.start()
while True:
	Input = input()
	clientSocket.send(str.encode(Input))

clientSocket.close()
