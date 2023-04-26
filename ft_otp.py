# /goinfre/ismannou/miniconda3/envs/42AI-ismannou/bin/python for later
from time import time
import argparse
import oathtool
import hmac
import hashlib
import sys
import base64
import struct
import pyotp
def ft_otp():
    pass

if __name__ == '__main__':
    # just a 64 byte hex code
    key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # t = b"0fd5d94bc649d6dbfa0fbc3e6f6c034bf74f5528"
    # print(len(bytes('0fd5d94bc649d6dbfa0fbc3e6f6c034bf74f5528','utf-8')))
    timeFactor = int(time() // 30)
    timeBytes = struct.pack(">Q",timeFactor)
    print('sys.getsizeof(timeBytes)')
    print(sys.getsizeof(timeBytes))
    keyBytes = bytes(key,"utf-8")
    totp = pyotp.TOTP(key)
    print('totp.now()')
    print(totp.now())
    try:
        print('int(hex,16)')
        print(int(key,16))
    except ValueError as e:
        print('Invalid hex code.')
    test = hmac.new(keyBytes,timeBytes,digestmod='sha1')
    test = test.digest()
    offsetIdx = test[19] & 15
    bin_code = offsetIdx
    bin_code = test[offsetIdx] & 0x7f << 24 |\
        test[offsetIdx + 1]  & 0xff << 16 |\
        test[offsetIdx + 2]  & 0xff << 8 |\
        test[offsetIdx + 4]  & 0xff
    num = bin_code % 1000000
    print('str')
    print(str(num))
    print('offsetIdx')
    print(offsetIdx)
    print('bin_code')
    print(bin_code)
    print('NUM')
    print(num)


    # print(oathtool.generate_otp(key))