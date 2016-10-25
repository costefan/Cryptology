import os

import hashlib

from Crypto import Random
from Crypto.Cipher import AES


class RDSCryptor:

    def __init__(self, rds_manager_path, os_path=False):
        """Used to define key for symmetric encryption

        :return:
        """
        self.key = hashlib.md5('admin_pass'.encode()).digest()
        if os_path:
            # encrypted file, MUST be stored in repository
            self.passfile_enc = os.path.join(
                rds_manager_path, 'credentials.txt.enc'
            )
            # decrypted file
            self.passfile_dec = os.path.join(
                rds_manager_path, 'credentials.txt'
            )
        else:
            # encrypted file, MUST be stored in repository
            self.passfile_enc = '{}/{}'.format(
                rds_manager_path, 'credentials.txt.enc'
            )
            # decrypted file
            self.passfile_dec = '{}/{}'.format(
                rds_manager_path, 'credentials.txt'
            )

    @staticmethod
    def pad(s):
        return s + b" " * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, msg):
        msg = self.pad(msg)
        # iv - initialization vector
        # с помощью него шифруют первый блок
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        return iv + cipher.encrypt(msg)

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(ciphertext[AES.block_size:])

        return plain_text.rstrip(b'')

    def encrypt_file(self):

        with open(self.passfile_dec, 'rb') as fo:
            plain_text = fo.read()
        encrypted_text = self.encrypt(plain_text)
        os.remove(self.passfile_dec)
        with open(self.passfile_enc, 'wb') as fo:
            fo.write(encrypted_text)

    def decrypt_file(self):

        with open(self.passfile_enc, 'rb') as fo:
            text = fo.read()
        text = self.decrypt(text)

        with open(self.passfile_dec, 'wb') as fo:
            fo.write(text)


if __name__ == '__main__':
    rds_manager_path = '/home/costefan/university/Cryptology/LAB3/'
    cryptor = RDSCryptor(rds_manager_path, os_path=True)
    a = int(input('input param'))
    if a == 1:
        cryptor.encrypt_file()
    elif a == 2:
        cryptor.decrypt_file()

