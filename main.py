import wx # GUI 프로그램을 위한 패키지 임포트
import myframe as mf # myframe 모듈을 mf로 별칭하기

import socket 

ip_addr = socket.gethostbyname('raspberrypi13.local')
serverAddressPort = (ip_addr, 20001) #내 메세지를 받을 주소.
bufferSize = 1024 
c_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # 소켓생성

class LedController(mf.LedControl):
    def led_on(self, event):
        print("엘이디가 켜졌다.")
        c_socket.sendto(str.encode("on"), serverAddressPort)

    def led_off(self, event):
        print("엘이디가 꺼졌다.")
        c_socket.sendto(str.encode("off"), serverAddressPort)

my_app = wx.App() # 하나의 앱을 생성한다.
frame = LedController(parent=None) # 설계한 디자인 하나의 객체로 생성
frame.Show() # 객체를 보여줍니다.
my_app.MainLoop() #계속 실행될 수 있도록 메인루프를 가동합니다.

