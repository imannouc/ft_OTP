# ft_otp

The aim of this Project is to implement a TOTP (Time-based One-Time Password)
system.

## Resources :
#### TOTP: Time-Based One-Time Password Algorithm

https://datatracker.ietf.org/doc/html/rfc6238

#### HOTP: An HMAC-Based One-Time Password Algorithm

https://datatracker.ietf.org/doc/html/rfc4226

### Requirements :

    pip3 install pyotp # This module is used to test the results of my own otp function
    pip3 install cryptography
    pip3 install qrcode


## Usage :

    usage: ft_otp [-h] [-g G | -k K]

    generate a time-based one time password

    options:
    -h, --help  show this help message and exit
    -g G        takes a .hex file that contains a hexadecimal password with at least 64 bytes.
                and generates an encrypted .key file from it.
    -k K        takes a .key file and generates a new TOTP and displays it in the standard output
