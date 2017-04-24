import os, json
import face_recognition as fare
from numpy import savetxt

def getFiles(path):
  os.chdir(path)
  arr = []
  for file in os.listdir(path):
    if file.endswith(".jpg"):
      arr.append(os.path.join(path, file))
  return arr

files = getFiles("/home/images/references")

for f in files:
  image = fare.load_image_file(f)
  reference = fare.face_encodings(image)[0]
  head, tail = os.path.split(f)
  f = '/home/references/{filename}.txt'.format(filename=tail)
  savetxt(f, reference)
