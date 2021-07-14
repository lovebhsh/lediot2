from gpiozero import LED
from time import sleep
import socket

my_led = LED(4)

localIP = socket.gethostbyname('raspberrypi13.local')
localPort = 20001
bufferSize = 1024
my_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
my_socket.bind((localIP, localPort))

while(True): 
    msg, addr = my_socket.recvfrom(1024) 
    recv_msg = msg.decode(encoding='UTF8') 
    address = "from addr:{}".format(addr)
    
    if recv_msg == "on":
        print("LED on")
        my_led.on()
    elif recv_msg == "off":
        print("LED off")
        my_led.off()
    
    print(recv_msg) 
    print(address)
    my_socket.sendto(str.encode('잘받았다'), addr)

    