import os
import bpy

#THIS ONLY DECIMATES OBJS IN A CURRENT LAYER! IT WILL NOT DECIMATE OBJS IN OTHER LAYERS 

for name in bpy.data.objects.keys(): #gets a list of every single object that's in the scene INCLUDING lights, cameras, backgrounds 
    print("Working on " + name) #print name so we know which object we are on 
    try: 
        bpy.ops.object.mode_set(mode='OBJECT') #switch to OBJECT mode so we can try to decimate
    except: 
        print("OBJECT mode did not work!") # keep moving on if things don't work out 
        pass
    
    obj = bpy.data.objects[name] #get the specific object that we are working on 
    bpy.ops.object.select_all(action="DESELECT") #DESELECT all the objects in the scene 
    obj.select = True #set select boolean flag to true 
    bpy.context.scene.objects.active = obj # select the object that we are currently on 
    
    bpy.ops.object.mode_set(mode='EDIT') # go to EDIT mode for the selected object 
    
    try:
        bpy.ops.mesh.select_all(action="SELECT") # this selects all objects however in Blender when you select all objects, there is a reference object that is shaded differently to which actions are applied 

    except:
        print("Error when I tried to select " +name + ". Probably on a different layer, so skipping...") #move onto the next iteration
        continue

    bpy.ops.mesh.remove_doubles() # allows vertices near each other to be merged into one vertex, making render times smaller 
    bpy.ops.object.mode_set(mode='OBJECT') # go to OBJECT mode for the selected object 
    
    bpy.ops.object.modifier_add(type='DECIMATE') #choose to modify the selected object with the DECIMATE modifier which further reduces number of vertices to speed up renders 
    #CHANGE THIS RATIO AS NEED BE! EXPERIMENT A LITTLE! 
    obj.modifiers["Decimate"].ratio = 0.5 # the ratio is 0.5 here meaning that around half of all vertices will be merged and destroyed 
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate") # finally apply the DECIMATE modifier with the ratio specified 