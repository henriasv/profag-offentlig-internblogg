import os
import subprocess

path = "_posts"
currentPath = os.path.dirname(os.path.abspath(__file__))

for dirName, subdirList, fileList in os.walk(path):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if ".ipynb" in fname: 
            os.chdir(os.path.join(os.path.dirname(__file__), dirName))
            subprocess.call(["jupyter", "nbconvert", fname, "--to", "markdown"])
            subprocess.call(["rm", fname])
            os.chdir(currentPath)