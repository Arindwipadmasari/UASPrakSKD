import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES 

# Prosesambilkunci
def getKey(keysize):
    key = os.urandom(keysize)
    return key


def getIV(blocksize):
    iv = os.urandom(blocksize)
    return iv

# Pengenkripsian gambar AES dengan penggunaan panjang blok 16 serta dengan nama ulang gambar hasil enkripsi
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16 
    encrypted_filename = "encryptedSKD.Arin_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2: 
            file2.write(ciphertext)
    return encrypted_filename

# Pengdeskripsian gambar AES dengan penggunaan panjang blok 16 sertai dengan nama ulang gambar hasil deskripsi
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    decrypted_filename = "decryptedSKD.Arin_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE)

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data)

    return decrypted_filename

#Taambah file foto yang akan di enkripsi
KEYSIZE = 32 
BLOCKSIZE = 16 
filename = "mawar.jpg" 

#ambil dari nilai
key = getKey(KEYSIZE) 
iv = getIV(BLOCKSIZE) 

encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)