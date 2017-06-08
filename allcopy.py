#!/usr/local/bin/python3.5
# -*- coding: UTF-8 -*-

import os
import shutil
os.chdir('C:\\') #Make sure you add your source and destination path below

dir_src = (r"D:\Dokumentumok\Nekem\Python\\")
dir_dst = (r"D:\raspberrypi\Python\\")

print("Másolás innen:")
print(dir_src)
print("Ide:")
print(dir_dst)
print()

lista = os.listdir(dir_src)
kiterjesztes=".py"

for filename in lista:
    if filename.endswith(kiterjesztes):
        shutil.copy( dir_src + filename, dir_dst)
        print("A következő fájl másolása:", filename)
