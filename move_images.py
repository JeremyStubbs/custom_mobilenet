import os
import shutil
import random
import glob

PATH = "/Users/jeremystubbs/Desktop/Python/Machine_Learning_NNs/Mobilenet/custom/asl_images/"

os.chdir(PATH)

target = "."

# for folder_name in os.listdir('train'):
#     if folder_name[0]!= target:
#         valid_folder = PATH + "valid/"+folder_name
#         if os.path.isdir(valid_folder) is False:
#             os.mkdir(valid_folder)
    

for folder_name in os.listdir('train'):
    if folder_name[0]!= target:
        os.chdir(PATH+'train/'+folder_name)
        for c in random.sample(glob.glob('image*'), 200):
            shutil.move(c, PATH+'valid/'+folder_name)


