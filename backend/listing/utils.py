import os
import random

def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'images/listing/{basename}{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr,
                                                                 ext=file_extension)
