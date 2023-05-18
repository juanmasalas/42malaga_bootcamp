import string, secrets, base64, re




def hex_gen():
    hex = string.hexdigits
    pwd_len = 64
    pwd = ''
    for i in range(pwd_len):
        pwd += ''.join(secrets.choice(hex))
    # return pwd
    with open ("key.hex", "w") as f:
        f.write(pwd)
    return pwd


key = hex_gen()
print(" File 'key.hex' gerenate with = " + key)