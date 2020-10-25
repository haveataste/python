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
         ('origin_timestamp', ctypes.c_ulong),
         ('receive_timestamp', ctypes.c_ulong),
         ('transmit_timestamp_seconds_zs', ctypes.c_uint),
         ('transmit_timestamp_seconds_xs', ctypes.c_uint),
         ('transmit_timestamp_fractions', ctypes.c_longlong)
    ]

def getTime(NTP_SERVER, NTP_PORT=123):
    NTP_Send = NTP_Packet()
    NTP_Send.Control_Word = socket.htonl(0x23000000)
    NTP_Send.root_delay = 0
    NTP_Send.root_dispersion = 0
    NTP_Send.reference_identifier = 0
    NTP_Send.reference_timestamp = 0
    NTP_Send.origin_timestamp = 0
    NTP_Send.receive_timestamp = 0
    NTP_Send.transmit_timestamp_seconds_zs = 0
    NTP_Send.transmit_timestamp_seconds_xs = 0
    NTP_Send.transmit_timestamp_fractions = 0

    data_send = ctypes.string_at(ctypes.addressof(NTP_Send), ctypes.sizeof(NTP_Send))
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    soc.sendto(data_send, (NTP_SERVER, NTP_PORT))
    (data_recv, addr) =soc.recvfrom(2048)
    soc.close()

    NTP_Recv = NTP_Packet()
    ctypes.memmove(ctypes.addressof(NTP_Recv), data_recv, ctypes.sizeof(NTP_Recv))
    TIME_1970 = 2208988800
    ntp_time = socket.ntohl(NTP_Recv.transmit_timestamp_seconds_zs) - TIME_1970
    return '  NTP Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ntp_time)) + ' Server : ' + addr[0] + ' Port : ' + str(addr[1])

def main():
    print('Local Time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(getTime('ntp1.aliyun.com'))
    print(getTime('time1.cloud.tencent.com'))

if __name__ == "__main__":
    main()
