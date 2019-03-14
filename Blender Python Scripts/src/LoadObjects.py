import os
import bpy

# get list of all files in directory
os.chdir('/home/yor5/Desktop/4.3i_LifeScienceDB_JP') #CHANGE THIS TO BE YOUR DIRECTORY WHERE YOUR TXT LIST OF ALL OBJECTS THAT YOU WANT TO IMPORT IS LOCATED 

file_list = [line.strip() for line in open("objs.txt")] #CHANGE THIS TO BE THE TEXT FILE WITHIN THE CHOSEN DIRECTORY THAT CONTAINS THE TXT LIST OF ALL OBJECTS YOU WANT TO IMPORT 

# get a list of files ending in 'obj'
obj_list = [item for item in file_list if "bone" in item.lower()] #IF YOU WANT TO FILTER THROUGH AND IMPORT FILES THAT CONTAIN A KEY WORD, THIS IS THE LINE THAT TAKES CARE OF IT! CHANGE "bone" TO WHATEVER KEYWORD YOU WANT! 

# loop through the strings in obj_list and add the files to the scene
for path_to_file in obj_list: #IF YOU COMMENTED OUT THE PREVIOUS LINE "OBJ_LIST =...", SINCE YOU DIDN'T WANT TO FILTER BY KEYWORD, THEN REPLACE "obj_list" WITH "file_list"
    bpy.ops.import_scene.obj(filepath = path_to_file)