#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
import os
import shutil
#
os.system('clear')
print("################################################################################")
print()
dir_src=input(" Copy from [Full path] : ")
dir_dst=input(" Copy to   [Full path] : ")
ext=input(" File extension (e.g.: .BMP) : ")
print()
print("################################################################################")
#
print()
print(" Copy from :", dir_src)
#print(dir_src)
print(" Copy to :", dir_dst)
#print(dir_dst)
print()
print("################################################################################")
array = os.listdir(dir_src)

for filename in array:
    if filename.endswith(ext):
        shutil.copy( dir_src + filename, dir_dst)
#        print("A következő fájl másolása:", filename)
