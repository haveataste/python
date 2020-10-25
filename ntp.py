import socket
import ctypes
import time

class NTP_Packet(ctypes.Structure):
    _fields_ = [
         ('Control_Word', ctypes.c_uint),
         ('root_delay', ctypes.c_uint),
         ('root_dispersion', ctypes.c_uint),
         ('reference_identifier', ctypes.c_uint),
         ('reference_timestamp', ctypes.c_ulong),
         ('originate_timestamp', ctypes.c_ulong),
         ('receive_timestamp', ctypes.c_ulong),
         ('transmit_timestamp_seconds', ctypes.c_ulong),
         ('transmit_timestamp_fractions', ctypes.c_longlong)
    ]

def getTime(NTP_HOST, NTP_PORT=123):
    NTP_Send = NTP_Packet()
    NTP_Send.Control_Word = socket.htonl(0x23000000)
    NTP_Send.root_delay = 0
    NTP_Send.root_dispersion = 0
    NTP_Send.reference_identifier = 0
    NTP_Send.reference_timestamp = 0
    NTP_Send.originate_timestamp = 0
    NTP_Send.receive_timestamp = 0
    NTP_Send.transmit_timestamp_seconds = 0
    NTP_Send.transmit_timestamp_fractions = 0
    #把结构体发送出去
    data_send = ctypes.string_at(ctypes.addressof(NTP_Send), ctypes.sizeof(NTP_Send))
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    soc.sendto(data_send, (NTP_HOST, NTP_PORT))
    
    (data_recv, addr) =soc.recvfrom(2048)
    soc.close()
    #将二进制数据拷贝到结构体
    NTP_Recv = NTP_Packet()
    ctypes.memmove(ctypes.addressof(NTP_Recv), data_recv, ctypes.sizeof(NTP_Recv))
    #计算服务器的时间
    tbn = bin(NTP_Recv.transmit_timestamp_seconds)[2:].zfill(64)
    tbh = tbn[56:64] + tbn[48:56] + tbn[40:48] + tbn[32:40] + tbn[24:32] + tbn[16:24] + tbn[8:16] + tbn[0:8]
    TIME_1970 = 2208988800
    ntp_time = int(tbh, 2) - TIME_1970
    return ' NTP Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ntp_time)) + ' Server : ' + addr[0] + ' Port : ' + str(addr[1])
    
def main():
    print('Local Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(getTime('ntp1.aliyun.com'))`

if __name__ == "__main__":
    main()
