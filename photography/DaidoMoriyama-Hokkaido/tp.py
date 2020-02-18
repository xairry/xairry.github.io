# coding = utf-8
import os
arr = []
for file in os.walk("../DaidoMoriyama-Hokkaido"):
  
  for n in file[2]:
    #print('!['+ n.split('.')[0] +']('+n+')  ')
    arr.append('!['+ n.split('.')[0] +']('+n+')\\n')

print(len(arr))