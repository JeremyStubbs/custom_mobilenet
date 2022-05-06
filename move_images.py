import os
import shutil
import random
import glob

PATH = "/Users/jeremystubbs/Desktop/Python/Machine_Learning_NNs/Mobilenet/custom/archive/"

os.chdir(PATH)

for folder_name in os.listdir('train'):
    if folder_name[0]!= ".":
        os.chdir(PATH+'train/'+folder_name)
        print('train/'+folder_name)
        # if os.path.isdir('valid/{folder_name}') is False:
        #     os.makedir('valid/{folder_name}')
        for c in random.sample(glob.glob(folder_name+'*'), 500):
            shutil.move(c, PATH+'valid/'+folder_name)


