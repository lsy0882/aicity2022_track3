import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
import pdb

#Train Validation Split
'''
video_path = "/home/data/aicity/byvideo_224/"
driver_list = glob(video_path + "*")
driver_list.sort()
Train_dir = video_path + "Train"
Validation_dir = video_path + "Validation"
Train_driver = driver_list[0:4]
Train_driver.append(driver_list[5])
Validation_driver = []
for driver in driver_list:
    if driver not in Train_driver:
        Validation_driver.append(driver)
print("Train :", Train_driver)
print("Validation :", Validation_driver)


os.makedirs(Train_dir, exist_ok=True)
os.makedirs(Validation_dir, exist_ok=True)
for driver_name in Train_driver:
    print("mv {0} {1}".format(driver_name,Train_dir))
    command = ("mv {0} {1}".format(driver_name,Train_dir))
    output = subprocess.call(command, shell=True, stdout=None)
for driver_name in Validation_driver:
    print("mv {0} {1}".format(driver_name,Validation_dir))
    command = ("mv {0} {1}".format(driver_name,Validation_dir))
    output = subprocess.call(command, shell=True, stdout=None)
# Space Deletion
print("rename 's/ //g' {0}*/*/*.npy".format(video_path))
command = ("rename 's/ //g' {0}*/*/*.npy".format(video_path))
output = subprocess.call(command, shell=True, stdout=None)


################
npy_list = glob("/home/data/aicity/byvideo_224/Train/*/*.npy")
npy_list.sort()
result_path = "/home/data/aicity/byclass_224/Train/"
for i in range(20):
    os.makedirs(result_path + str(i), exist_ok=True)
#pdb.set_trace()
print(len(npy_list))
for npy_n in npy_list:
    if ' ' in npy_n:
        print("Error :", npy_n)
        npy_n = npy_n.replace(" ","")
        print(npy_n)
    filename = os.path.basename(npy_n)
    file_l = filename.split('_')
    classname = file_l[1]
    try:
        classname = float(classname)
        classname = int(classname)
        print(filename, classname)

    except:
        classname = 18
        print(filename, classname)
        print("NA")
    print("mv {0} {1}{2}".format(npy_n, result_path, classname))
    command = ("mv {0} {1}{2}".format(npy_n, result_path, classname))
    output = subprocess.call(command, shell=True, stdout=None)
    #pdb.set_trace()

'''
npy_list = glob("/home/data/aicity/byvideo_224/Validation/*/*.npy")
npy_list.sort()
result_path = "/home/data/aicity/byclass_224/Validation/"
for i in range(20):
    os.makedirs(result_path + str(i), exist_ok=True)
#pdb.set_trace()
print(len(npy_list))
for npy_n in npy_list:
    filename = os.path.basename(npy_n)
    file_l = filename.split('_')
    classname = file_l[1]
    try:
        classname = float(classname)
        classname = int(classname)
        print(filename, classname)

    except:
        classname = 18
        print(filename, classname)
        print("NA")
    print("mv {0} {1}{2}".format(npy_n, result_path, classname))
    command = ("mv {0} {1}{2}".format(npy_n, result_path, classname))
    output = subprocess.call(command, shell=True, stdout=None)
    #pdb.set_trace()