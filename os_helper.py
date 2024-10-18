import os
import sys

def does_path_exist(path):
    print("Checking if path exists...")
    return os.path.exists(path)

def is_directoty(path):
    print("Checking if path is a directory...")
    return os.path.isdir(path)

def list_dir(path):
    print("Getting all files in the current directory...")
    return os.listdir(path)


def check_user_input(input):
    print(f"Checking user input: {input}")
    # check if input has user
    if (len(input) > 1):
        # set the parent directory path
        parent_dir = f"../{input[1]}"
        if does_path_exist(parent_dir) and is_directoty(parent_dir):
            print(f"User input is valid: {input[1]}")
            return parent_dir
        else:
            print(f"User input is invlaid")
            sys.exit("Input is not a directory or doesn't exists")
    else:
        print(f"User input is invlaid")
        sys.exit("No directory name was entered")
    
# def change_dir(path):
#     print("Changing directory...")
#     os.chdir(path)

def get_current_location():
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    return current_dir