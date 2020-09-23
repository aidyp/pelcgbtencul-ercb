from connector import netcat, to_json
from Crypto.Util.number import bytes_to_long, long_to_bytes

host = 'socket.cryptohack.org'
port = 13391

'''
Server takes a digest of my message
Server does a 'calculated digest' which is sig^e mod N
Server checks if digest bytes == calculated digest bytes

if msg matches ('^I am Mallory.*own Cryptohack.org$'), win

received signature is
sig = digest(msg) ^ d (N)

Server allows me to provide my own values of N, and (e). 



'''


def get_signature():
    content = '{\"option\":\"get_signature\"}'
    data = netcat(host, port, content)
    proc = to_json(data)
    proc['N'] = int(proc['N'][2:], 16)
    proc['e'] = int(proc['e'][2:], 16)
    proc['signature'] = int(proc['signature'][2:], 16)
    return proc

def pack_verification(N, e, msg):
    content = {'option':'verify'}

def send_verification()

def interrogate_signature(proc):
    print('N = ' + str(proc['N']))
    print('e = ' + str(proc['e']))
    print('sig = ' + str(proc['signature']))

def verify(proc):
    v = pow(proc['signature'], proc['e'], proc['N'])
    print(long_to_bytes(v))



ret = get_signature()
interrogate_signature(ret)
verify(ret)