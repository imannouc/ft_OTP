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
from cryptography.fernet import Fernet
import qrcode

master_key = b'Ks1Aq6pbmXJbopmn_kKetz-P6KJkemGWJx9JzGjIj3U='

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

def check_hex_msg(hexMsg):
    try:
        int(hexMsg,16)
        if (len(hexMsg) < 64):
            raise(ValueError)
    except ValueError as e:
        print('./ft_otp: error: key must be 64 hexadecimal characters.')
        exit(2)

if __name__ == '__main__':
    secret = 'MNUGC2DBGBZQ===='
    # just a 64 byte hex code
    testkey = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf"
    parser = argparse.ArgumentParser(description='WHATEVER')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g',type=str,help='takes a .hex file that contains a hexadecimal password with at least 64 bytes. And generates an encrypted .key file from it.')
    group.add_argument('-k',type=str,help='takes a .key file and generates a new OTP and displays it in the standard output')
    args = parser.parse_args()
    if (args.g != None):
        pass
        # go open .hex file, read it, encrypt it,open a .key file ,write the encrypted msg in a .key file
        try:
            with open(args.g, 'r') as f:
                hexMsg = f.read()
            check_hex_msg(hexMsg)
            print('Key was successfully saved in ft_otp.key.')
            f = Fernet(master_key)
            encryptedMsg = f.encrypt(bytes(hexMsg,'utf-8'))
            with open('ft_otp.key','w') as f:
                f.write(f"{encryptedMsg.decode()}")
        except Exception as e:
            print(e)
    elif(args.k != None):
        # go open .key file, read it, decrypt it, obtain the hex , pass the hex to ft_otp
        try:
            with open(args.k) as f:
                encryptedMsg = f.read()
            f = Fernet(master_key)
            # print('encryptedMsg : ', encryptedMsg)
            hexMsgBytes = f.decrypt(encryptedMsg)
            hexMsg = hexMsgBytes.decode()
            print('hexMsgBytes : ', hexMsgBytes)
            print('hexMsg : ', hexMsg)
            # hexMsg = base64.b32encode(bytes.fromhex(hexMsg))
            # print('hexMsgBytes : ', hexMsgBytes)
            # print('hexMsg : ', bytes.decode(hexMsg))
            # uri = pyotp.totp.TOTP(hexMsg).provisioning_uri(name='testOtp',issuer_name='ft_otp')
            # print('uri',uri)
            uri = f"otpauth://totp/:ft_otp?secret={hexMsg}&issuer=ft_otp"
            t = qrcode.make(uri)
            t.save('qrcode.png')
            ft_otp(hexMsg)
        except Exception as e:
            print(e)


    # totp = pyotp.TOTP(key)
    # print('totp.now()')
    # print(totp.now())


    # print(oathtool.generate_otp(key))–––