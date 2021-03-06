# Many thanks to Suraj Singh at BitForestInfo for his great article: http://www.bitforestinfo.com/2017/12/code-to-create-tcp-packet-header-with-python-socket-module.html
import socket
import struct


# Validates a given IP address
def validate_ip(addr):
    octets = addr.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False

    return True

class TCPPacket:

 def __init__(self, dport, sport, dst, src, data = ''):
  self.dport = dport
  self.sport = sport
  self.src_ip = src
  self.dst_ip = dst
  self.data   = data
  self.raw = None
  self.create_tcp_fields()

 def create_tcp_fields(self):

  # ---- [ Source Port ]
  self.tcp_src = self.sport

  # ---- [ Destination Port ]
  self.tcp_dst = self.dport

  # ---- [ TCP Sequence Number]
  self.tcp_seq = 0

  # ---- [ TCP Acknowledgement Number]
  self.tcp_ack_seq = 0

  # ---- [ Header Length ]
  self.tcp_hdr_len = 80

  # ---- [ TCP Flags ]
  # TODO: set flags singularly
  tcp_flags_rsv = (0 << 9)
  tcp_flags_noc = (0 << 8)
  tcp_flags_cwr = (0 << 7)
  tcp_flags_ecn = (0 << 6)
  tcp_flags_urg = (0 << 5)
  tcp_flags_ack = (0 << 4)
  tcp_flags_psh = (0 << 3)
  tcp_flags_rst = (0 << 2)
  tcp_flags_syn = (1 << 1)
  tcp_flags_fin = (0)

  self.tcp_flags = tcp_flags_rsv + tcp_flags_noc + tcp_flags_cwr + \
        tcp_flags_ecn + tcp_flags_urg + tcp_flags_ack + \
        tcp_flags_psh + tcp_flags_rst + tcp_flags_syn + tcp_flags_fin

  # ---- [ TCP Window Size ]
  # TODO: settable window
  self.tcp_wdw = socket.htons (5840)

  # ---- [ TCP CheckSum ]
  self.tcp_chksum = 0

  # ---- [ TCP Urgent Pointer ]
  # TODO: settable urg flag
  self.tcp_urg_ptr = 0


  return

 def assemble_tcp_fields(self):
  self.raw = struct.pack('!HHLLBBHHH', # Data Structure Representation
   self.tcp_src,   # Source IP
   self.tcp_dst,    # Destination IP
   self.tcp_seq,    # Sequence
   self.tcp_ack_seq,  # Acknownlegment Sequence
   self.tcp_hdr_len,   # Header Length
   self.tcp_flags ,    # TCP Flags
   self.tcp_wdw,   # TCP Windows
   self.tcp_chksum,  # TCP cheksum
   self.tcp_urg_ptr # TCP Urgent Pointer
   )

  self.calculate_chksum() # Call Calculate CheckSum
  return

 def calculate_chksum(self):
  src_addr     = socket.inet_aton( self.src_ip )
  dest_addr    = socket.inet_aton( self.dst_ip )
  placeholder  = 0
  protocol     = socket.IPPROTO_TCP
  tcp_len      = len(self.raw) + len(self.data)

  psh = struct.pack('!4s4sBBH' ,
   src_addr ,    # Source Address
   dest_addr ,   # Destination Address
   placeholder , # Placeholder
   protocol ,    # Protocol
   tcp_len       # Length of pseudo + Demo TCP header + Data
   )

  data = bytes(self.data, 'utf-8')

  psh = psh + self.raw + struct.pack('!%ds' % len(data), data)

  self.tcp_chksum = self.chksum(psh) # call CheckSum calculation function

  self.reassemble_tcp_fields()       # finally, reassemble all piece of information

  return

 def chksum(self, msg):
  s = 0  # Binary Sum
  print(str(msg))
  # loop taking 2 characters at a time
  for i in msg: #range(0, len(msg), 1):

   a = ord(chr(i))
   b = ord(chr(i))
   s = s + (a+(b << 8))


  # One's Complement
  s = s + (s >> 16)
  s = ~s & 0xffff
  return s

 def reassemble_tcp_fields(self):
  self.raw = struct.pack('!HHLLBBH',
   self.tcp_src,
   self.tcp_dst,
   self.tcp_seq,
   self.tcp_ack_seq,
   self.tcp_hdr_len,
   self.tcp_flags ,
   self.tcp_wdw
   )+ \
  struct.pack("H",
   self.tcp_chksum
   )+ \
  struct.pack('!H',
   self.tcp_urg_ptr
   )
  return
