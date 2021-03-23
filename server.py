import socket
from _thread import * 


userList  = {} # ip : isim
clientLis = [] # client 

# host : port : socket 

host = "localhost" # sunucunu ip adresini yaz
port = 4545        # isteğe bağlı 
s = socket.socket()

# connect and listen port

try:
	s.bind((host , port))
	s.listen()
except:
	print("hata - 1")
	

print("Bağlantı bekleniyor . . .")

# create thread function 

def broadCast(kullanici , number):
	name = kullanici.recv(1024)
	userList[number] = name.decode('utf-8')
	oturumMesaj = userList[number]+" odaya katıldı "
	
	f = open("login.txt" , "a" , encoding='utf-8')
	yaz = userList[number]+" : " + iport[0]+"\n"
	f.write(yaz)
	f.close()
	
	for i in clientLis:
		i.send(oturumMesaj.encode())
		
	# odaya katılan kullanıcının ismini herkese gönder 
	
	while True:
		try:
			gelen = kullanici.recv(1024)
			gelen = gelen.decode('utf-8')
			
			# bu mesajı bütün kullanıcılara gönderelim 
			# kimden geldiği bilgisini de ekleyelim 
			gelen = userList[number]+"#"+gelen
			
			for i in clientLis:
				i.send(gelen.encode())
		except:
			# hata almışsam kullanici nın bağlantısı kopmuştur .
			# clientLis den silmem gerekli
			clientLis.remove(kullanici)
			# ve bu process in sonlanabilmesi için döngüden çıkmam gerekir
			# çıkmadan önce diğer kullanıcılara kimin çıktığını söylemeliyim 
			gonder = userList[number]+" odadan ayrıldı"
			for i in clientLis:
				i.send(gonder.encode())
			break
		

# finish function

while True:
	istemci , iport = s.accept() # gelen bağlantı isteğini kabul ediyor 
	clientLis.append(istemci)
	print(iport[0] , " bağlandı") # iport[0] : ip , iport[1] : port no  
	start_new_thread(broadCast , (istemci , iport[0] ,)  )
	
# 
# github.com/daddydemir


