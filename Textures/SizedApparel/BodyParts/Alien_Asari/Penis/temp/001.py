import os

for filename in os.listdir("."):
    new_filename = filename.replace("huge", "4_RNW")
    new_filename = new_filename.replace("large", "3_RNW")
    new_filename = new_filename.replace("giant", "5_RNW")
    new_filename = new_filename.replace("small", "1_RNW")
    new_filename = new_filename.replace("micro", "0_RNW")
    
    new_filename = new_filename.replace("penis_insect", "OvipositorM")
    os.rename(filename, new_filename)
