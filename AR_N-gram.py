# -*- coding: utf-8 -*-
from nltk.util import ngrams
import codecs
#---------------------
infile = codecs.open("test.txt", 'r+', 'utf-8')
outfile = codecs.open("testout.txt", 'w+', 'utf-8')
words = infile.read()
sentences=words.split("\n")
infile.close()
n = 3
l=[]
s=""
d=""
l1=[]
l2=[]
for x in sentences:
  if len(x)>2:
    nn=len(x)
    for r in range(1,nn):
      xgrams = ngrams(x.split(" "),r)
      for grams in xgrams:
        l.append(grams)
for c in l:
  s=s+"\n"
  l1.append(d)
  if d not in l2 :
    l2.append(d)
  d=""
  for cc in c: 
     s=s+" "+cc
     d=d+" "+cc   
for b in l2:
    counter= l1.count(b)
    print counter , b
    outfile.write(b+" \t "+str(counter)+"\n")

outfile.close() 
