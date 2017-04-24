import os, json
import face_recognition as fare
from numpy import loadtxt

def getFiles(path):
  os.chdir(path)
  arr = []
  for file in os.listdir(path):
    if file.endswith(".txt"):
      arr.append(os.path.join(path, file))
  return arr

jingtian = fare.load_image_file("images/liyitong2.jpg")
source = fare.face_encodings(jingtian)[0]


files = getFiles("/home/references")


fmat = ''

for f in files:
  ref = loadtxt(f)
  compares = fare.compare_faces([ref], source, 0.9)
  result = compares[0]
  if result == True:
    fmat = f
    break

print ('Result is : {fmat}'.format(fmat=fmat))
