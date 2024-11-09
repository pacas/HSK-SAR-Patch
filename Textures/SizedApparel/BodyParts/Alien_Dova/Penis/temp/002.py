import os

for filename in os.listdir("."):
    new_filename = filename.replace("DogPenis", "OvipositorM")
    new_filename = new_filename.replace("4_RNW_south — копия", "5_RNW_south")
    new_filename = new_filename.replace("4_RNW_east — копия", "5_RNW_east")
    new_filename = new_filename.replace("4_RNW_north — копия", "5_RNW_north")

    os.rename(filename, new_filename)
