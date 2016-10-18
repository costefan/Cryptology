import os
import sys
import subprocess
import shlex
import re
import hashlib


def check_system_info():
    try:
        out = subprocess.Popen(shlex.split("df /"), stdout=subprocess.PIPE).communicate()
        m = re.search(r'(/[^\s]+)\s', str(out))
    except Exception as err:
        print('You have trouble with {}'.format(err))
        sys.exit(0)

    info_to_hash = list(os.uname())
    info_to_hash.pop(-2)
    info_to_hash.append(m.group(1))
    info_to_hash = ",".join(info_to_hash)

    with open('./app/data.txt', 'r') as f:
        data = f.read()
        if not data == hashlib.sha224(
                info_to_hash.encode()
        ).hexdigest():
            raise Exception('Your pass wrong...')
