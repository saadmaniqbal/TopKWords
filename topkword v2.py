# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 06:51:18 2019

@author: Nutu
"""

import string
import sys
from string import punctuation

"""k = int(input("give me a number: "))"""
"""get the value of k"""

inputFile = open("input.txt",encoding='windows-1252')
if inputFile.mode == 'r':
    i=0
    #punctuations = """`~!@#$%^&*()-_+=\|]}[{"':;?/>.<,"""
    
    contents = inputFile.read()
    
    #contents = ''.join(a for a in contents if a not in punctuation)
    contents = contents.lower()
    #print(contents)
    content1 = contents.split(';')
    print(content1)
    
    
print(content1[0].split('='))
#print(i)
#Read input from console
#inputCmd = str(sys.argv[1])
#inputDict = dict(map(lambda x: x.split('='), inputCmd.split(';')))
#inputPath = inputDict['input']
#k = int(inputDict['k'])
    
#account for all sort of input output and k values mismatched
"""if k<1:
    print("please enter a valid input")
elif not k.isdigit():
    print("please enter a number")
else:
    print("please try again") #wrong
        """
#outputPath = inputDict['output']
#Read input from file
"""inputFile = open("input.txt","r")

content = str((inputFile.read())).decode('utf-8')
strList = sorted(getListFromStr(content))
#print(strList)
#recursive function

def recursiveCount(ls, result={}):
   if ls:
       elem = ls.pop()
       if elem in result.keys():
           result[elem] = result[elem] + 1
           
       else:
           result[elem] = 1
          
       return recursiveCount(ls, result)  
   return sorted(result.items(), reverse=True,  key=lambda x: x[1])
wordWithCount = recursiveCount(strList)

#print(wordWithCount)
wordWithCountNew = {}


counter1=0
for a,b in wordWithCount:
    if a.isalpha():
        wordWithCountNew[a]= b
        
wordWithCountNew = sorted(wordWithCountNew.items() , reverse=True, key=lambda x: x[1])
listlength = len(wordWithCountNew)
#print(listlength)
i=0
j=0
l=0
while i<k :
    if (listlength > 1):
        if(l<listlength-1):
            if not(wordWithCountNew[l][1] == wordWithCountNew[l+1][1]):
                
                i+=1
            l+=1
        else:
            break
    elif listlength ==1:
        if k >=1:
            l=1
            break
    elif listlength == 0:
        break
    
print(wordWithCountNew) 
#wordWithCountNew = sorted(wordWithCountNew.items() , reverse=True, key=lambda x: x[1])
#print(l)

#need to fix the while loop for less values than k . also make sure they are only words, put a checker that checks if the key is an alphabet, eg. make a second tuple consisting of only alphabets
#also keep an account of what happens when all of them are asked to be printed. finally fix the situation of i<k  
    
 #   for j,k in wordWithCount:
        
  #      i=3
#Write result to file
#result = " ".join( k + " "+ str(v) for (k, v) in wordWithCount)
  
#print(wordWithCount)
#outputFile = open(outputPath,"w+")
counter = 0
while counter<l:
    print(wordWithCountNew[counter][0] + " " +str(wordWithCountNew[counter][1]))
    counter+=1

if (counter !=0) and (counter == l):
    print(wordWithCountNew[counter][0] + " " +str(wordWithCountNew[counter][1]))
#print(result)

#outputFile.close()


#need to fix the while loop for less values than k . also make sure they are only words, put a checker that checks if the key is an alphabet, eg. make a second tuple consisting of only alphabets
#also keep an account of what happens when all of them are asked to be printed. finally fix the situation of i<k  
    
 #   for j,k in wordWithCount:
        
  #      i=3
#Write result to file
#result = " ".join( k + " "+ str(v) for (k, v) in wordWithCount)
  
#outputFile = open(outputPath,"w+")
#counter = 0
#while counter<l:
#    print(wordWithCountNew[counter][0] + " " +str(wordWithCountNew[counter][1]))
#    counter+=1
#print(result)

#outputFile.close()"""
