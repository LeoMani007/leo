import socket as s
import select as sel
import subprocess as sb

HOST = 'localhost'
PORT = 80

server = s.socket(s.AF_INET,s.SOCK_STREAM)
server.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
server.bind((HOST,PORT))

server.listen(10)
print(f"server listening to port : {PORT}")
while True:
    client,addr=server.accept()
    print(f"server connected to {client}   and    {data}")
    try:
        data = client.recv(1024)
        if data.decode() == b'quit' or b'exit':
            client.close()
            break
        else:
            p = sb.Popen(addr.decode("utf-8"),shell=True,stdin=sb.PIPE,stdout=sb.PIPE,stderr=sb.PIPE)
            stdout,stderr=p.communicate()
            msg1 = stderr+stdout
            client.send(msg1.encode())
        client.close()
    except KeyError as e:
        print(e)
    finally:
        print("server closed ")
    
