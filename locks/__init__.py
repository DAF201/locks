import os
import time
import site


PATH = site.getusersitepackages()+'\\\\timer.txt'
# LOCK_PATH = site.getsitepackages()[-1]+'\\usercustomize.py'


def lock_unlock():
    if os.path.isfile(PATH):
        with open(PATH, 'r')as rec:
            rec_time = rec.read()
            # print(rec_time)
        if int((str(time.time()-float(rec_time))).split('.')[0]) > 5:
            os.remove(PATH)
            print('unlocking python')
        else:
            with open(PATH, 'w')as rec:
                rec.write(str(time.time()))
            print('python is locked,please try again at %s' %
                (time.ctime(time.time()+3600)))
            os._exit(0)


def create_lock():
    if os.path.isfile(PATH) == False:
        with open(PATH, 'w')as rec:
            rec.write(str(time.time()))
            print('creating lock')
        os._exit(0)
    else:
        with open(PATH, 'r')as rec:
            rec_time = rec.read()
        print('lock existed, will be unlocked at %s' %
              time.ctime(float(rec_time)+3600))


