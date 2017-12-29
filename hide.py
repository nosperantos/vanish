from os import listdir,getcwd,chdir,remove
from win32api import GetShortPathName
from sys import argv
from shutil import copy
import psyco
psyco.full()
dirname = GetShortPathName(argv[1])
chdir(dirname)
index = open(dirname+":index.dat","w")
for file in listdir(getcwd()):
   try:
      newname = ":"+file
      copy(file,newname)
      index.write(file)
      index.write('\n')
      remove(file)
   except:
      print "[x] Cannot hide %s"%file
      pass
index.close()