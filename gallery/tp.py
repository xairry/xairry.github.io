# coding = utf-8
import os
arr = []
for file in os.walk("../_posts/ArakiNobuyoshi-sentimentaljourney"):
  
  for n in file[2]:
    print('!['+ n.split('.')[0] +']('+n+')  ')
    #arr.append('!['+ n.split('.')[0] +']('+n+')\\n')

#print(arr)