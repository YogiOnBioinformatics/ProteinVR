import os
import sys  

#PATH INPUT 
path = r"C:/Users/Yogindra Raghav/Documents/Yogindra/cs1501/Project 4" #CHANGE THIS AS NEED BE!!!!!!!!!!!!!!!

#SET OUTPUT DIRECTORY
outputdir = r"C:/Users/Yogindra Raghav/Desktop/" #CHANGE THIS AS NEED BE!!!!!!!!!!!!!!!!!!!!!
if not outputdir.find("\\") == -1:
    print("You need to enter the output directory name without using a backwards slash! USE ONLY FORWARD SLASHES!")
    sys.exit(0)
if not outputdir.endswith("/"):
    outputdir = outputdir+"/"

#CHANGE DIRECTORIES  
os.chdir(path)

#GET LIST OF ALL ITEMS IN THE DIRECTORY CHOSEN
items = os.listdir(path)

#CREATE NEW FILE IN OUTPUT DIRECTORY 
f = open(outputdir+"objs.txt", 'w+')

#ITERATE THROUGH EACH FILE AND SEE THE ONES THAT ARE OBJECT FILES WHICH WE APPEND TO OUR FILE 
for item in items:
    if item.endswith(".txt"):
        f.write(item+ "\n")

f.close()
