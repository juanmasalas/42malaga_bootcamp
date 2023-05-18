import hmac, base64, hashlib, struct, time, re, argparse, qrcode
from cryptography.fernet import Fernet, InvalidToken

master_key = b'D9Nemtr75yUJqJQ0ZqP7Tj7IJWtXHZFtccukiZnBsoQ='


def args_init():
    analizador = argparse.ArgumentParser(
        prog="./ft_otp",
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio 'ft_otp' del Bootcamp de Ciberseguridad de la Fundación 42 (Málaga).",
    )

    analizador.add_argument(
        "-g",
        help="Almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        action='store_true')
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str)

    return analizador.parse_args()



def input_():
    password = input()
    password_hex = password.encode('utf-8').hex()
    print(f"\nResult of the string converted to Hexadecimal")
    print(password_hex)
    if not re.match(r'^[0-9a-fA-F]{64,}$', password_hex):
        print(f"\nThe key is not hexadecimal or is less than 64 characters.\n")  
        exit()
    hex2bytes = bytes(password_hex, 'utf-8')
    bytes2b32 = base64.b32encode(hex2bytes)
    secret = bytes2b32.decode('utf-8')
    # print(secret)
    print(f"\nSuccessfully generated secret and QR code")
    return secret
      
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    while len(x)!=6:
        x+='0'
    return x

def encrypt_data(secret):
    with open ("ft_otp.key", "w") as key:
        key.write(secret)
    with open("ft_otp.key", "rb") as fi:
        file_data = fi.read()
        f = Fernet(master_key)
        token = f.encrypt(file_data)
    with open ("ft_otp.key", "wb") as f:
        f.write(token)
    return token

def decrypt_data():
    try:
        with open(gen_token, "rb") as fa:
            file_data = fa.read()
            f = Fernet(master_key)
            token_decrypt = f.decrypt(file_data)
            return token_decrypt
    except (FileNotFoundError, InvalidToken, IsADirectoryError):
        print("\n\033[31mInvalid file. You should enter a valid file.key.\033[39m\n")
        exit()

def generator_qr(secret):
    qrtest = "otpauth://totp/FT_OTP:BootcampCybersecurity?secret=" + secret+"&issuer=FT_OTP"
    obj = qrcode.make(qrtest)
    imgQr = open("qr.png","wb")
    obj.save(imgQr)
    imgQr.close()


        
# ================================================================================ 

if __name__ == "__main__":

    args = args_init()

    gen_key = args.g
    gen_token = args.k
    

    if gen_key:
        print(f"\nPlease enter a text string of at least 32 characters.To convert to a Hexadecimal string of at least 64 characters.")
        secret = input_()
        token = encrypt_data(secret)
        generator_qr(secret)
    elif gen_token:  
            token_decrypt = decrypt_data()
            print(get_totp_token(token_decrypt))
                   
    else:
        print("\n\033[31mCheck usage model with -h.\033[39m\n")
