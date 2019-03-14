Decimation.py: Iterate through the objects of a specific scene and decimate them by a given amount

    - This script is ran only in the Blender Terminal! 
    - Make sure to change the decimation ratio as need be! 
    - If you have over-decimated, the only solution is to reload all the objects and redo the Decimation with a lower ratio
    - If you would like to decimate again after realizing that your decimation ratio was too low, then make sure to realise that a second decimation will be a decimation on top of the decimation you already did. So if you did a decimation ratio of 0.3 the first time, and then you did 0.5 the second time, you decimated the originial raw objects by 0.3 and then on top of that you have decimated half the vertices of the "0.3 decimated" objects. 