import socket
#import sys
import re
import hashlib
import base64
import threading
import struct
#import subprocess
 
def send(client, msg):
    data = bytearray(msg.encode('utf-8'))
    if len(data) > 126:
        data = bytearray([b'\x81', 126]) + bytearray(struct.pack('>H', len(data))) + data
    else:
        data = bytearray([b'\x81', len(data)]) + data
    client.send(data)
 
def recv(client):
    first_byte = bytearray(client.recv(1))[0]
    FIN = (0xFF & first_byte) >> 7
    opcode = (0x0F & first_byte)
    second_byte = bytearray(client.recv(1))[0]
    mask = (0xFF & second_byte) >> 7
    payload_len = (0x7F & second_byte)
    if opcode < 3:
        if (payload_len == 126):
            payload_len = struct.unpack_from('>H', bytearray(client.recv(2)))[0]
        elif (payload_len == 127):
            payload_len = struct.unpack_from('>Q', bytearray(client.recv(8)))[0]
        if mask == 1:
            masking_key = bytearray(client.recv(4))
        masked_data = bytearray(client.recv(payload_len))
        if mask == 1:
            data = [masked_data[i] ^ masking_key[i%4] for i in range(len(masked_data))]
        else:
            data = masked_data
    else:
        return opcode, bytearray(b'\x00')
    return opcode, bytearray(data)
 
def handshake(client):
    request = client.recv(2048)
    m = re.match('[\\w\\W]+Sec-WebSocket-Key: (.+)\r\n[\\w\\W]+\r\n\r\n', request)
     
    key = m.group(1)+'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
     
    response = "HTTP/1.1 101 Switching Protocols\r\n"+\
           "Upgrade: websocket\r\n"+\
           "Connection: Upgrade\r\n"+\
           "Sec-WebSocket-Accept: %s\r\n"+\
           "\r\n"
    r = response % ((base64.b64encode(hashlib.sha1(key).digest()),))
    client.send(r)
flag = 5
def handle_client (client, addr):
    global flag
    handshake(client)
    try:
        while 1:
            opcode, data = recv(client)
            if opcode == 0x8:
                print 'close frame received'
                break
            elif opcode == 0x1:
                if len(data) == 0:
                    break
                msg = data.decode('utf-8', 'ignore')
                send(client, "echo : " + msg)
                print msg
                flag = msg
                '''
                try:
                    output = unicode(subprocess.check_output(msg, stderr=subprocess.STDOUT, shell=True), 'cp949')
                except subprocess.CalledProcessError as cpe:
                    output = unicode(cpe.output, 'cp949')
                print output
                send(client, output)
                '''
            else:
                print 'frame not handled : opcode=' + str(opcode) + ' len=' + str(len(data))
                 
    except Exception as e:
        print str(e)
    print "disconnected"
    client.close()
 
#start_server(8765)
class firebaseServer:
    def __init__(self, port):
        self.start_server(port);

    def start_server(self, port):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(5)
        print 'Waiting for connection on port' + str(port) + ' ...'
        self.client, self.addr = self.sock.accept()
        print 'Connection from : ' + str(self.addr)
        self.thread = threading.Thread(target = handle_client, args = (self.client, self.addr)).start()
        '''
        while True:
            chat = str(raw_input("input data : "));
            send(client, "database.ref('/hanzo').set('"+ str(chat) +"');")A
        '''

    def update(self, url, value):
        send(self.client, "database.ref('"+str(url)+"').set('"+ str(value) +"');")

    def remove(self, url):
        send(self.client, "database.ref('"+str(url)+"').remove();")

    def callback(self, url):
        send(self.client, "database.ref('"+str(url)+"').remove();")

