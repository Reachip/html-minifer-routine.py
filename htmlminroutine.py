import subprocess
from os import listdir
from os.path import isfile, join

def main(path):
    for element in listdir(path):
        element_path = join(path, element)
        
        if isfile(element_path): 
            if element_path.split(".")[2] == "html":
                subprocess.run(["htmlmin", element_path, element_path])
        else:
            main(element_path)


main("./output")
