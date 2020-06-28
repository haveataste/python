import socket
import ctypes
import time

class NTP_Packet(ctypes.Structure):
    _fields_=[
        ('Control_Word',ctypes.c_int),
        ('root_delay',ctypes.c_int),
        ('root_dispersion',ctypes.c_int),
        ('reference_identifier',ctypes.c_int),
        ('reference_timestamp',ctypes.c_longlong),
        ('originate_timestamp',ctypes.c_longlong),
        ('receive_timestamp',ctypes.c_longlong),
        ('transmit_timestamp_seconds',ctypes.c_int),
        ('transmit_timestamp_fractions',ctypes.c_int)
    ]

def getTime():
    NTP_Send = NTP_Packet()
    NTP_Send.Control_Word = socket.htonl(0x0B000000)
    NTP_Send.root_delay = 0
    NTP_Send.root_dispersion = 0
    NTP_Send.reference_identifier = 0
    NTP_Send.reference_timestamp = 0
    NTP_Send.originate_timestamp = 0
    NTP_Send.receive_timestamp = 0
    NTP_Send.transmit_timestamp_seconds = 0
    NTP_Send.transmit_timestamp_fractions = 0
    #把结构体发送出去
    bytes= ctypes.string_at(ctypes.addressof(NTP_Send), ctypes.sizeof(NTP_Send))
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    NTP_HOST = 'ntp.aliyun.com'
    soc.sendto(bytes, (NTP_HOST, 123))
    data, addr =soc.recvfrom(2048)
    soc.close()
    #将二进制数据拷贝到结构体
    NTP_Recv = NTP_Packet()
    ctypes.memmove(ctypes.addressof(NTP_Recv), data, ctypes.sizeof(NTP_Recv))
    #计算服务器的时间
    TIME_1970 = 2208988800
    ntp_time = socket.ntohl(NTP_Recv.transmit_timestamp_seconds) - TIME_1970
    #print('Local Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('NTP Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ntp_time)), ntp_time, NTP_Recv.transmit_timestamp_seconds)

getTime()
