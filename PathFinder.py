#find_path will find the path that data is located in
#storing the data in different locations leads to errors between users
#add your path to the paths array if yours is different

import os

def find_path(verbose=False):
    paths = ["C:/Users/jon.harris/Desktop/school/final/input/", "data/", "../input/"]
    my_path = ""
    for path in paths:
        try:
            os.listdir(path)
            my_path = path
        except:
            filler_exception=0
    if verbose:
        print("path: {}".format(my_path))
        print("all files in directory: {}".format(os.listdir(my_path)))
    return my_path
