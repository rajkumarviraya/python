import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

start = int(input("start port"))
stop  = int(input("stop port"))
ip = input("Enter IP Address:")


for i in range(start,stop):
    name = sock.connect_ex((ip,i))

    if name == 0:

        port = socket.getservbyport(i)

        print(f"{name} --> open {i} {port}")

    else:

        print(f"{name} --> {i} close ")


sock.close()




