import hmac, base64, struct, hashlib, time
import pyotp,sys

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    print(key)
    print(bytes(secret,'utf-8'))
    #decoding our key
    # key = bytes(secret,'utf-8')
    msg = struct.pack(">Q", intervals_no)
    #conversions between Python values and C structs represente
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[-1] & 15
    #Generate a hash using both of these. Hashing algorithm is HMAC
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    #unpacking
    return h

def get_totp_token(secret):
    #ensuring to give the same otp for 30 seconds
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    #adding 0 in the beginning till OTP has 6 digits
    while len(x)!=6:
        x+='0'
    return x
#base64 encoded key
secret = 'MNUGC2DBGBZQ===='
key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(get_totp_token(secret))
totp = pyotp.TOTP(secret)
print('totp.now()')
print(totp.now())
