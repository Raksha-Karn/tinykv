import socket

def test_ping_returns_pong():
    with socket.create_connection(("127.0.0.1", 6379), timeout=2) as sock:
        sock.sendall(b"*1\r\n$4\r\nPING\r\n")
        response = sock.recv(1024)
        assert response == b"+PONG\r\n"
