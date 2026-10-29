import socket
import threading

host = ''
port = 64932


def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    print "Server start..."
    while True:
        c, addr = s.accept()
        print str(addr)
        print "connected"
        buf = c.recv(1024)
        if("Settings" in buf):
            print buf
            writeIn = open("Settings.txt", "w")
            writeIn.write(buf)
            writeIn.close()
        elif("Wlan" in buf):
            print buf
            writeIn = open("Wlan.txt", "w")
            writeIn.write(buf)
            writeIn.close()
        elif("WName" in buf):
            print buf
            writeIn = open("WName.txt", "w")
            writeIn.write(buf)
            writeIn.close()
        elif("Stream" in buf):
            print buf
            writeIn = open("Stream.txt", "w")
            writeIn.write("1")
            writeIn.close()
        elif("Finish" in buf):
            writeIn = open("Stream.txt", "w")
            writeIn.write("0")
            writeIn.close()
        print buf
        print "Fertig"


if __name__ == '__main__':
    Main()
