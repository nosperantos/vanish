from os import listdir,getcwd,chdir,remove
from win32api import GetShortPathName
from sys import argv
from shutil import copy
import psyco
psyco.full()
dirname = GetShortPathName(argv[1])
chdir(dirname)
index = open(dirname+":index.dat").readlines()
for file in index:
   file = ":"+file.strip()
   newname = file[1:]
   try:
      copy(file,newname)
   except:
      print "[x] Cannot unhide %s"%file
      pass
   remove(file)
remove(":index.dat")