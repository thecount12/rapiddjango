
import os
import shutil


def clean():	
    my_clean = input("Enter name of project to erase: ")
    if os.path.exists(my_clean):
        print("erasing directory")
        shutil.rmtree(my_clean)


clean()
