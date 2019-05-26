import socket


def communicate(host, port, request):
    s = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    response = s.recv(1042)
    s.close()
    return response
