import os
from pathlib import Path

def working_directory(directory):
    owd = os.getcwd()
    print("Current Working Directory is ",  owd )
    try:
        os.chdir(directory)
        print("Changed Directory ", directory)
        yield directory
    finally:
        os.chdir(owd)

def test_function():
    myChangedDir = working_directory('./PYTHON')
    print("My changed Directory is ",  myChangedDir)
    

test_function()



