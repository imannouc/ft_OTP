# /goinfre/ismannou/miniconda3/envs/42AI-ismannou/bin/python for later
from time import time
import argparse
import hmac
import hashlib
import sys
import base64
import struct
import pyotp
import oathtool

def ft_otp(secret):
    key = base64.b32decode(testkey, True)
    timeFactor = int(time()) // 30
    timeBytes = struct.pack(">Q",timeFactor)
    # '>' : Big Endian.
    # 'Q' : unsigned long long (8 bytes)
    test = hmac.new(key,timeBytes,digestmod='sha1').digest()
    offsetIndex = test[-1] & 0xf
    code = (struct.unpack(">I",test[offsetIndex:offsetIndex + 4])[0] & 0x7fffffff) % 1000000
    print(f"{code:06}")


if __name__ == '__main__':
    secret = 'MNUGC2DBGBZQ===='
    # just a 64 byte hex code
    testkey = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf"
    ft_otp(testkey)
    # totp = pyotp.TOTP(key)
    # print('totp.now()')
    # print(totp.now())


    # print(oathtool.generate_otp(key))