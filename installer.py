import os
import sys
import subprocess
import shlex
import re
import hashlib
from fixtures.create_users import users_data
from cryptor import RDSCryptor

directory_path = str(input('Print here please dir tha file will be placed: '))
file_path = str(input('Input path to the file  program will start: '))

try:

    out = subprocess.Popen(shlex.split("df /"), stdout=subprocess.PIPE).communicate()
    m = re.search(r'(/[^\s]+)\s', str(out))
    os.system('pyinstaller --distpath={} {}'.format(
        directory_path, file_path
    ))
except Exception as err:
    print('You have trouble with {}'.format(err))
    sys.exit(0)

info_to_hash = list(os.uname())
info_to_hash.pop(-2)
info_to_hash.append(m.group(1))
info_to_hash = ",".join(info_to_hash)
with open("{}{}/data.txt".format(
        directory_path, file_path.split('.')[0]), 'w+'
) as f:
    f.write(
        hashlib.sha224(info_to_hash.encode()).hexdigest()
    )

fixtures_path = "{}{}/credentials.txt.exp".format(
    directory_path, file_path.split('.')[0]
)

# Creating file with fixture data for admin
if not os.path.isfile(fixtures_path):
    rds_manager_path = '{}{}'.format(directory_path, file_path.split('.')[0])
    cryptor = RDSCryptor(rds_manager_path)
    string = ' '.join(str(key) + '=' + str(value)
                      for key, value in users_data.items())
    string = cryptor.encrypt(string.encode())

    with open(cryptor.passfile_enc, 'wb+') as fo:
        fo.write(string)
